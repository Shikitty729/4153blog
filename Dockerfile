# Use a Python base image
FROM python:3.12-slim

# add dependencies for mysqlclient
RUN apt-get update && apt-get install -y  \
    pkg-config  \
    default-mysql-client  \
    default-libmysqlclient-dev \
    build-essential

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the app port
EXPOSE 8080

# Command to run your app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
