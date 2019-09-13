from flask import Flask, render_template
from data import articles

app = Flask(__name__)

lst_articles = articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def all_articles():
    return render_template('articles.html', articles = lst_articles)

@app.route('/article/<string:id>')
def get_article(id):
    return render_template('article.html', id = id)

if __name__ == '__main__':
    app.run(debug=True)