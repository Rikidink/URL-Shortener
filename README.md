﻿# Rickly: URL Shortener
Simple URL shortener developed with Flask backend using Tailwind CSS for styling.
URLs stored in a PostgreSQL database and is interfaced using SQLAlchemy.  
Very early stages of development right now with plans to implement more features and refinements with a better user interface.  

---

## Prerequisites
Requires a PostgreSQL database (you can use other databases but PostgreSQL is preferred for seamless integration).

## Setup | Try it out!

1. Clone the repository
2. Create a virtual environment within the flask directory and activate:

```console
python -m venv env  
env/Scripts/activate
```

3. Install dependencies/requirements using pip:  

```console
(venv) pip install -r requirements.txt
```

4. In the flask folder, create a config.py file which contains your db connection string (replace username, password, and database with your respective names):  

```python
DB_CONNECTION_STRING = 'postgresql://username:password@localhost:5432/database'
```

5. Run the app:  

```console
(venv) flask run
```

6. Go to http://127.0.0.1:5000 to try it out.  

---  

## Future plans/ideas/refinements:
 
- ~~Use a front-end framework (probably React)~~ (don't really need one, just using Tailwind for CSS now)
- ~~Implement QR codes for shortened URLs~~
- ~~Deploy the project somewhere~~ (deployed on AWS currently, but probably will change)
- ~~Use an actual database for storage of URLs (probably PostgreSQL)~~
- ~~Add the about and contact pages~~
- Use regex for better URL validation
- Might have to fix copy to clipboard for mobile
- Make common classes for buttons and stuff in tailwind
- Have a counter for amount of times a URL is visited
- Improve overall UI/UX
  - ~~Support for small screens/mobile (i.e: hamburger menu)~~
  - Dark mode button (obviously not necessary I just think its cool)
  - ~~Fix qrcode border~~ (and make the qrcode cooler: maybe allow users to customise qrcode?)
  - Ability to expand qrcode when button is pressed
  - Have a nice animated background for the page (maybe gradient?)
  - Display shortened URLs in a list instead of one at a time
  - Add success/fail messages for input and copy to clipboard
  - File name for qrcode image should be destination URL

 **Credits/References:**  
 Background animation by a [user on TailwindFlex](https://tailwindflex.com/@anonymous/background-animation)

