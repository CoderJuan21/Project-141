import csv
from flask import Flask, jsonify, request

all_movies = []
with open("articles.csv", encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
liked_articles = []
not_liked_articles = []
app = Flask(__name__)

@app.route("/get-article")
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success",
    })

@app.route("/liked-article",methods=["POST"])
def liked_movie():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    print(all_articles)
    liked_articles.append(movie)
    return jsonify({
        "status":"success",
    }),201

@app.route("/not-liked-article",methods=["POST"])
def unliked_movie():
    movie = all_articles[0]
    all_movies = all_articles[1:]
    all_articles.append(movie)
    return jsonify({
        "status":"success",
    })
    
if __name__ == "__main__":
    app.run()
