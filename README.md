Cloning repository

1. Choose the directory where you want to create repository, right click and select 'Git Clone', in the Git window copy your https repository access link and click OK
2. Right click (in the directory of just cloned repository) and select 'TortoiseGit', select 'Switch/Checkout' and choose the branch.

Creating virtual environment

1. cd to Redmine\defc-webapp
2. Create an virtual enviroment with the command: 
$ conda create --name python27 python=2.7
3. To activate this environment, use
>activate python27

Installing crispy forms
1. pip install django-crispy-forms==1.3.0

  *ToDo change README.me according to use the requirements.txt


Running django app:
1. cd to your django app directory --settings=PROJECTNAME.settings.local OR server OR db_sqlLite
2. run python manage.py makemigrations --settings=PROJECTNAME.settings.local OR server OR db_sqlLite
3. run python manage.py migrate --settings=PROJECTNAME.settings.local OR server OR db_sqlLite
4. run python manage.py createsuperuser --settings=PROJECTNAME.settings.local OR server OR db_sqlLite
5. run python manage.py runserver --settings=PROJECTNAME.settings.local OR server OR db_sqlLite


