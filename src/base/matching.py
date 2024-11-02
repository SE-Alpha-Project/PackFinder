#
# Created on Sun Oct 09 2022
#
# The MIT License (MIT)
# Copyright (c) 2022 Rohit Geddam, Arun Kumar, Teja Varma, Kiron Jayesh, Shandler Mason
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from base.models import Profile


WEIGHTS = {
    "gender": 0.4,
    "diet": 0.3,
    "degree": 0.1,
    "course": 0.1,
    "country": 0.1,
}


def similarity_score(gender, degree, diet, country, course):
    """Calculate the similarity score"""
    score = (
        WEIGHTS["gender"] * gender
        + WEIGHTS["diet"] * diet
        + WEIGHTS["degree"] * degree
        + WEIGHTS["country"] * country
        + WEIGHTS["course"] * course
    )

    return score


def matchings(current_user):
    """Generate matches using Manhattan Distance Algorithm"""
    user_profile = Profile.objects.get(user=current_user)
    all_profiles = Profile.objects.exclude(user=current_user)

    match_list = []
    matches = []

    for profile in all_profiles:

        gender = (
            1
            if user_profile.preference_gender == profile.gender
            or user_profile.preference_gender == profile.NO_PREF
            else 0
        )
        degree = (
            1
            if user_profile.preference_degree == profile.degree
            or user_profile.preference_degree == profile.NO_PREF
            else 0
        )
        diet = (
            1
            if user_profile.preference_diet == profile.diet
            or user_profile.preference_diet == profile.NO_PREF
            else 0
        )
        country = (
            1
            if user_profile.preference_country == profile.country
            or user_profile.preference_country == profile.NO_PREF
            else 0
        )
        course = (
            1
            if user_profile.preference_course == profile.course
            or user_profile.preference_course == profile.NO_PREF
            else 0
        )

        score = similarity_score(gender, degree, diet, country, course)

        if score > 0.5:
            match_list.append((profile, score))

    match_list.sort(key=lambda x: x[1], reverse=True)

    for m in match_list:
        matches.append(m[0])

    return matches


def calculate_compatibility_score(user_profile, other_profile):
    total_weight = 0
    weighted_score = 0
    
    # Sleep Schedule Compatibility
    sleep_weight = user_profile.sleep_schedule_importance
    total_weight += sleep_weight
    if user_profile.sleep_schedule == other_profile.sleep_schedule:
        weighted_score += sleep_weight * 1.0
    elif 'Flexible' in [user_profile.sleep_schedule, other_profile.sleep_schedule]:
        weighted_score += sleep_weight * 0.7
    else:
        weighted_score += sleep_weight * 0.3

    # Cleanliness Compatibility
    cleanliness_weight = user_profile.cleanliness_importance
    total_weight += cleanliness_weight
    cleanliness_diff = abs(user_profile.cleanliness - other_profile.cleanliness)
    cleanliness_score = 1 - (cleanliness_diff / 9)  # 9 is max difference
    weighted_score += cleanliness_weight * cleanliness_score

    # Noise Level Compatibility
    noise_weight = user_profile.noise_importance
    total_weight += noise_weight
    if user_profile.noise_level == other_profile.noise_level:
        weighted_score += noise_weight * 1.0
    elif 'Moderate' in [user_profile.noise_level, other_profile.noise_level]:
        weighted_score += noise_weight * 0.7
    else:
        weighted_score += noise_weight * 0.3

    # Guest Preference Compatibility
    guests_weight = user_profile.guests_importance
    total_weight += guests_weight
    guest_levels = {'Rarely': 1, 'Sometimes': 2, 'Often': 3}
    guest_diff = abs(guest_levels[user_profile.guests_preference] - 
                    guest_levels[other_profile.guests_preference])
    guest_score = 1 - (guest_diff / 2)  # 2 is max difference
    weighted_score += guests_weight * guest_score

    # Calculate final percentage
    final_score = (weighted_score / total_weight) * 100
    return round(final_score, 1)


def get_compatible_roommates(user_profile, min_score=50):
    all_profiles = Profile.objects.exclude(user=user_profile.user)
    compatible_roommates = []
    
    for profile in all_profiles:
        score = calculate_compatibility_score(user_profile, profile)
        if score >= min_score:
            compatible_roommates.append({
                'profile': profile,
                'score': score,
                'match_details': get_match_details(user_profile, profile)
            })
    
    return sorted(compatible_roommates, key=lambda x: x['score'], reverse=True)


def get_match_details(user_profile, other_profile):
    details = []
    
    # Sleep Schedule
    if user_profile.sleep_schedule == other_profile.sleep_schedule:
        details.append(f"Perfect sleep schedule match: {user_profile.sleep_schedule}")
    elif 'Flexible' in [user_profile.sleep_schedule, other_profile.sleep_schedule]:
        details.append("Compatible sleep schedules with flexibility")
    
    # Cleanliness
    cleanliness_diff = abs(user_profile.cleanliness - other_profile.cleanliness)
    if cleanliness_diff <= 2:
        details.append("Very similar cleanliness standards")
    elif cleanliness_diff <= 4:
        details.append("Moderately compatible cleanliness standards")
    
    # Noise Level
    if user_profile.noise_level == other_profile.noise_level:
        details.append(f"Perfect noise level match: {user_profile.noise_level}")
    elif 'Moderate' in [user_profile.noise_level, other_profile.noise_level]:
        details.append("Compatible noise preferences")
    
    # Guest Preference
    if user_profile.guests_preference == other_profile.guests_preference:
        details.append(f"Perfect guest preference match: {user_profile.guests_preference}")
    
    return details
