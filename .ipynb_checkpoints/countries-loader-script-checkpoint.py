import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['countries']
collection_country = db['country']

with open('countries.json') as f:
    countries_json = json.load(f)
    
for country in countries_json:
    country_to_save = { "_id" : country['cca3'], "cca3" : country['cca3'] , "borders" :country['borders'] , "region" : country['region']}
    collection_country.insert_one(country_to_save)