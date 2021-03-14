# doctophoto
Web application, built with Django, that allows doctor to send radiography images with description to his patients.
It was a group project for PRO course at PJAIT university.

# Features
* Login and registration
* Doctors can create "descriptions" of radiography photos
* Patients can view their descriptions and radiography photos
* Various data is hidden from users who aren't supposed to see it (e.g. an patient can't see someone's else description)

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
