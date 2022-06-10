<div id="top"></div>


<h3 align="center">Music Platform REST API</h3>

<!-- ABOUT THE PROJECT -->
## About The Project

This is a REST API for a music platform with functionalities like tracks, posts, messages etc.  


### Built with

* [Django REST Framework](https://www.django-rest-framework.org/)


<!-- GETTING STARTED -->
## Getting Started

This is how to make the project run locally.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ikolokotronis/music-platform-api.git
   ```
2. Install PIP packages (inside the /src directory)
   ```sh
   pip install -r requirements.txt
   ```
3. Enter your database settings in settings.py. Here is an example if you want to use PostgreSQL:
   ```python
   DATABASES = {
    'default': {
        'HOST': '127.0.0.1',
        'NAME': 'db_name_here',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'user_name_here',
        'PASSWORD': 'password_here',
    }
    }
   ```   
4. Run the server
   ```sh
   python manage.py runserver
   ```


<!-- ENDPOINTS -->
## API Endpoints

<i>will be available soon</i>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

