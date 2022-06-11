# Blog Application for Doctors and Patient

This is a blog application where doctors can upload blogs in various categories and the patients can view these blogs. 

Types of Users: Doctors who can upload the blogs or create drafts and Patients who can view only the uploaded blogs.

# Tasks Accomplished: 
1) Blog Creation form which can be used by the doctors to create blogs.
2) Form contains the required fields like title, image, category, summary and content. (Categories include Mental Health, Heart Disease, Covid19, Immunization)
3) This Blog Creation form also has a field where the doctor can specify if the given blog needs to be published or left as a draft. 
4) Doctor can view all the blogs, his own blogs, his drafts too while the patient can view only the blogs that are published and not drafts.
5) The patient and doctor can view the blogs category wise. 
6) WHile displaying each blog, they contain category, title, summary and content. The summary and content are truncated with ... if they exceed the given size.
7) MySQL database has been used.

# Tech Stack Used:
Django Framework - Python (Backend)

HTML, CSS and Bootstrap (Frontend)

MySQL (Database)

# Libraries that need to be installed: 
django: pip install django

# To start the server and view the website
Step 1: Run python manage.py runserver

Step 2: Go to the Browser and enter http://127.0.0.1:8000/

# Screenshots of the application:

1) Home Page: 

<img width="750" alt="image" src="https://user-images.githubusercontent.com/83284855/172517373-ca37a776-b66c-4782-9e87-5dcde5e2f118.png">
