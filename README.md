# Youtube-Video
This is a Django-based web application that allows users to enter the URL of a video they want to download. The application uses Django's POST method for secure form submissions and includes CSRF protection.

# Features
Secure form submission using Django's POST method
It uses Python Pytube library to download youtube video
It has CSRF protection
It will show Success message upon successful video download
# Requirements
Python 3.x
Django 3.x 
Pytube for YouTube videos
# Installation
# 1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/videodownloader.git
cd videodownloader
# 2. Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
# 3. Install Dependencies
bash
Copy code
pip install django
pip install pytube  # Or any other library you are using for downloading videos
# 4. Set Up the Django Project
bash
Copy code
cd myproject
python manage.py migrate
python manage.py createsuperuser  # Follow the prompts to create a superuser
# 5. Run the Development Server
bash
Copy code
python manage.py runserver
Usage
Once you open the web page
You should be able to see a form where you can enter the URL of the video you want to download.
Enter the URL and click the "Download" button.
If the video is downloaded successfully, you will see a success message.

# Acknowledgments
Django Documentation
Bootstrap Documentation
pytube Documentation
