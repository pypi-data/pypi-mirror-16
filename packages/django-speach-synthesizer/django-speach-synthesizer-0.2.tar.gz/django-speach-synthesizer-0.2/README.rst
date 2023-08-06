=====
Django Speach Synthesizer
=====

Django Speach Synthesizer is a simple Django app to create .wav files from your text

Must be installed RHVoice-test utilite on Unix Machine

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add some apps  to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rest_framework_swagger',
        'rest_framework',
        'django_speach_synthesizer',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^syntha/', include('django_speach_synthesizer.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/docs/
   to see docs and available api