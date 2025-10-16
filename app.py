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
