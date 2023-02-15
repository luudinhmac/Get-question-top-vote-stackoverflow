import requests
import argparse

def vote_highest_stackoverflow(number, topic):

    # Set the API endpoint and parameters
    api = 'https://api.stackexchange.com/2.3/questions'
    params = {
        'order': 'desc',
        'sort': 'votes',
        'tagged': topic,
        'site': 'stackoverflow'
    }
# Make the API request
    response = requests.get(api, params=params)
# Get the JSON data from the response
    data = response.json()
# Print the titles, scores, and links of the top number questions
    print(f"Top results for '{topic}':\n")
    for i, item in enumerate(data['items'][:number]):
        print(f"{i+1}. {item['title']} ({item['score']})\n{item['link']}\n")
if __name__ == '__main__':
    # Prompt the user to enter a topic
    topic = input('Enter a search topic: ')
    # user enter number of results
    number = int(input("Enter number to search on Stack Overflow: "))

    vote_highest_stackoverflow(number, topic)
