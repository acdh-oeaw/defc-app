DEFC-App
=====

About DEFC-App 
--------------

DEFC stands for Digitizing Early Farming Cultures, a project conducted by the [Austrian Academy of
Sciences](http://www.orea.oeaw.ac.at/go-digital.html). The DEFC-App is an application for curating, exploring, and retrieving archaeological datasets.

Install
-------

The DEFC-App is based on [Django 1.8](https://www.djangoproject.com/) and was developed and tested with Python 3.4. 

1. Clone the repository and check out the master branch which holds the latest stable version.
2. Change to the project´s root directory.
3. Create a virtual environment. 
4. Run `pip install -r requirements.txt` to install all required packages.
5. Change directory into `orea/settings/` and adept `dummysettings.py` according to your custom database.
6. Open a terminal, change to the project´s root directory.
7. Run `python manage.py runserver --settings=orea.settings.dummysettings`
8. Open a browser of your choice and enter [http://127.0.0.1:8000/defcdb/](http://127.0.0.1:8000/defcdb/). 
9. If everything worked out, you should see something like on this [demo-page](http://defc.eos.arz.oeaw.ac.at/defcdb/)

Import controlled vocabularies
------------------------------

On of the main assets of the DEFC-App is its carefully curtated controlled vocabulary which helps keeping the different datasets as homogeneous as possible. 

1. more to come....