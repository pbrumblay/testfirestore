import json
from google.cloud import firestore

db = firestore.Client()

with open('recipes.json', 'r') as json_file:
    c = db.collection('recipes')
    data = json.load(json_file)
    for r in data:
        id = r.pop('Id', None)
        c.add(r, str(id))
