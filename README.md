  ,ad8888ba,    88        88  88  888888888888             db         88888888ba   88888888ba 
 d8"'    `"8b   88        88  88           ,88            d88b        88      "8b  88      "8b
d8'        `8b  88        88  88         ,88"            d8'`8b       88      ,8P  88      ,8P
88          88  88        88  88       ,88"             d8'  `8b      88aaaaaa8P'  88aaaaaa8P'
88          88  88        88  88     ,88"              d8YaaaaY8b     88""""""'    88""""""'  
Y8,    "88,,8P  88        88  88   ,88"               d8""""""""8b    88           88         
 Y8a.    Y88P   Y8a.    .a8P  88  88"                d8'        `8b   88           88         
  `"Y8888Y"Y8a   `"Y8888Y"'   88  888888888888      d8'          `8b  88           88         




  ___       _                 _            _   _            
 |_ _|_ __ | |_ _ __ ___   __| |_   _  ___| |_(_) ___  _ __  
  | || '_ \| __| '__/ _ \ / _` | | | |/ __| __| |/ _ \| '_ \ 
  | || | | | |_| | | (_) | (_| | |_| | (__| |_| | (_) | | | |
 |___|_| |_|\__|_|  \___/ \__,_|\__,_|\___|\__|_|\___/|_| |_|                                

The project aim is create our first webside where user can test his knowledge with many different quizzes or create his own quiz. 
User can also add comments and scores under each quiz.

  _____         _                 _             _           
 |_   _|__  ___| |__  _ __   ___ | | ___   __ _(_) ___  ___ 
   | |/ _ \/ __| '_ \| '_ \ / _ \| |/ _ \ / _` | |/ _ \/ __|
   | |  __/ (__| | | | | | | (_) | | (_) | (_| | |  __/\__ \
   |_|\___|\___|_| |_|_| |_|\___/|_|\___/ \__, |_|\___||___/
                                          |___/             
Django, Postgresql



  _                           _     
 | |    __ _ _   _ _ __   ___| |__  
 | |   / _` | | | | '_ \ / __| '_ \ 
 | |__| (_| | |_| | | | | (__| | | |
 |_____\__,_|\__,_|_| |_|\___|_| |_|
                                    

- First you need Git, Python (>= 3.6) with Virtualenv and Pip installed. 
If you are under Linux/Mac this should be a no-brainer, if you use Windows and you don't have a Git, Python, Virtualenv and Pip workflow yet, please read this tutorial
http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/

for Pip and Virtualenv installation/usage and visit this link
https://git-scm.com/download/win

to download/install Git.

- If not already downloaded/installed, download/install Git, Python (>= 3.6), Pip (normally comes with Python) and Virtualenv

- Open the console (aka terminal, shell) on your computer

- Create a project directory in your terminal:

mkdir -p path/to/projectfolder

- CD into your project directory:

cd path/to/projectfolder

- Create a virtual environment with Virtualenv:

virtualenv venv --python=python3.6

- Activate the virtual environment:

source venv/bin/activate

- Clone the repository to your local machine:

git clone https://github.com/zjask119/quizapp/

- Install the requirements:

pip install -r requirements.txt

Create the database:
python manage.py migrate

Finally, run the development server:
python manage.py runserver

The project will be available at 127.0.0.1:8000.



  ____                                __    __                  _   _                   _ _ _   _           
 / ___|  ___ ___  _ __   ___    ___  / _|  / _|_   _ _ __   ___| |_(_) ___  _ __   __ _| (_) |_(_) ___  ___ 
 \___ \ / __/ _ \| '_ \ / _ \  / _ \| |_  | |_| | | | '_ \ / __| __| |/ _ \| '_ \ / _` | | | __| |/ _ \/ __|
  ___) | (_| (_) | |_) |  __/ | (_) |  _| |  _| |_| | | | | (__| |_| | (_) | | | | (_| | | | |_| |  __/\__ \
 |____/ \___\___/| .__/ \___|  \___/|_|   |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|\__,_|_|_|\__|_|\___||___/
                 |_|                                                                                        
- Creating new user
- Adding a new quiz
- Comment existed quizzes
- Solving existing quizzes
- Sorting quizzes (genre, popularity, recently added)


   ___  _   _                 _        __                            _   _             
  / _ \| |_| |__   ___ _ __  (_)_ __  / _| ___  _ __ _ __ ___   __ _| |_(_) ___  _ __  
 | | | | __| '_ \ / _ \ '__| | | '_ \| |_ / _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
 | |_| | |_| | | |  __/ |    | | | | |  _| (_) | |  | | | | | | (_| | |_| | (_) | | | |
  \___/ \__|_| |_|\___|_|    |_|_| |_|_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|
                                                                                       

A Complete Beginner's Guide to Django
https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/

Read the official documentation (its worth it)!
https://docs.djangoproject.com/en/2.1/

Do the official get started tutorial
https://docs.djangoproject.com/en/2.1/intro/

Two other, very good tutorials: 
write a blog system (videos)
https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

write a simple geo app (with GeoDjango)
https://realpython.com/location-based-app-with-geodjango-tutorial/

Django design philosophies
https://docs.djangoproject.com/en/2.1/misc/design-philosophies/



