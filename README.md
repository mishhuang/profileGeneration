# profileGeneration
The Cat Profile Microservice is a simple REST API built using Flask, which provides JSON-formatted data containing randomized cat profiles. The profiles include information such as name, age, coloring, personality, coat, toy, likes, and dislikes.

## Requirements
Before you are able to run the microservice and make requests, you need to have the following installed:
Python (version 3.6 or higher)
Flask (installed via pip install flask)
Requests (installed via pip install requests)

## Running the Microservice
Save the provided microservice code in a Python file.
Open your terminal.
Navigate to the directory where you saved the microservice python file.
Run the microservice using the following command: python {microserviceName}.py
This will start the microservice as a Flask application and will be available to receive requests at the URL: http://127.0.0.1:5000/catprofile

## Programmatically Request Data from the Microservice
You can use the Python requests library, which can be installed using the following command in your terminal: pip install requests.

#### Here's an example of how to make a request and receive the data:
import requests

url = 'http://127.0.0.1:5000/catprofile'

response = requests.get(url)

if response.status_code == 200:
    cat_profiles = response.json()
    print("Cat Profiles:")
    print(cat_profiles)
else:
    print("Error:", response.status_code)

## Programmatically Receive Data from the Microservice
When you make a request to the microservice using an HTTP client, you will receive a JSON response containing three randomized cat profiles. These profiles are currently randomly generated from static source code. The response will look like this:
[
    {
        "age": 5,
        "coat": "medium hair",
        "coloring": "orange",
        "dislike": "loud noises",
        "like": "brushing",
        "name": "Runner",
        "personality": "aloof",
        "toy": "flying"
    },
    {
        "age": 13,
        "coat": "medium hair",
        "coloring": "calico",
        "dislike": "getting wet",
        "like": "catnip",
        "name": "Jolly",
        "personality": "aloof",
        "toy": "squeky"
    },
    {
        "age": 7,
        "coat": "long hair",
        "coloring": "orange",
        "dislike": "loud noises",
        "like": "playtime",
        "name": "Floofy",
        "personality": "shy",
        "toy": "squeky"
    }
]

This json file can be programmatically processed as needed in your application.
