# Student Management System (AAI LAB - CCA1)

This repository contains a starter Django project for the Student Management System assignment with a students app that implements full CRUD for a Student model.

Repository layout (added by the assistant):

- aai_lab_project/ - Django project settings and URLs
- students/ - Django app with models, views, URLs and templates
- Project_PDFs/ - folder to place project PDF reports (empty placeholder)
- jokes/ and joke-generator/ may exist from an earlier step; they are not integrated into the Django project by default.

Quick start

1. Create and activate a virtual environment:

   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate

2. Install dependencies:

   pip install -r requirements.txt

3. Run migrations and create a superuser:

   python manage.py migrate
   python manage.py createsuperuser

4. Start the development server:

   python manage.py runserver

5. Open http://localhost:8000 to see the students list.

Add your project PDF

- Upload your project PDF into Project_PDFs/ and commit it to the repository.

If you want me to also remove the jokes files or wire the jokes app into the project, tell me and I will update settings.py and urls.py accordingly.
