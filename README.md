<div id="top"></div>


<h3 align="center">Music Platform REST API</h3>

<!-- ABOUT THE PROJECT -->
### About The Project

This is a REST API for a music platform with functionalities like tracks, posts, messages etc.  


### Built with

* [Django REST Framework](https://www.django-rest-framework.org/)


<!-- GETTING STARTED -->
### Getting Started

This is how to make the project run locally.

#### Installation

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
## Endpoints

### Open Endpoints

Open endpoints require no Authentication.

* Register : `POST /users/register/`
* Login : `POST /users/login/`

### Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired from the Login view or the Register view.

### Current User related

Each endpoint manipulates or displays information related to the User whose
Token is provided with the request:

* Show info: `GET /users/properties/`
* Update info : `PUT /users/properties/`

### Account related

Endpoints for viewing and manipulating the Accounts that the Authenticated User
has permissions to access.  
For now it is just a GET request to view account properties of another user.

* Show An Account : `GET /users/properties/:pk/`

### Track related
Endpoints for viewing and manipulating tracks.

* Show track list: `GET /tracks/`
* Create new track: `POST /tracks/`

Endpints for a single track
* Show single track details: `GET /tracks/:pk/`
* Update single track: `PUT /tracks/:pk/`
* Delete single track: `DELETE /tracks/:pk/`

### Post related
Endpoints for viewing and manipulating posts.

* Show post list: `GET /posts/`
* Create new post: `POST /posts/`

Endpints for a single post
* Show single post details: `GET /posts/:pk/`
* Update single post: `PUT /posts/:pk/`
* Delete single post: `DELETE /posts/:pk/`

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

