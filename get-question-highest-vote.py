import requests

# Set the API endpoint and parameters
api = 'https://api.stackexchange.com/2.3/questions'

def get_highest_vote():
    params = {
        'order': 'desc',
        'sort': 'votes',
        'site': 'stackoverflow'
    }
    # Make the API request
    response = requests.get(api, params=params)
    # Get the JSON data from the response
    data = response.json()
    # Print the titles and scores of the top 10 questions
    for i, item in enumerate(data['items'][:10]):
        print(f"{i+1}. {item['title']} {item['score']}")
get_highest_vote()