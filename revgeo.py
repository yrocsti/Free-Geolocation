"""Enter a U.S. address and use the U.S. Census to get the longitude and latitude for the entered address. self.data will return decimal degrees (example: -122.890267). Convert function output is degrees minutes seconds format."""

import requests


class RevGeo:
    """Create an object for reverse geolocation for free."""

    rbenchmark = 'Public_AR_Current'
    rformat = 'json'

    def __init__(self, address, city, state, zip_code):
        """Initialize address parameters for requests."""
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.data = self.get_long_lat()

    def get_long_lat(self) -> tuple:
        """Create payload for request."""
        payload = {'street': self.address, 'city': self.city, 'state': self.state, 'zip': self.zip_code, 'benchmark': self.rbenchmark, 'format': self.rformat}

        """Respone from the U.S. Census in a json file format"""
        response = requests.get("https://geocoding.geo.census.gov/geocoder/locations/address", params=payload)

        data = response.json()
        """Will return Long and Lat if address is found."""
        if data['result']['addressMatches'][0]['matchedAddress'] is None:
            return f"address: {self.street} {self.city} {self.state} {self.zip_code} was not found. Please try another address."
        else:
            return (data['result']['addressMatches'][0]['coordinates']['x'], data['result']['addressMatches'][0]['coordinates']['y'])

    def convert_to_dms(self) -> tuple:
        """Convert longitude and latitude from decimal degrees to DMS format as a tuple."""
        dms = []
        for num in self.data:
            slat = str(num)
            d, md = map(int, slat.split('.'))
            dec_minutes = (abs(num) - abs(d)) * 60

            smin = str(dec_minutes)
            minutes, sd = map(int, smin.split('.'))
            seconds = (abs(dec_minutes) - abs(minutes)) * 60
            dms.append(f'{d}:{minutes}:{round(seconds)}')
        dms = tuple(dms)

        return dms
