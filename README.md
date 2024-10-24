# Posts Microservice

This microservice handles user posts for the Columbia Forum project.

## Usage

To connect with remote MySQL server, create a `my.cnf` file in the root directory, which should look like:

```
[client]
database=your_database_name    # The name of the remote database you're connecting to
user=your_username             # The username for your remote MySQL instance
password=your_password         # The password for your MySQL user
host=remote_server_ip          # The IP address or hostname of the remote MySQL server
port=3306    
```

Run command:
`python manage.py runserver`
