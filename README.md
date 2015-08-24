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


Running django app:
1. cd to your django app directory
2. run python manage.py makemigrations
3. run python manage.py migrate
4. run python manage.py createsuperuser
5. run python manage.py runserver


