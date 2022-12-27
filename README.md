
# Welcome to Flask Starter Kit!

  

Hi! I'm **Shahir Islam** your helper for flask startup kit.

Clone this repo and you are good to go.  


## Summary

- [Dependencies](#Dependencies)
- [Files and Folders](#Files-and-Folders)
- [Before you Start](#Before-you-Start)
- [Installetion](#Installetion)
- [Test](#Test)
- [Good Bye](#Good-Bye)

  
  

# Dependencies

  

-  [Flask](https://palletsprojects.com/p/flask/) : Flask obviously...duh

-  [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/) : SQLAlchemy for Database `SQL-lite`

-  [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) : For serializing API response

-  [PyJwt](https://github.com/jpadilla/pyjwt/) : For encoding JWT user token
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/) : For Password Hashing `sha256`

  

# Files and Folders

  - __pycache__ : This is a default folder you don't need to look at it.
  - **instance** : This folder is for Database
  - **venv** : This folder is for Virtual Enviroment. You just need to activate it. You can delete it if you want.
  - **requirements** : This is a text file and this contains every package you need to install in one place.
  - **app** : This is a python file and this contains our main code. 
  
# Before you Start

--> Use this repo for only backend perpous.  
--> There is no front-end.  
--> This is a starter kit with JWT based auth system.  
--> I used `sql-lite` as database.  
  

> **Note** : You can use **db** as your wish.

  
# Installetion

Make sure you have installed [python](https://www.python.org/downloads/).

**Step 1.** Clone this repo into your local mechine.  
**Step 2.** Open downloaded/cloned folder using any code editor.  
**Step 3.** Activate virtual enviroment. Open terminal and type `./venv/Scripts/Activate.ps1`  
> **Note** : If you have deleted venv folder then you can skip  

**Step 4.** Install all libraries. Open terminal and type `> pip install -r requirements.txt`    

**Step 5.** RUN ! Open terminal and type `> python app.py`  

**Extra**  : If you want to add more tables or columns to the db then type in the terminal    
  ```
    > flask shell 
    > db.create_all() 
  ```  
Here we use `db` for line 16 where we inisialize db as database variable.
 
# Test 

- You need any web response reader software. (Postman, Insomnia, API Tester) I'm using Postman
- After running `> python app.py` you should see an IP:port 
`exm: 127.0.0.1:5000` on your terminal where the app is running. Copy that IP:port and send a `GET` request. If the response is success then you are good to go.
- On `/sign-up , /login` I've used to input data in forms.
- 
### Sign Up `/sign-up`
![Postman Signup](https://res.cloudinary.com/cmb-npi/image/upload/v1672179309/signUp_or3np7.png)

### Login `/login`
![enter image description here](https://res.cloudinary.com/cmb-npi/image/upload/v1672179309/login_jlqyvw.png)

### Use Token  `/home`

Token Key is : `x-access-token`
You will get a token when you login.

![enter image description here](https://res.cloudinary.com/cmb-npi/image/upload/v1672179309/token_rulmp2.png)

> **Note** : Token will expayre after 1 hour you can change this on code line 102. 

# Good Bye

Thanks for visiting my repo. If you are having any problem working with this please tweet me [@lifeofdekisugi](https://twitter.com/lifeofdekisugi).

Fell free to contribute. Don't forget to spread the love 🖤
