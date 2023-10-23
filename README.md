# YaCut - URL Shortening Service

YaCut is a simple URL shortening service and API written in Python using the Flask framework. It allows users to shorten long URLs and access the original URLs by providing a unique short identifier.

## Key Features

- Generate short links associated with long URLs.
- Optional custom short link names (up to 16 characters).
- Automatic generation of short links if a custom name is not provided.
- Redirection to the original URL when accessing short links.

## User Interface

The user interface consists of a single page with a form that includes two fields:

1. A required field for the long original URL.
2. An optional field for a custom short link.

If a user provides a custom short link that already exists, the service informs the user.

## API

YaCut provides a simple API with two endpoints:

- `/api/id/`: Accepts POST requests to create a new short link.
- `/api/id/<short_id>/`: Accepts GET requests to retrieve the original URL based on the specified short identifier.

## Getting Started

1. Clone this repository to your local machine.
```
git clone git@github.com:Kapshtyk/yacut.git
cd yacut
```
2. Set up a virtual environment and install the required packages from the `requirements.txt` file.
```
python3 -m venv venv
```
MacOS/Linux:
```
source venv/bin/activate
```
Windows:
```
source venv/scripts/activate
```
```
pip install -r requirements.txt
```
3. Initialize the database (SQLite) for development.
```
flask db upgrade
```
4. Start the Flask application and visit the URL to access the YaCut service.
```
flask run
```

## Custom Short Link Generation

YaCut uses a custom algorithm to generate short link identifiers of variable length. You can customize this algorithm based on your preferences.

## Error Handling

Custom error handlers are implemented for both the user interface and the API to provide informative error messages to users.

For detailed information on how to use the service and API, please refer to the documentation and specifications provided in the `openapi.yml` file. You can also use the Postman collection in the `postman_collection` directory to test and debug the API.

## Acknowledgments

This project was created as part of a sprint assignment. Thank you for checking it out!

## Author
- LinkedIn - [Arseny Kapshtyk](https://www.linkedin.com/in/kapshtyk/)
- Github - [@kapshtyk](https://github.com/Kapshtyk)


