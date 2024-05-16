import requests

# Define the base URL of the Star Wars API
base_url = "https://swapi.dev/api/"

# Define the endpoint you want to access (e.g., "films" for movies)
endpoint = "films"

# Send a GET request to the API
response = requests.get(f"{base_url}{endpoint}")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()

    # Print the titles of the Star Wars movies
    for movie in data["results"]:
        print(movie["title"])
else:
    print("Failed to retrieve data from the Star Wars API.")