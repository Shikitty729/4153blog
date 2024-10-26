# Posts Microservice

This microservice handles user posts for the Columbia Forum project.

## Usage

To connect with our remote MySQL server on AWS, create a `my.cnf` file in the root directory, which should look like:

```
[client]
database=your_database_name    # The name of the remote database you're connecting to
user=your_username             # The username for your remote MySQL instance
password=your_password         # The password for your MySQL user
host=remote_server_ip          # The IP address or hostname of the remote MySQL server
port=3306    
```

Run the Django project using:
`python manage.py runserver`

To sync with the database after updating data models in `models.py`, run
```
python manage.py makemigrations
python manage.py migrate
```


## Deployment

The service is deployed using Google Cloud Run here.


## API Endpoints

### Create Post

- **Endpoint**: `/posts/`
- **Method**: `POST`
- **Description**: Creates a new post with the provided title and content.
- **Request Body**:
    - `title` (string): The title of the post.
    - `content` (string): The content of the post.


### Get Post

- **Endpoint**: `/posts/<int:pid>/`
- **Method**: `GET`

### Get All Posts

- **Endpoint**: `/all_posts/`
- **Method**: `GET`


### Put Post

- **Endpoint**: `/posts/<int:pid>/`
- **Method**: `PUT`
- **Request Body**:
    - `title` (string): The title of the post.
    - `content` (string): The content of the post.


### Delete Post

- **Endpoint**: `/posts/<int:pid>/`
- **Method**: `DELETE`
