travel_log = [
    {"country": "France", "cities": ["Paris", "Lille", "Dijon"], "times": 10},
    {"country": "Germany", "cities": ["Frankfurt", "East Germany", "Berlin"], "times": 5}
]


def add_new_info(country_visited, cities_visited, visited_times):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities"] = cities_visited
    new_country["times"] = visited_times
    travel_log.append(new_country)


visited_country = str(input("Enter the name of the country visited:\n"))
cities_travelled = input("Enter the cities visited separated by ,: \n")
times_visited = int(input("Enter the number of times you visited the country:\n"))

add_new_info(country_visited=visited_country, cities_visited=cities_travelled, visited_times=times_visited)
print(travel_log)