travel_log = [
    {"country": "France", 
     "cities": ["Paris", "Lille", "Dijon:"], 
     "visits": 12},
    {"country":"Germany", 
     "cities": ["Berlin", "Hamburg", "Stuttgart:"], 
     "visits": 5}
]
def add_new_country(country, cities, visits):
    travel_log.append({"country": country, 
                       "cities": cities, 
                       "visits": visits
                       })
    
add_new_country("Russia", ["Moscow", "Saint Petersburg",  "Novosibirsk"], 2)
print(travel_log)