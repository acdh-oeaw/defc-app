Cloning repository

1. Choose the directory where you want to create repository, right click and select 'Git Clone', in the Git window copy your https repository access link and click OK
2. Right click (in the directory of just cloned repository) and select 'TortoiseGit', select 'Switch/Checkout' and choose the branch.

Creating virtual environment

1. cd to Redmine\defc-webapp
2. Create an virtual enviroment with the command: 
$ conda create --name freename python=3.4
3. To activate this environment, use
>activate freename

Installing packages
1. pip install -r requirements.txt



Running django app:
1. cd to your django app directory --settings=PROJECTNAME.settings.local OR server OR db_sqlLite
2. run python manage.py makemigrations --settings=PROJECTNAME.settings.local OR server OR db_sqlLite
3. run python manage.py migrate --settings=PROJECTNAME.settings.local OR server OR db_sqlLite
4. run python manage.py createsuperuser --settings=PROJECTNAME.settings.local OR server OR db_sqlLite
5. run python manage.py runserver --settings=PROJECTNAME.settings.local OR server OR db_sqlLite


