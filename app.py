from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import sys

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'newdb'
app.config["MONGO_URI"] = "mongodb://localhost:27017/newdb"
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
mongo = PyMongo(app)


@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = mongo.db.movies 

    output = []

    for q in movies.find():
        output.append({
        'uuid' : q['_id'], 
        'chi_name' : q['chi_name'],
        "eng_name" : q["eng_name"],
        "chi_genre" : q["chi_genre"],
        "eng_genre" : q["eng_genre"],
        "chi_director" : q["chi_director"],
        "eng_director" : q["eng_director"],
        "chi_cast" : q["chi_cast"],
        "eng_cast" : q["eng_cast"],
        "open_date" : q["open_date"],
        "thumbnail" : q["thumbnail"],
        "chi_synopsis" : q["chi_synopsis"],
        "eng_synopsis" : q["eng_synopsis"],
        "category" : q["category"],
        "duration" : q["duration"],
        })
    
    

    return jsonify(output)

@app.route('/movieDetail', methods=['GET'])
def get_one_movie():
    movie = mongo.db.movies
    q = movie.find_one({'_id' : request.args.get('uuid')})
    
    if q:
        output = {
        'uuid' : q['_id'], 
        'chi_name' : q['chi_name'],
        "eng_name" : q["eng_name"],
        "chi_genre" : q["chi_genre"],
        "eng_genre" : q["eng_genre"],
        "chi_director" : q["chi_director"],
        "eng_director" : q["eng_director"],
        "chi_cast" : q["chi_cast"],
        "eng_cast" : q["eng_cast"],
        "open_date" : q["open_date"],
        "thumbnail" : q["thumbnail"],
        "chi_synopsis" : q["chi_synopsis"],
        "eng_synopsis" : q["eng_synopsis"],
        "category" : q["category"],
        "duration" : q["duration"],
        }
    else:
        output = 'No results found'

    return jsonify( output)
    



if __name__ == "__main__":
  app.run()