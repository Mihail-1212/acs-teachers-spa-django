# ACS Django application (backend)

This is backend application for ACS (auto-controls system) 
for teachers and students.

Use:
- Django
- Django REST Framework (DRF)
- Authorization applications and modules for DRF
- DRF swagger (drf-yasg)

Application structure:

    .
    ├── acs_teacher_backend         # Application src directory
    │   ├── apps                        # Directory with all django apps inside
    │   ├── settings.py                 # Project settings file
    │   ├── urls.py                     # Project file with main routes
    ├── assets (auto generate)      # Auto generated directory for compile static files
    ├── docs (empty)                # Directory for documentation
    ├── media (auto generate)       # Auto generated directory for user files
    ├── static (auto generate)      # Auto generated directory for static files
    ├── .env                        # File within environment variables
    ├── LICENSE                     # License file
    ├── manage.py                   # Main django file
    ├── requirements.txt            # Text requirements file within pip freeze modules
    └── README.md                   
