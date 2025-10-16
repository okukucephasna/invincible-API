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
