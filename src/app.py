# from flask import Flask, render_template, request

# app = Flask(__name__)

# # Sample profiles data
# profiles = [
#     {
#         "bio": "Loves hiking.",
#         "course": "Biochemistry",
#         "degree": "Biology",
#         "gender": "Female",
#         "id": 1,
#         "name": "Alice"
#     },
#     {
#         "bio": "Avid gamer.",
#         "course": "Software Engineering",
#         "degree": "Computer Science",
#         "gender": "Male",
#         "id": 2,
#         "name": "Bob"
#     }
# ]

# @app.route('/search', methods=['GET'])
# def search_profiles():
#     query = request.args.get('q', '').lower()
#     print(f"Search Query: '{query}'")  # Debugging output
    
#     # Split the query into words for more flexible searching
#     query_words = query.split()  
#     results = [profile for profile in profiles if any(word in profile['name'].lower() or word in profile['bio'].lower() for word in query_words)]
    
#     print(f"Search Results: {results}")  # Debugging output
#     return render_template('search_results.html', query=query, results=results)

# if __name__ == '__main__':
#     app.run(debug=True)
