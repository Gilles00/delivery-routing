import requests as r

API_KEY = "AIzaSyBXkHh19xkywMvwd4iFXMLjS70TWv6LOaU"

base_url = "https://www.google.com/maps/?api=1&"

query_url = "https://www.google.com/maps/search/?api=1"

origin = input("which origin?").replace(" ", '+').replace(",", '%2C')

destination = input("which destination?").replace(" ", "+").replace(",", '%2C')

origin_query = query_url + "&key=" + str(API_KEY) + "&query=" + str(origin)

dest_query = query_url + "&key=" + str(API_KEY) + "&query=" + str(destination)

origin_results = r.get(origin_query)

dest_results = r.get(dest_query)

print("Origin Results are:", origin_results)

print("Destination Resuts are:", dest_results)





#class Map:
#    def __init__(self):
