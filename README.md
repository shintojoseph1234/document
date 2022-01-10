# Document API

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


A text saving and retrieval web app using Django. Able to save short text snippets with a title, timestamp and created user. The snippet also contain a relation to a Tag model (with only title field). Tag title is unique. Check whether the tag with the same title exists or not before creating a new one. If the same tag exists link to that tag. Implement JWT authentication for getting user.

## Installation

Install virtual enviroonment  [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) for Dependency Management

```bash
pip install virtualenv
```
Create and Activate a virtual environment

```bash
virtualenv --python=python3 document_env
source document_env/bin/activate
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
pip install --upgrade -r requirements.txt
```
Run the server
```bash
python manage.py runserver 8000
```

Or execute Dockerfile and start the container
```bash
docker build -t document:v0 .
docker run -it -p 8000:8000 document:v0
http://localhost:8000/
```


Open  [localhost:8000](http://localhost:8000/)  in a browser to see the Swagger API  Documentation

Open  [localhost:8000/docs](http://localhost:8000/docs/)  in a browser to see the Django API  Documentation

Open  [localhost:8000/redoc](http://localhost:8000/redoc/)  in a browser to see the OpenAPI specification

Open  [localhost:8000/api](http://localhost:8000/api/)  in a browser to see the available API


## Authentication API's

* Login API.
   ```bash
   http://localhost:8000/api/token/
   ```

	```bash
	curl -X POST "http://localhost:8000/api/token/" -H  "Content-Type: application/json" -d "{  \"username\": \"shinto\",  \"password\": \"shinto\"}"

	{
		"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MTkyODkyOSwiaWF0IjoxNjQxODQyNTI5LCJqdGkiOiJkMGZhNjVhMDFmY2U0NDM3OGNmYTUxZTIxNThlNjdkNCIsInVzZXJfaWQiOjF9.t9f4xJLjp3DNtE8Bb5MtlZXGPWd2l2QU1X2zB4QbgV0",
		"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQxODQyODI5LCJpYXQiOjE2NDE4NDI1MjksImp0aSI6IjkxN2JiNjY1OWFmZjRhZTZiZWEyYjc3YmQyMWMxZDUwIiwidXNlcl9pZCI6MX0.A2wqS9VZd0sb8R4qLItZRI5fJa1i24-lTPOlKH9hGuQ"
	}
	```

* Refresh API.
   ```bash
	 http://localhost:8000/api/token/refresh/
   ```

	```bash
	curl -X POST "http://localhost:8000/api/token/refresh/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: UOpIwxKrBSLlDbyEOPPAf6qPsQA5ENVPBwBRt3IzgTeg2ibcHdctGkdwBKnt5JEb" -d "{  \"refresh\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MTkyODkyOSwiaWF0IjoxNjQxODQyNTI5LCJqdGkiOiJkMGZhNjVhMDFmY2U0NDM3OGNmYTUxZTIxNThlNjdkNCIsInVzZXJfaWQiOjF9.t9f4xJLjp3DNtE8Bb5MtlZXGPWd2l2QU1X2zB4QbgV0\"}"

	{
		"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQxODQyODU3LCJpYXQiOjE2NDE4NDI1MjksImp0aSI6ImE5NDgyY2M0ZmYxZDQ5ZGU5YWI0M2UzZDE1OTBmMzE5IiwidXNlcl9pZCI6MX0.9pWTdu2py8bXkUdNMdHXRIlOs_81fJp6TQq9MeqqDWA"
	}
	```


## CRUD API's

* Overview API.
   ```bash
	 http://localhost:8000/api/content/overview/
   ```

	 ```bash
	 curl -X GET "http://localhost:8000/api/content/overview/" -H  "accept: application/json" -H  "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQxODQyODU3LCJpYXQiOjE2NDE4NDI1MjksImp0aSI6ImE5NDgyY2M0ZmYxZDQ5ZGU5YWI0M2UzZDE1OTBmMzE5IiwidXNlcl9pZCI6MX0.9pWTdu2py8bXkUdNMdHXRIlOs_81fJp6TQq9MeqqDWA"


	 {
	  "count": 5,
	  "snippets": [
	    {
	      "url": "http://localhost:8000/api/content/5/"
	    },
	    {
	      "url": "http://localhost:8000/api/content/1/"
	    },
	    {
	      "url": "http://localhost:8000/api/content/2/"
	    },
	    {
	      "url": "http://localhost:8000/api/content/3/"
	    },
	    {
	      "url": "http://localhost:8000/api/content/4/"
	    }
	  ]
	}
	 ```


* Create API.

	 ```bash
		curl -X POST "http://localhost:8000/api/content/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQxODQyODU3LCJpYXQiOjE2NDE4NDI1MjksImp0aSI6ImE5NDgyY2M0ZmYxZDQ5ZGU5YWI0M2UzZDE1OTBmMzE5IiwidXNlcl9pZCI6MX0.9pWTdu2py8bXkUdNMdHXRIlOs_81fJp6TQq9MeqqDWA" -d "{  \"title\": \"string\",  \"timestamp\": \"2022-01-10T19:33:26.185Z\",  \"created_by\": \"string\"}"

		{
		 "id": 6,
		 "title": "string",
		 "timestamp": "2022-01-10T19:33:26.185000Z",
		 "created_by": "string"
		}
	 ```



* Detail API.

	 ```bash
	 curl -X GET "http://localhost:8000/api/content/" -H  "accept: application/json" -H  "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQxODQyODU3LCJpYXQiOjE2NDE4NDI1MjksImp0aSI6ImE5NDgyY2M0ZmYxZDQ5ZGU5YWI0M2UzZDE1OTBmMzE5IiwidXNlcl9pZCI6MX0.9pWTdu2py8bXkUdNMdHXRIlOs_81fJp6TQq9MeqqDWA"

		[
		  {
		    "id": 1,
		    "title": "string",
		    "timestamp": "2022-01-08T20:54:19.517000Z",
		    "created_by": "string"
		  },
		  {
		    "id": 2,
		    "title": "string",
		    "timestamp": "2022-01-08T20:54:19.517000Z",
		    "created_by": "string"
		  }
		]
	 ```

* Update API.
  ```bash
	 curl -X PUT "http://localhost:8000/api/content/1/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQxODQyODU3LCJpYXQiOjE2NDE4NDI1MjksImp0aSI6ImE5NDgyY2M0ZmYxZDQ5ZGU5YWI0M2UzZDE1OTBmMzE5IiwidXNlcl9pZCI6MX0.9pWTdu2py8bXkUdNMdHXRIlOs_81fJp6TQq9MeqqDWA" -d "{  \"title\": \"string\",  \"timestamp\": \"2022-01-10T19:39:45.097Z\",  \"created_by\": \"string\"}"

	 {
	   "id": 1,
	   "title": "string",
	   "timestamp": "2022-01-10T19:39:45.097000Z",
	   "created_by": "string"
	 }
  ```

* Delete API.
  ```bash
	 curl -X DELETE "http://localhost:8000/api/content/1/" -H  "accept: application/json" -H  "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQxODQyODU3LCJpYXQiOjE2NDE4NDI1MjksImp0aSI6ImE5NDgyY2M0ZmYxZDQ5ZGU5YWI0M2UzZDE1OTBmMzE5IiwidXNlcl9pZCI6MX0.9pWTdu2py8bXkUdNMdHXRIlOs_81fJp6TQq9MeqqDWA"
  ```

* Tag list API.
  ```bash
	 curl -X GET "http://localhost:8000/api/tag/" -H  "accept: application/json" -H  "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQxODQyODU3LCJpYXQiOjE2NDE4NDI1MjksImp0aSI6ImE5NDgyY2M0ZmYxZDQ5ZGU5YWI0M2UzZDE1OTBmMzE5IiwidXNlcl9pZCI6MX0.9pWTdu2py8bXkUdNMdHXRIlOs_81fJp6TQq9MeqqDWA"

	 [
	  {
	    "title": "shhh"
	  },
	  {
	    "title": "shinto"
	  },
	  {
	    "title": "string"
	  }
	]
  ```

* Tag Detail API.
  ```bash
	curl -X GET "http://localhost:8000/api/tag/1/" -H  "accept: application/json" -H  "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQxODQyODU3LCJpYXQiOjE2NDE4NDI1MjksImp0aSI6ImE5NDgyY2M0ZmYxZDQ5ZGU5YWI0M2UzZDE1OTBmMzE5IiwidXNlcl9pZCI6MX0.9pWTdu2py8bXkUdNMdHXRIlOs_81fJp6TQq9MeqqDWA"

	[
	  {
	    "id": 2,
	    "title": "string",
	    "created_by": "string",
	    "timestamp": "2022-01-08T20:54:19.517000Z",
	    "tag_id": 1
	  },
	  {
	    "id": 3,
	    "title": "string",
	    "created_by": "string",
	    "timestamp": "2022-01-08T21:43:54.804000Z",
	    "tag_id": 1
	  },
	]
  ```
