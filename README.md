# Machine Learning Techniques for Detecting Phishing Websites
This project focuses on detecting phishing websites, a major cause of cybersecurity threats, using advanced machine learning techniques implemented in Python. The aim is to enhance web safety by accurately identifying and mitigating phishing risks.

# Here's a step-by-step guide to set up and run a Django project:

## 1. Set Up Your Environment
  
- Make sure you have Python installed (version 3.6 or later is recommended). You can download it from[ python.org](https://www.python.org).
```
pip install pip
```

- Install Dependencies Install the required packages listed in the requirements.txt file. This file is typically found in the root of the project and contains all necessary packages.
  
```
pip install -r requirements.txt
```
## 2. Install Django

Once your virtual environment is activated, install Django using pip:
```
pip install django
```
## 3. Set Up Database (if applicable)
```
python manage.py migrate
```

## 4. Create a Superuser (Optional)

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

