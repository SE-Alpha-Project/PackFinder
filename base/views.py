from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'base/profile.html')

@login_required
def inbox(request):
    return render(request, 'base/inbox.html')

@login_required
def compatibility_quiz(request):
    return render(request, 'base/compatibility_quiz.html')

@login_required
def find_people(request):
    return render(request, 'base/find_people.html') 