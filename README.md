# amigo-social-network
A social network.. with features like status updates, likes, dislikes, commenting, friends, private messages etc.. project currently under developement

#Technologies used:
Django
sqlite3 for database
bootstrap3

#things to install to get this up and running...using "pip"
django-registraton-redux
pillow
python-dev
django-crispy-forms

#delete the database.. then run the following commands to set up
python manage.py makemigrations
python manage.py migrate
python manage.py syncdb

#to run the server
python manage.py runserver

#things currently working
Registration
Status updates
Sending and Accepting Friend request
full view of newsfeed, including status updates from your friends .. all in a unified and sorted mannner
