import requests

def get_planet_info():
    url = "https://swapi.dev/api/planets/"
    params = {"search": "Tatooine"}

    response = requests.get(url, params=params)
    data = response.json()

    if data["count"] == 0:
        print("Planet not found.")
        return

    planet = data["results"][0]
    print(f"Name: {planet['name']}")
    print(f"Climate: {planet['climate']}")
    print(f"Terrain: {planet['terrain']}")
    print(f"Population: {planet['population']}")

get_planet_info()