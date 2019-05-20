import requests


class LocationList:
    def __init__(self, api_username, api_password):
        self.api_username = api_username
        self.api_password = api_password
    
    def __str__(self):
        return "Location List Object.."


class ServiceList:
    def __init__(self, api_username, api_password):
        self.api_username = api_username
        self.api_password = api_password

    def __str__(self):
        return "Service List Object.."
