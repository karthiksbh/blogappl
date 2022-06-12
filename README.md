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

HTML, CSS, Bootstrap and Javascript(Frontend)

MySQL (Database)

# Technical Requirements: 
Used MYSQL database as given in the task.

<img width="750" alt="image" src="https://user-images.githubusercontent.com/83284855/173212229-9579827c-3211-4f6e-83e9-978bf54abf1e.png">


# Libraries that need to be installed: 
django: pip install django

mysqlclient: pip install mysqlclient

# To start the server and view the website
Step 1: Run python manage.py runserver

Step 2: Go to the Browser and enter http://127.0.0.1:8000/

# Screenshots of the application:

1) Home Page: 

<img width="750" alt="image" src="https://user-images.githubusercontent.com/83284855/172517373-ca37a776-b66c-4782-9e87-5dcde5e2f118.png">


2) Blogs Dashboard for the Patient with categories(After logging in a patient): 

This displays the blogs of all the doctors that are present and not just the logged in doctor.

<img width="750" alt="image" src="https://user-images.githubusercontent.com/83284855/173212246-db512deb-e58b-4c39-8d6d-ecf583785ac6.png">


3) Blog Dashboard for Doctor with categories and other options(After logging in a doctor): 

<img width="750" alt="image" src="https://user-images.githubusercontent.com/83284855/173212056-93435d61-2832-419f-aa8a-3f2c1caa1443.png">


4) Current Blogs of the Logged In Doctor: 

<img width="750" alt="image" src="https://user-images.githubusercontent.com/83284855/173212066-e9084986-002d-40eb-9b65-ca54c73413bc.png">


5) Drafts of the Logged In Doctor(which are not published): 

<img width="750" alt="image" src="https://user-images.githubusercontent.com/83284855/173212146-946d2029-2c9d-46ab-8186-563fbc9e89db.png">


6) Page to Create Blogs(for the doctor):

<img width="750" alt="image" src="https://user-images.githubusercontent.com/83284855/173212167-d7e91911-1bf8-49c7-9f54-73e7a389bcdc.png">



