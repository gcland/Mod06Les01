import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

#fetch_planet_data()

def longest_oribital_period():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    oribtial_period_dict = {}
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            orbit_period = planet['sideralOrbit']
            oribtial_period_dict[name] = orbit_period

    print(oribtial_period_dict)
    v = list(oribtial_period_dict.values())
    k = list(oribtial_period_dict.keys())
    planet_max_period = k[v.index(max(v))]
    print(f"Planet with max oritbial period: {planet_max_period}.\nOribital period: {max(v)}")
    

    

longest_oribital_period()
        