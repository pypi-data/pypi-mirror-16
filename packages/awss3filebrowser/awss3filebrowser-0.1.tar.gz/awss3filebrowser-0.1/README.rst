=====
awss3browser
=====

awss3browser is a simple Django app to browser AWS S3 BUCKET.
You can create folder, delete folder and files, rename,upload file and get details .
Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "awss3browser" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'awss3browser',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^filebrowser/', include('awss3browser.urls')),

3. ADD SETTINGS to settings.py

AWS_ACCESS_KEY_ID = 'YOUR_AWS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY'
AWS_STORAGE_BUCKET_NAME = 'YOUR_AWS_STORAGE_BUCKET_NAME'
AWS_STORAGE_BUCKET_ROOT_FOLDER = 'YOUR_AWS_STORAGE_BUCKET_ROOT_FOLDER' // for example AWS_STORAGE_BUCKET_ROOT_FOLDER = 'public' is the root folder of my s3 bucket


4. Visit 'http://127.0.0.1:8000/filebrowser/files/' to see the filelist.