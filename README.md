# Machine Learning Techniques for Detecting Phishing Websites
This project focuses on detecting phishing websites, a major cause of cybersecurity threats, using advanced machine learning techniques implemented in Python. The aim is to enhance web safety by accurately identifying and mitigating phishing risks.

## Here's a step-by-step guide to set up and run a Django project:

### 1. Set Up Your Environment
  
- Make sure you have Python installed (version 3.6 or later is recommended). You can download it from[ python.org](https://www.python.org).
```
pip install pip
```

- Install Dependencies Install the required packages listed in the requirements.txt file. This file is typically found in the root of the project and contains all necessary packages.
  
```
pip install -r requirements.txt
```
### 2. Install Django

Once your virtual environment is activated, install Django using pip:
```
pip install django
```
### 3. Set Up Database (if applicable)
```
python manage.py migrate
```

### 4. Create a Superuser (Optional)

- Default is a username and password is admin and admin
 - or 
- Follow the prompts to create the superuser account.
 ```
python manage.py createsuperuser
```

## 5. Run the Development Server Start the Django development server with:
```
python manage.py runserver
```


# Unsplash API Setup Guide

This guide will help you set up and use the Unsplash API in your application.

## Step-by-Step Guide

### 1. Create an Unsplash Account
- Visit [Unsplash](https://unsplash.com/) and sign up for a new account if you don't have one.

### 2. Create an Application
- After logging in, navigate to the [Unsplash Developer page](https://unsplash.com/developers).
- Click on the **Your Apps** tab.
- Click on the **New Application** button.
- Fill out the application form:
  - **Application Name**: Name your app.
  - **Description**: Describe what your app does.
- Click **Create Application**.

### 3. Obtain Access Key and Secret Key
- After creating your application, you will see your **Access Key** and **Secret Key**. Use the Access Key to authenticate your requests.
- Keep your Secret Key confidential.

### 4. Read the API Documentation
- Familiarize yourself with the [Unsplash API documentation](https://unsplash.com/documentation) for available endpoints, request methods, and usage guidelines.

### 5. Make API Requests
- Use the Access Key to make API requests. Here’s an example in Python using the `requests` library( Use in `features24.html` , `features25.html` ):
```
In HTML(features25,features24)

const apiKey = 'use your api key';

```
# Screenshot
<figure>
  <p align="center">
  <img src="Screenshot/home.jpg" width="1000" " />
  </p>
  <figcaption> Fig.1: Home </figcaption>
</figure>
<figure>
  <p align="center">
  <img src="Screenshot/indox.jpg" width="1000" " />
  </p>
  <figcaption> Fig.2: Indox </figcaption>
</figure>

# References

- [Vaibhav Bichave](https://github.com/vaibhavbichave/Phishing-URL-Detection/tree/master)
- [UI/UX Design](https://play.teleporthq.io/)
  



