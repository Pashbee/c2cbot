from rttapi.factory import LocationList, ServiceList 


AVAIL_RESOURCES = ["location", "service"]


class UnknownResource(Exception):
    pass


def resource(rtype, api_username, api_password):
    """Resource factory method."""
    if rtype == "location":
        resource = LocationList(api_username, api_password)
    elif rtype == "service":
        resource = ServiceList(api_username, api_password)
    else:
        raise UnknownResource('Please select from {0}'.format(rtype,
                              AVAIL_RESOURCES))
    return resource
