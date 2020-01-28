import requests


class LocationList:
    def __init__(self, credenvelope):
        self.api_username = credenvelope['api_username']
        self.api_password = credenvelope['api_password'] 
        self.api_url = credenvelope['api_url']
    
    def __str__(self):
        return "Location List Object.."


class ServiceList:
    def __init__(self, credenvelope):
        self.api_username = credenvelope['api_username']
        self.api_password = credenvelope['api_password'] 
        self.api_url = credenvelope['api_url']

    def __str__(self):
        return "Service List Object.."
