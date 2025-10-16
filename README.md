

![invincible-u17h0jg0nw7lhrgc](https://github.com/user-attachments/assets/286702c4-9fd3-4f20-a597-a153e68045aa)
Invincible API

This project is inspired by my love for ***Invincible***, one of my all-time favorite superhero shows.
It’s a simple **Flask-RESTful API** that serves character information from the *Invincible* universe — including their names, aliases, estimated ages, locations, power levels, abilities, and image URLs.

---

## 🚀 Project Overview

This version of the API does **not** use a database.
Instead, it reads data from a local **JSON file**, making it lightweight, fast, and easy to run anywhere.

The project is organized into three main parts:

1. **`data/`** – contains the `characters.json` file with all character information
2. **`resources/`** – contains Flask-RESTful resource classes that define API endpoints and logic
3. **`app.py`** – the main entry point that initializes and runs the Flask API

---

## 🧱 Project Structure

```
invincible_api/
│
├── app.py
├── data/
│   └── characters.json
├── resources/
│   └── characters.py
├── static/
│   └── images/
│       ├── invincible.jpg
│       ├── omni-man.jpg
│       └── atom-eve.jpg
├── requirements.txt
└── README.md
```

📸 *Project structure on my computer:* <img width="658" height="445" alt="code structure" src="https://github.com/user-attachments/assets/459791f7-0873-42af-acea-2354af8af06d" />

---

## 💻 Code Overview

### `app.py`

```python
from flask import Flask
from flask_restful import Api
from resources.characters import CharacterList, CharacterResource

app = Flask(__name__)
api = Api(app)

# API routes
api.add_resource(CharacterList, '/api/v1/characters')
api.add_resource(CharacterResource, '/api/v1/characters/<int:character_id>')

if __name__ == '__main__':
    app.run(debug=True)
```

### `resources/characters.py`

```python
from flask_restful import Resource
import json

with open("data/characters.json", "r") as f:
    CHARACTERS = json.load(f)

class CharacterList(Resource):
    def get(self):
        """Return all characters"""
        return {"characters": CHARACTERS}, 200

class CharacterResource(Resource):
    def get(self, character_id):
        """Return a single character by ID"""
        character = next((c for c in CHARACTERS if c["id"] == character_id), None)
        if character:
            return character, 200
        return {"message": "Character not found"}, 404
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/invincible-api.git
cd invincible-api
```

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000
```

📸 *Testing the API in Postman:* <img width="643" height="242" alt="testing the api in postman" src="https://github.com/user-attachments/assets/46e5c5a3-a539-4d91-853d-33ade441301c" />

---

## 🧠 API Endpoints

### 🔹 Get All Characters

**Endpoint:**

```
GET /api/v1/characters
```

**Response Example:**

```json
{
  "characters": [
    {
      "id": 1,
      "name": "Mark Grayson",
      "alias": "Invincible",
      "age": 18,
      "location": "Earth",
      "power_level": 9000,
      "abilities": ["Super strength", "Flight", "Enhanced durability"],
      "image_url": "/static/images/invincible.jpg"
    }
  ]
}
```

📸 *Response Example:* <img width="647" height="439" alt="the api with the reponse" src="https://github.com/user-attachments/assets/473594b1-b098-406a-8441-4d89067089ea" />

---

### 🔹 Get a Single Character

**Endpoint:**

```
GET /api/v1/characters/<id>
```

**Example:**

```
GET /api/v1/characters/2
```

**Response Example:**

```json
{
  "id": 2,
  "name": "Omni-Man",
  "alias": "Nolan Grayson",
  "age": 45,
  "location": "Viltrum / Earth",
  "power_level": 12000,
  "abilities": ["Super strength", "Flight", "Immortality"],
  "image_url": "/static/images/omni-man.jpg"
}
```

---

## 🖼️ Static Files

Character images are stored under the `/static/images/` directory.
You can access them directly through your browser, for example:

```
http://127.0.0.1:5000/static/images/invincible.jpg
```

---

## ☁️ Hosting

The project is fully compatible with **PythonAnywhere** and other Flask-friendly hosting platforms.

To deploy:

1. Upload your project folder to your PythonAnywhere account.
2. Create and activate a virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Edit your WSGI file to import your `app`.
5. Reload the web app from the PythonAnywhere dashboard.

Once deployed, your live API will look like:

```
https://<your-username>.pythonanywhere.com/api/v1/characters
```

---

## 🧩 Technologies Used

* **Python 3**
* **Flask**
* **Flask-RESTful**
* **JSON** for lightweight data storage

---

## 💡 Future Improvements

* Integrate a real database (SQLite/MySQL/PostgreSQL)
* Implement search and filtering
* Add more characters and media assets
* Include Swagger or Postman API documentation
* Add pagination and caching for scalability

---
Perfect 🔥 Cephas — here’s a **GitHub-ready, polished, human-sounding** section that blends naturally with the tone you’ve been using in your Invincible API project README.

You can paste it **directly under** your main description section (e.g. after “About the Project” or “How It Works”).

---

## 🌍 Hosting on PythonAnywhere

This API is hosted live on **[PythonAnywhere](https://www.pythonanywhere.com/)** — a simple and free way to run Python web apps online.
Below are the exact steps I followed to get it running publicly so anyone can access the data and images.

---

### 🧭 1. Create a PythonAnywhere Account

* Go to [pythonanywhere.com](https://www.pythonanywhere.com/) and create a free account.
* Once signed in, open your **Dashboard**.

---

### 💻 2. Clone the Project

From your dashboard, open a **Bash console** and run:

```bash
git clone https://github.com/<your-username>/invincible_api.git
cd invincible_api
```

This downloads the repository to your PythonAnywhere home directory.

---

### ⚙️ 3. Install Dependencies

Install all required libraries in your environment:

```bash
pip install --user -r requirements.txt
```

This ensures Flask, Flask-RESTful, and any other packages are available.

---

### 🌐 4. Create a New Web App

1. Go to the **Web** tab on PythonAnywhere.
2. Click **“Add a new web app.”**
3. Choose **Manual configuration (Flask)** → select **Python 3.10**.
4. After creation, note the path shown — something like:

   ```
   /var/www/cephasokuku_pythonanywhere_com_wsgi.py
   ```

---

### 🧩 5. Configure the WSGI File

* Open the file mentioned above.
* Replace the Flask section with the following code:

```python
import os
import sys

# Path to your project
project_home = '/home/cephasokuku/invincible_api'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.chdir(project_home)

# Import the Flask app
from app import app as application
```

Click **Save** when done.

---

### 🧱 6. Set Up Static Files

This allows your hosted API to serve images (and any other static files).

In the **Web** tab → scroll down to **Static files**, then click **“Add a new static file mapping.”**

| URL        | Directory                                 |
| ---------- | ----------------------------------------- |
| `/static/` | `/home/cephasokuku/invincible_api/static` |

Click **Save**, then **Reload your web app**.

---

### 🚀 7. Test the API

Visit your hosted URL:

```
https://cephasokuku.pythonanywhere.com/
```

If everything is set up correctly, you’ll see:

```json
{"message": "Welcome to Invincible API"}
```

You can now view data endpoints like:

```
https://cephasokuku.pythonanywhere.com/api/characters
```

and access images directly:

```
https://cephasokuku.pythonanywhere.com/static/images/invincible.png
```

---

### 🔁 8. Updating the App

Whenever you make changes locally and push them to GitHub, pull the updates into PythonAnywhere:

```bash
cd ~/invincible_api
git pull
```

Then **Reload** the web app from the Web tab.

---

### ✅ That’s It!

Your **Invincible API** is now fully deployed online — serving character data, images, and all the glory of your favorite show 💪🦸‍♂️

---

Would you like me to add a short **“Live Demo”** badge and link snippet (e.g. `[Live API](https://cephasokuku.pythonanywhere.com/)`) that you can place at the top of your README?

## ❤️ Credits

Created by **Cephas Okuku**
A tribute to the *Invincible* universe and its incredible storytelling.


