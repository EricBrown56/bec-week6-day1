import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    #print(planets)

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            index = planets.index(planet) #get index of planet
            name = planets[index]["englishName"] #get planet English name
            mass = planets[index]["mass"]["massValue"] #get planet mass
            orbit_period = planets[index]["sideralOrbit"] #get planet orbit period
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
            

fetch_planet_data()

print("=" * 50)

def fetch_planet_info():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies'] # Enhance format the output in a more readable manner
    planet_info = []
    for planet in planets:
        if planet['isPlanet']:
            index = planets.index(planet)
            name = planets[index]["englishName"]
            mass = planets[index]["mass"]["massValue"]
            planet_info.append([name, str(mass)]) #list of planets
    return planet_info
        

def find_heaviest_planet(planets):
    #print(planets)
    heaviest_planet = max(planets, key=lambda x: x[1])
    #print(heaviest_planet)
    print(f"The heaviest planet is {heaviest_planet[0]} with a mass of {heaviest_planet[1]} kg")

#name, mass = find_heaviest_planet(planets)
planets = fetch_planet_info()
find_heaviest_planet(planets)