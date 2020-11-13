cities = ['Nairobi', 'Nakuru', 'Bungoma', 'Kakamega']


cities_filterd = filter(lambda city: city.startswith("N"), cities)
print(list(cities_filterd))
