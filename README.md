# doctophoto
Web application, built with Django, that allows doctor to send radiography images with description to his patients.
Doctors only see descriptions they made and patients only see their own descriptions.
It was a group project for PRO subject at PJAIT university.


## Project setup
1. Clone the repo
2. Install venv inside project folder
3. Install dependencies from requirements.txt
4. Create .env file in doctophoto folder with required data. You can refer to .env.example file
5. Create the database using 'python manage.py migrate'

### Database
For this project we used Docker with postgres database. Our settings are available in both
docker-compose and settings.py of Django project.
You can migrate the whole database we used and example data through init_db.bat script you
can find in scripts folder.