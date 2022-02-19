# THE FOOD APP 

## About The Project
### The food App allow users who wants to check the different categories of meal a resturant offers, the application also allows login users to create, update and delete a menu. The first page of the application is called the main home page, the page provide a link in the navbar that allows new user to create a new account and signup, users who already have account will be redirected to the login page. Next Page that comes after the login page is the **Home** page On the home of the application can be found the name the of the food, the image of the food in a square format, the description, the price and the discount price. On the same page can be found the link to the detail page. 

### The detail page include the image, the price, the discount price of a specific menu.The detail page also include both the delete and update buttom. The delete buttom allows login  users to delete the selected food item where as the update buttom allows login users to make changes to either the image,description,price and the discount price. 

## How To Install and Run the Project.
### create a folder on your desktop to server as a container for your project, clone the project into the folder you created.
### Open your command prompt and move to the directoriate of the folder you created for the project. In the commandline install the following packages:   
1. Ensure that you have pipenv install.
1. pipenv install django.
1. pipenv install pillow.

#### After packages has well installed, user can run the commmand: python manage.py runserver. The link below will be displayed in the command prompt:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/).

#### copy and paste  the link in your browser. A welcome page is shown to the user, the welcome page provide a link that requires new users to signup before having a full access to the application. 
#### in the url of the foodapp, which is located in the project, users can see the various links that allows them to create, edit and delete the food item.