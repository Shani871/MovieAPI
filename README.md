

# 🎬 Movie API with Django REST Framework (DRF)

A Django REST Framework-based Movie API that allows users to search, filter, and paginate through a movie database.

## 📦 Features

- ✅ **Search Functionality:** Search movies by name using a search bar.
- ✅ **Pagination Support:** Browse movies with pagination.
- ✅ **Django REST Framework Integration:** Built using Django REST Framework for API handling.
- ✅ **Simple UI:** Basic HTML template for movie listing and navigation.

---

## 🚀 Technologies Used

- **Python 3.x**
- **Django 4.x**
- **Django REST Framework (DRF)**
- **SQLite (default database)**
- **Bootstrap (for basic styling)**

---

 # Project documentation

🎯 Setup and Installation
	1.Clone the Repository:

      git clone https://github.com/username/movie-api.git
      cd movie-api

2. Create a Virtual Environment:

       python -m venv venv
       source venv/bin/activate  # Mac/Linux
       venv\Scripts\activate     # Windows

3.	Install Dependencies:

        pip install -r requirements.txt


4.	Run Migrations:

         python manage.py makemigrations
         python manage.py migrate


5.	Create a Superuser (Optional for Admin Access):

         python manage.py createsuperuser


6.	Run the Development Server:

            python manage.py runserver


7.	Access the API:
	  •	API Endpoint: http://127.0.0.1:8000/api/movies/
	•	Admin Panel: http://127.0.0.1:8000/admin/

🖥️ Movie List Page Example (HTML)

<form action="" method="get">
    <input type="search" name="movie_name" placeholder="Search Movies">
    <button type="submit">Search</button>
</form>

{% for movie_item in movie_object %}
    <p>{{ movie_item.name }}</p>
{% endfor %}

{% if movie_object.has_previous %}
    <a href="?page=1">First</a>
    <a href="?page={{ movie_object.previous_page_number }}">Previous</a>
{% endif %}

Page: {{ movie_object.number }} of {{ movie_object.paginator.num_pages }}

{% if movie_object.has_next %}
    <a href="?page={{ movie_object.next_page_number }}">Next</a>
    <a href="?page={{ movie_object.paginator.num_pages }}">Last</a>
{% endif %}

📡 API Endpoints
	•	List Movies: GET /api/movies/
	•	Retrieve a Movie: GET /api/movies/<id>/
	•	Search Movies: GET /api/movies/?search=<name>
	•	Create a Movie: POST /api/movies/ (Admin access only)
	•	Update a Movie: PUT /api/movies/<id>/ (Admin access only)
	•	Delete a Movie: DELETE /api/movies/<id>/ (Admin access only)

✅ Example API Response (JSON)

{
    "id": 1,
    "name": "Inception",
    "genre": "Sci-Fi",
    "release_year": 2010
}

✅ Testing the API (Using Postman)
	•	GET Request: Fetch all movies.
	•	POST Request: Add a new movie.
	•	PUT Request: Update an existing movie.
	•	DELETE Request: Delete a movie.

🎯 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions.

📃 License

This project is licensed under the MIT License. See the LICENSE file for details.

⭐ Star this repository if you find it useful!

This `README.md` includes installation steps, project structure, example code, API endpoints, and a sample JSON response for your Django REST Framework Movie API project. Let me know if you need any modifications! 🚀
