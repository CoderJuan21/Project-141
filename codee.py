import csv
from flask import Flask, jsonify, request
from DemographicFiltering import output
from content_filtering import get_recomendations
from storage import liked_articles, not_liked_articles, all_articles
app = Flask(__name__)

@app.route("/get-article")
def get_movie():
    return jsonify({
        "data":all_articles[0],
        "status":"success",
    })

@app.route("/liked-article",methods=["POST"])
def liked_movie():
    article = all_articles[0]
    all_articles = all_articles[1:]
    print(all_articles)
    liked_articles.append(article)
    return jsonify({
        "status":"success",
    }),201

@app.route("/not-liked-article",methods=["POST"])
def unliked_article():
    article = all_articles[0]
    all_movies = all_articles[1:]
    all_articles.append(article)
    return jsonify({
        "status":"success",
    })

@app.route("/popular-article")
def popular_articles():
    movie_data = []
    for article in output:
        _d = {
           "url":article[0],
           "title":article[1],
           "text":article[2],
           "lang":article[3],
           "total_events":article[4]
        }
        movie_data.append(_d)
    return jsonify({
        "data":movie_data,
        "status":"success",
    })

@app.route("/recommended-article")
def recommended_articles():
    all_recommended = []
    for liked_movie in liked_articles:
        output = get_recomendations(liked_movie[19])
        for data in output:
            all_recommended.append(data)
    import itertools 
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended, _ in itertools.groupby(all_recommended))
    movie_data = []
    for recommended in all_recommended:
        _d = {
           "url":recommended[0],
           "title":recommended[1],
           "text":recommended[2],
           "lang":recommended[3],
           "total_events":recommended[4]
        }
        movie_data.append(_d)
    return jsonify({
        "data":movie_data,
        "status":"success",
    })
    
if __name__ == "__main__":
    app.run()
