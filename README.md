# 🦸‍♂️ Invincible API

This project is inspired by my love for ***Invincible***, one of my all-time favorite superhero shows.
It’s a simple **Flask-RESTful API** that serves character information from the *Invincible* universe — including their names, aliases, estimated ages, locations, power levels, abilities, and image URLs.

## 🚀 Project Overview

This version of the API does not use a database.
Instead, it reads data from a local JSON file, making it lightweight and easy to run anywhere.

The project is structured into three main parts:

1. **`data/`** – contains the `characters.json` file with all character information
2. **`resources/`** – contains Flask-RESTful resource classes that define API endpoints and logic
3. **`app.py`** – the main entry point that initializes and runs the Flask API

---

## 🧱 Project Structure
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

An image of how the project structure looks like on my computer
<img width="658" height="445" alt="code structure" src="https://github.com/user-attachments/assets/459791f7-0873-42af-acea-2354af8af06d" />

Code for the different sections
Code for app.py
# app.py
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
Code for characters.py
# resources/characters.py
from flask_restful import Resource
import json
from flask import request

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


## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/invincible-api.git
cd invincible-api
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000
```

Testing the API in postman
<img width="643" height="242" alt="testing the api in postman" src="https://github.com/user-attachments/assets/46e5c5a3-a539-4d91-853d-33ade441301c" />


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
An image of the response

<img width="647" height="439" alt="the api with the reponse" src="https://github.com/user-attachments/assets/473594b1-b098-406a-8441-4d89067089ea" />

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

For deployment:

* Upload your project folder
* Install dependencies via a virtual environment
* Configure the WSGI file to import your `app`
* Reload the web app from the PythonAnywhere dashboard

---

## 🧩 Technologies Used

* **Python 3**
* **Flask**
* **Flask-RESTful**
* **JSON** for lightweight data storage

---

## 💡 Future Improvements

* Add database integration (SQLite/MySQL/PostgreSQL)
* Implement search and filtering
* Add more characters and images
* Include Swagger or Postman API documentation
* Introduce caching and pagination for scalability

---

## ❤️ Credits

Created by **Cephas Okuku**
A tribute to the *Invincible* universe and its incredible storytelling.

---

Would you like me to add a short **section with a live demo link and deployment instructions for PythonAnywhere** at the bottom (once you deploy it)?
That way, people visiting your GitHub can directly test your API online.
