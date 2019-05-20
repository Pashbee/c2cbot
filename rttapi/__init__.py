from rttapi.factory import LocationList, ServiceList 


AVAIL_RESOURCES = ["location", "service"]

class UnknownResource(Exception):
    pass


def resource(rtype, api_username, api_password):
    """Resource factory method."""
    if rtype == "location":
        rreturn = LocationList(api_username, api_password)
    elif rtype == "service":
        rreturn = ServiceList(api_username, api_password) 
    else:
        raise UnknownResource('UnknownResource - Please select from {0}'.format(AVAIL_RESOURCES))
    return rreturn
