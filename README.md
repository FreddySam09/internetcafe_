# internetcafe_

Flask-Python Website based Slot Pre-booking & Educational Guidance Platform

Flask Application Documentation
Overview
This Flask application is designed to manage computer bookings, user accounts, staff interactions, and user queries. It provides features for user registration, login, computer pre-booking, professional help queries, and staff management.

Components 
1. run.py
This script is the entry point of your Flask application. It initializes the Flask app, creates the database tables, and starts the development server.

2. app/init.py
This module initializes the Flask app and sets up various configurations, including database configuration, secret key, and login manager.

3. app/forms.py
This module defines the various forms used in the application. It includes form classes for user registration, login, staff registration, queries, etc.



4. app/models.py
This module defines the data models for your application. It includes classes that define the structure of your database tables, such as User, Doubt, ComputerBooking, Staff, and Query.

5. app/routes.py
This module defines the different routes and their associated view functions. It handles the logic for rendering templates, processing form submissions, and interacting with the database.

6. Templates (HTML files)
These are the frontend templates that define how your web pages are displayed. They are stored in the templates folder and are rendered using data from the backend.

7. Static Files
The static folder contains static assets such as CSS stylesheets, JavaScript files, and images that are used to style and enhance the frontend of your application.

8. Database (site.db)
This SQLite database file is where the application's data is stored. It contains tables corresponding to your defined models and holds the actual user information, booking records, queries, etc.

9. Other Files
There might be other configuration files or resources that your application uses, such as configuration files, additional Python scripts, or custom modules.

10. Virtual Environment
It's common practice to use a virtual environment to manage the dependencies of your Flask application. This keeps your project's dependencies isolated from the global Python environment.

11. Dependencies
Your application depends on various Python packages, including Flask, Flask-WTF, Flask-SQLAlchemy, Flask-Login, and possibly others. These packages are specified in a requirements.txt file and are installed within your virtual environment.

Routes and Functionality
Routes define the different URL paths that users can access in your Flask application. These routes are associated with specific functions that handle user requests, perform operations, and render templates.

/signup: Allows users to register with their name, email, and password. A new User entry is added to the database.

/login: Enables user login with their email and password. On successful login, the user is redirected to the home page.

/logout: Logs out the current user and clears the session.

/home: Displays the home page after login, providing an overview of available functionalities.

/pre-booking: Presents a calendar with available dates for computer pre-booking. Prevents bookings within the next 2 days.

/pre-booking/<selected_date>: Shows available slots for the selected date, preventing double booking.

/computer-booking/<slot>/<date>: Allows users to book available computers for specific slots and dates.

/help: Allows users to post doubts and staff to provide replies.

/professional-help: Displays a list of staff members categorized by department, enabling users to submit queries.

/query-staff/int:staff_id: Allows users to send queries to specific staff members.

/staff-signup: Enables staff registration, similar to user signup.

/staff-login: Allows staff members to log in with their credentials.

/staff-home: Displays the staff home page with staff-specific features.

/staff-queries: Shows queries addressed to staff members and allows them to respond.

/payment-confirmation: Displays a confirmation page after successful payment for computer bookings.

Database Models:
Models define the structure of your application's data and allow you to interact with the database. Each model corresponds to a table in the database and contains fields that represent the attributes of the data. By using models, you can organize and manage data efficiently in your Flask application.

User: Represents registered users with attributes like name, email, password, last_booking_date, and user_type.

Doubt: Represents user-posted doubts with a text field and associated replies.

Reply: Represents replies to doubts, associated with a specific doubt.

ComputerBooking: Represents computer bookings with user, computer, slot, booking date, and booked-by information.

Staff: Represents staff members with attributes like name, email, password, department, and phone number.

Query: Represents user queries directed to staff, associated with user and staff members.



Form Classes:
Forms play a crucial role in gathering and validating user input in a Flask application. This application uses Flask-WTF forms to manage user interactions such as user registration, login, staff registration, querying, and more.

SignupForm
Allows users to register with their name, email, and password.

LoginForm
Enables user login using their email and password.

StaffSignupForm
Allows staff members to register with their information.

StaffLoginForm
Enables staff members to log in using their email and password.

QueryForm
Allows users to post queries and staff to provide replies.

Templates:
1. base.html:
This is the base template that other templates extend. It includes the common structure, navigation bar, and styles for your web application. It also defines blocks that can be overridden by child templates.

2. welcome.html:
A template that extends base.html. It displays a welcome message and provides options for user sign-up and login.

3. signup.html and login.html:
Templates for user registration and login, respectively. They extend base.html and include forms for users to input their credentials.

4. home.html:
A template that extends base.html and displays the user's home page. It welcomes the user and provides options for pre-booking, collaborative help, and professional help.

5. days.html:
A template for selecting a date for pre-booking. It displays a list of dates and links to slots available for booking.

6. pre_booking.html:
Displays a form for users to select a time slot to pre-book a computer system. It includes dynamic options based on availability and shows booked computers.

7. computer_booking.html:
Displays a form for booking a specific computer within a time slot. It also provides information about the availability of computers.

8. payment_confirmation.html:
A simple HTML page for simulating payment confirmation after booking.

9. help.html:
Displays educational help options. Users can post queries and view replies.

10. professional_help.html:
Displays professional help options. Users can select a department and view staff members for querying.

11. query_staff.html:
Allows users to send queries to staff members.

12. staff_signup.html and staff_login.html:
Templates for staff members to sign up and log in.

13. staff_home.html:
A template for staff members' home page. Displays a welcome message and options to view queries.

14. staff_queries.html:
Displays queries from students and provides a form for staff to respond.

These templates use the Flask templating engine to render dynamic content and extend the base template. The navigation bar changes based on whether the user is logged in and their role (user or staff). Forms use Flask-WTF to generate and handle form fields, and validation is performed to ensure data integrity.

The application is structured with routes (@app.route(...)) that link URL endpoints to specific functions. These functions render the corresponding templates, handle form submissions, and interact with the database using SQLAlchemy. The database models are not explicitly provided in your code snippet, but they likely define tables for users, queries, responses, staff members, etc.

The code also handles user authentication, session management, and authorization based on user roles (user or staff). It utilizes Flask's request object to access form data and session information, and it includes error handling using flash messages.


Conclusion
This Flask application provides a user-friendly interface for computer bookings, user queries, and staff interactions. Users can register, book computers, and seek professional help. Staff members can log in, respond to queries, and manage their profile. The application leverages Flask, Flask-WTF, Flask-SQLAlchemy, and Flask-Login to achieve its functionalities.

