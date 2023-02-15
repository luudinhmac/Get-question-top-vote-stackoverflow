from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search', methods=['POST'])
def search():
    topic = request.form['topic']
    number = request.form['number']
    api = 'https://api.stackexchange.com/2.3/questions'
    params = {
        'order': 'desc',
        'sort': 'votes',
        'tagged': topic,
        'site': 'stackoverflow'
    }
    response = requests.get(api, params=params)
    data = response.json()
    results = []
    for i, item in enumerate(data['items'][:int(number)]):
        result = {
            'title': item['title'],
            'score': item['score'],
            'link': item['link']
        }
        results.append(result)
    return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run()
