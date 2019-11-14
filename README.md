QUIZ APP    


INTRODUCTION - THE PROJECT AIM                                    

The project aim is create our first webside where user can test his knowledge with many different quizzes or create his own quiz. 
User can also add comments and scores under each quiz.


TECHNOLOGIES

Django, Postgresql


LAUNCH
                                    
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


SCOPE OF FUNCIONALITIES

- Creating new user
- Adding a new quiz
- Comment existed quizzes
- Solving existing quizzes
- Sorting quizzes (genre, popularity, recently added)


OTHER INFORMATION
                                                                                  
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



