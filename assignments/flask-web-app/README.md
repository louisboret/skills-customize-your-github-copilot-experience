# 📘 Assignment: Flask Web App

## 🎯 Objective

Build a simple Flask web application with routes, HTML templates, and form handling so students can submit and view data in a browser.

## 📝 Tasks

### 🛠️ Create the Flask application

#### Description
Create a Flask app with a homepage route and a route to add new data through a form.

#### Requirements
Completed project should:

- Use `Flask` and create an app instance.
- Add a route for `/` that renders a homepage template.
- Add a route for `/add-student` that renders a form template.
- Use `render_template()` to return HTML pages.


### 🛠️ Handle form submissions

#### Description
Implement form handling so students can submit a name and grade, and the app stores the results in memory.

#### Requirements
Completed project should:

- Accept `POST` submissions at `/add-student`.
- Save valid student entries in a list stored in memory.
- Redirect the user back to the homepage after a successful form submission.


### 🛠️ Validate input and display entries

#### Description
Validate the form input and display the submitted student list on the homepage.

#### Requirements
Completed project should:

- Check that both name and grade are provided before saving.
- Show a validation error message on the form page when fields are missing.
- Display a list of added students on the homepage.
