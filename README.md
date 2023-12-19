﻿# Flask URL-Shortener
Simple URL shortener developed with Flask.  
Very early stages of development right now with plans to implement more features and refinements with a better user interface.  

---

**Try it out (idk why you would though):**  
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

4. Run the app:  

```console
(venv) flask run
```

5. Go to http://127.0.0.1:5000 to try it out.  

---  

**Future plans for features/refinements:**  
- Use a front-end framework (probably React)
- Implement QR codes for shortened URLs
- Use an actual database for storage of URLs (probably PostgreSQL)
- Deploy the project somewhere
