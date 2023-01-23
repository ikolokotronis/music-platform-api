<div id="top"></div>


<h3 align="center">Music Platform REST API</h3>

#### Key functionalities
* Create and manage a personal account
* CRUD posts 
* CRUD tracks with an audio file attached
* Have conversations with other users
* View other accounts/posts/tracks

### Built with

* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)


<!-- GETTING STARTED -->
### Getting Started

This is how to make the project run locally.

#### Installation

1. Clone the repo
  ```
  git clone https://github.com/ikolokotronis/music-platform-api.git
  ```
2. Move to docker directory (assuming you are located in the project's root directory)
  ```
  cd ./src/.docker/
  ```
3. Build the container
  ```
  docker-compose up --build
  ```
4. Now you can access the API at http://127.0.0.1:8080


<!-- ENDPOINTS -->
## Endpoints

### Open Endpoints

Open endpoints require no Authentication.

* Register : `POST /users/register/`
* Login : `POST /users/login/`

### Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired from the Login view or the Register view.
All of the endpoints below require Authentication.

### Current User related

Each endpoint displays or manipulates information related to the User whose
Token is provided with the request:

* Show info: `GET /users/properties/`
* Update info : `PUT /users/properties/`

### Account related

Endpoints for viewing the User Accounts that the Authenticated User
has permissions to access.  
For now it is just a GET request to view account properties of another user.

* Show account's details : `GET /users/properties/:pk/`

### Conversation / Message related
Endpoints for creating messages or viewing conversations that are available for the current user.

* Show conversation list: `GET /conversations/`

Single conversations
* Show single conversation details: `GET /conversations/:pk/`

Messages
* Send a message to another user: `POST /conversations/messages/`

### Track related
Endpoints for viewing, manipulating and creating tracks.

* Show track list: `GET /tracks/`
* Create new track: `POST /tracks/`

Single tracks
* Show single track details: `GET /tracks/:pk/`
* Update single track: `PUT /tracks/:pk/`
* Delete single track: `DELETE /tracks/:pk/`

### Post related
Endpoints for viewing, manipulating and creating posts.

* Show post list: `GET /posts/`
* Create new post: `POST /posts/`

Single posts
* Show single post details: `GET /posts/:pk/`
* Update single post: `PUT /posts/:pk/`
* Delete single post: `DELETE /posts/:pk/`


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
