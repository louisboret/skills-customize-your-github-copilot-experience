# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and validate REST APIs with FastAPI and Pydantic by creating endpoints to manage a simple item catalog.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description
Build the API routes needed to fetch item data from the application.

#### Requirements
Completed project should:

- Create a FastAPI app with at least two routes: `GET /items` and `GET /items/{item_id}`.
- Return JSON responses for each route.
- Include at least three sample items in the API data store.

### 🛠️ Add POST and PUT Support

#### Description
Allow users to add new items and update existing items through the API.

#### Requirements
Completed project should:

- Implement `POST /items` to create a new item from request JSON data.
- Implement `PUT /items/{item_id}` to update an existing item.
- Return the created or updated item in the response.

### 🛠️ Validate Requests and Handle Errors

#### Description
Use Pydantic models for request validation and add error responses for invalid requests.

#### Requirements
Completed project should:

- Define Pydantic models for item input validation.
- Return a `404` response when a requested item ID does not exist.
- Return a `400` response when required request fields are missing or invalid.
