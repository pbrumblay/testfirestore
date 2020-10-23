from google.cloud import firestore
import time
import json

db = firestore.Client()
recipes_col = db.collection('recipes')

def get_reuse_all(id):
    """ Reuses the client connection and collection reference. """
    doc_ref = recipes_col.document(id)
    return doc_ref.get()

def get_singleton_client_new_collection(id):
    """ Reuses the client connection but fetches the collection reference. """
    c = db.collection('recipes')
    doc_ref = c.document(id)
    return doc_ref.get()

def get_new_client(id):
    """ Resets the client connection and collection reference for each call. """
    new_client = firestore.Client()
    c = new_client.collection('recipes')
    doc_ref = c.document(id)
    return doc_ref.get()

with open('recipes.json', 'r') as json_file:
    c = db.collection('recipes')
    data = json.load(json_file)

    start = time.perf_counter()
    for r in data:
        id = r['Id']
        get_reuse_all(str(id))
    end = time.perf_counter()
    print(f'Reusing the client and collection reference took {end - start} seconds')

    start = time.perf_counter()
    for r in data:
        id = r['Id']
        get_singleton_client_new_collection(str(id))
    end = time.perf_counter()
    print(f'Reusing the client but not the collection refrerence took {end - start} seconds')

    start = time.perf_counter()
    for r in data:
        id = r['Id']
        get_new_client(str(id))
    end = time.perf_counter()
    print(f'Resetting the client took {end - start} seconds')
