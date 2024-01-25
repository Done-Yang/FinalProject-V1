"""
Find ip address by host name
"""
# import socket

# # Get the host name from the user
# host_name = input("Enter the host name: ")

# Get the IP address of the host name
# ip_address = socket.gethostbyname(host_name)

# # the IP address
# print(f"IP address of {host_name}: {ip_address}")

# # Get the host name and IP address of the local machine
# local_host_name = socket.gethostname()
# local_ip_address = socket.gethostbyname(local_host_name)

# # Print the local machine details
# print(f"Local host name: {local_host_name}")
# print(f"Local IP address: {local_ip_address}")

# from ipwhois import IPWhois

# # Get the IP address from the user
# ip_address = input("Enter the IP address: ")

# # Look up the IP address details
# ipwhois = IPWhois(ip_address)
# results = ipwhois.lookup_rdap()

# # Print the IP address details
# print(f"IP address: {results['query']}")
# print(f"Country: {results['asn_country_code']}")
# print(f"ASN: {results['asn']}")
# print(f"ISP: {results['asn_description']}")

# try:
#     city = results['city']
#     print(f"City: {city}")
# except KeyError:
#     print("City information unavailable")

# print(f"State/Region: {results['region']}")
# print(f"Zip code: {results['postal_code']}")
# print(f"Latitude: {results['latitude']}")
# print(f"Longitude: {results['longitude']}")

""" Trackin by phone number"""

# import phonenumbers
# from phonenumbers import carrier

# myNumber = '+856 2078671726'

# from phonenumbers import geocoder

# doneNumber = phonenumbers.parse(myNumber)

# location = geocoder.description_for_number(doneNumber, 'en')
# service_provider = phonenumbers.parse(myNumber)

# print(carrier.name_for_number(service_provider, "en"))

# print(location)

"""Traking location by ip addres"""

# import requests

# ip_address = "142.250.199.14"  # Replace with the IP address you want to locate

# response = requests.get(f"https://ipapi.co/{ip_address}/json/")
# data = response.json()

# rg = data["region"]
# latitude = data["latitude"]
# longitude = data["longitude"]
# city = data["city"]

# print(data)
# print(f"Region: {rg}")
# print(f"Latitude: {latitude}")
# print(f"Longitude: {longitude}")
# print(f"City: {city}")
# print(f"City: {city}")
"""
"ip" : "8.8.8.8"
"city" : "Mountain View"
"region" : "California"
"region_code" : "CA"
"country_code" : "US"
"country_code_iso3" : "USA"
"country_name" : "United States"
"country_capital" : "Washington"
"country_tld" : ".us"
"continent_code" : "NA"
"in_eu" : false
"postal" : "94035"
"latitude" : 37.386
"longitude" : -122.0838
"timezone" : "America/Los_Angeles"
"utc_offset" : "-0700"
"country_calling_code" : "+1"
"currency" : "USD"
"currency_name" : "Dollar"
"languages" : "en-US,es-US,haw"
"asn" : "AS15169"
"org" : "Google LLC"
"""
