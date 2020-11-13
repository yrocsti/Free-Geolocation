import json
import requests


def get_address(address, city, state, zip_code):
    """Returns the payload parameter for the U.S. Census API request."""
    st_address = address
    u_city = city
    u_state = state
    u_zip = zip_code
    rbenchmark = 'Public_AR_Current'
    rformat = 'json'

    return {'street': st_address, 'city': u_city, 'state': u_state, 'zip': u_zip, 'benchmark': rbenchmark, 'format': rformat}


def get_info(payload):
    """Respone from the U.S. Census in a json file format"""
    response = requests.get("https://geocoding.geo.census.gov/geocoder/locations/address", params=payload)

    return response.json()


def convert(orig_lat: float) -> tuple:
    """ Converting latitude or longitude from decimal degrees to DMS format as a tuple"""
    slat = str(orig_lat)
    d, md = map(int, slat.split('.'))
    dec_minutes = (abs(orig_lat) - abs(d)) * 60

    smin = str(dec_minutes)
    minutes, sd = map(int, smin.split('.'))
    seconds = (abs(dec_minutes) - abs(minutes)) * 60

    return d, minutes, round(seconds)


"""
Uncomment this section to run script locally for your testing purposes
"""
##in_street = input("Enter street address: ")
##in_city = input("Enter city: ")
##in_state = input("Enter state: ")
##in_zip = input("Enter zip code: ")
##in_format = input("Would you like your results in D, M, S?: \n Enter Y or N: ")

user_address = get_address(in_street, in_city, in_state, in_zip)
data = get_info(user_address)


"""The following can be used for testing as well."""
##if data['result']['addressMatches'][0]['matchedAddress'] == None:
##    print(f"address: {in_street} {in_city} {in_state} {in_zip} was not found. Please try another address.")
##else:
##    long = data['result']['addressMatches'][0]['coordinates']['x']  
##    lat = data['result']['addressMatches'][0]['coordinates']['y']
##
##    if in_format == 'N':
##        print(f'longitude: {long} latitude: {lat}')
##    else:
##        dms_lat = convert(lat)
##        dms_long = convert(long)
##
##        print(f"Latitude - Degrees: {dms_lat[0]} Minutes: {dms_lat[1]} Seconds: {dms_lat[2]} \nLongitude - Degrees: {dms_long[0]} Minutes: {dms_long[1]} Seconds: {dms_long[2]}")
