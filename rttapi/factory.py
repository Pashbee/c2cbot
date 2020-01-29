import requests as r
from datetime import datetime

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

    def get_service(self, **kwargs):
        stdate = datetime.strptime(kwargs['stdate'], '%d%m%Y')
        api_params = [kwargs['ststat'],
                      stdate.year,
                      stdate.strftime('%m'),
                      stdate.strftime('%d'),
                      kwargs['sttime']]
        ccall = '{0}json/search/{1}/{2}/{3}/{4}/{5}'.format(self.api_url, *api_params)
        print(ccall)
        services = r.get(ccall, auth=r.auth.HTTPBasicAuth(self.api_username, self.api_password))
        return services.json()