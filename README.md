# Mental Health Therapy Management API
## API Overview
This is a Flask-based API for managing therapy client cases in a mental health institute. The API includes features for user authentication, role management, and case management using JWT tokenization for secure authentication. **SQLite** is used for storing user credentials and case data. The backend is deployed publicly and is testable via Postman.

## Features
1. User Authentication
   *  POST /auth/register: Register a clinician with a username and password (Role: Junior by default).
   * POST /auth/login: Authenticate a clinician and return a JWT token for session management.
2. Role Management
   * POST /auth/promote: Promote a clinician from "Junior" to "Senior" with a valid username and password.
   * POST /auth/demote: Demote a clinician from "Senior" to "Junior".
3. Therapy Case Management
    * GET /cases/cases: Fetch the list of all therapy cases.
    * POST /cases/case: Add a new therapy case.
4. JWT Authentication

## File Structure:

* app.py: The main entry point of the application, initializes the Flask app, sets up the blueprints, and starts the app.
* routes/: Contains the blueprints for authentication and case management, each in their respective files.
* db.py: Handles database connection and setup. This file contains the logic for connecting to the SQLite3 database and initializing the tables using SQL queries from setup_db.sql.
* models.py: Contains classes that represent database models (User and Case), with methods for interacting with the database (e.g., adding users or retrieving cases).
* jwt_util.py: Provides functions for generating and decoding JWT tokens.
* wrapper.py: Defines the token_required decorator, ensuring that routes requiring authentication are protected.
* build.sh /vercel.json:Use for the deployment using vercel.
* .env  : use to define secret key that used for authentication
## Backend Setup Instructions
1.   Clone the Repository
```
git clone https://github.com/pathu11/Therapy-Management-System.git
cd Therapy-Management-System
```
2. Install Dependencies

  ### Create a virtual environment
```bash 
python3 -m venv venv
```
  ### Activate the virtual environment:

```bash 
venv\Scripts\activate  # on windows
```
  ### Install Python Requirements

```bash 
pip install -r requirements.txt
```

## Start the Application
 #### To run the application locally, follow these steps:

  1. Modify app.py to work locally (replace 'app = create_app()' with this code segment )
```bash
   # Local development environment condition
    if __name__ == '__main__':
        app = create_app()
        app.run(debug=True)  # Will run on http://127.0.0.1:5000
```
2. **Running Locally**: For local development, users will run `python app.py`, and the application will be accessible at `http://127.0.0.1:5000`.

```bash 
python app.py
```
#### The server will start running, typically on http://127.0.0.1:5000

3. **Deployment on Vercel**: For deployment, Vercel takes care of the serverless deployment, so you don't need the `if __name__ == '__main__':` block in your deployed version. This block is just for local development.


## Testing the API Using Postman
1. Register a New User:
  * Method: POST
  * URL: http://127.0.0.1:5000/auth/register
  * Body:
```bash
{
        "fullname":"new user name".
        "username": "newuser",
        "password": "newpassword"
}
```
2. Login as already registered user:
  * Method: POST
  * URL: http://127.0.0.1:5000/auth/login
  * Body:
```bash
{
        
        "username": "user name",
        "password": "user's password"
}
```
   * Response(success):
```bash
{
  "token": "your_jwt_token_here"
}
```
3. Promote an user from Senior to Junior:
  * Method: POST
  * URL: http://127.0.0.1:5000/auth/promote
  * Body:
```bash
  {
       
        "username": "user name",
        "password": "user's password"
}
```
  * Headers: Authorization: Bearer your_jwt_token_here
    
4. Demote an user from  Junior to Senior:
  * Method: POST
  * URL: http://127.0.0.1:5000/auth/demote
  * Body:
```bash
{   
    "username": "user name",
    "password": "user's password"
}
```
  * Headers: Authorization: Bearer your_jwt_token_here
 
5. Get All Therapy Cases:
  * Method: GET
  * URL: http://127.0.0.1:5000/cases/cases
  * Headers: Authorization: Bearer your_jwt_token_here

6. Add a New Case:
  * Method: POST
  * URL: http://127.0.0.1:5000/cases/case
  * Body:
```bash
{
  "name": "John Doe",
  "description": "A 35-year-old man with depression and difficulty focusing at work."
}

```
  * Headers: Authorization: Bearer your_jwt_token_here

##  Deployment on Vercel
 ##### To deploy your application on Vercel:

 1.  Make sure you have linked your project to GitHub.
 2.  Go to the Vercel Dashboard, create a new project, and 
 3.  link it to your GitHub repository.
 4.  Vercel will automatically detect the Flask app and deploy it as a serverless function.
 5.  After deployment, you'll get a public URL for the API, which you can share with others for testing.

 ### Why Not Use GitHub Pages?
 GitHub Pages is designed for hosting static websites and cannot run server-side code like Flask. In contrast, Vercel is built for deploying dynamic, serverless applications, including Flask APIs. Vercel handles server setup, scaling, and deployment, making it the ideal choice for hosting a Flask API with full backend support.

## Backend Deployed on Vercel
This backend has been deployed using Vercel. You can access and test the API using the following link:
 [Mental Health Therapy API on Vercel](https://therasphere.vercel.app/)

## Final Notes
Thank you for reviewing this API. If you have any questions or feedback, feel free to reach out:
 * Email : [pathuahinsa2001@gmail.com](mailto:pathuahinsa2001@gmail.com)
 
