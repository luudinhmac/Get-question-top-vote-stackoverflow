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
# Print the topic and the titles, scores, and links of the top N questions
    print(f"Top results for '{topic}':\n")
    # The enumerate() function is used to get both the index and the value of each item.
    for i, item in enumerate(data['items'][:number]):
        print(f"{i+1}. {item['title']} ({item['score']})\n{item['link']}\n")


if __name__ == '__main__':
    # sets up an argument parser using argparse, allows the user to pass in the number and topic arguments from the command line.
    parser = argparse.ArgumentParser(description='Process some data')
    parser.add_argument('number', type=int, help='Number question to process')
    parser.add_argument('topic', help='tags of questions')
    args = parser.parse_args()
    vote_highest_stackoverflow(args.number, args.topic)
