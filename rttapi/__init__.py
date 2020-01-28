from rttapi.factory import LocationList, ServiceList 


AVAIL_RESOURCES = ["location", "service"]


class UnknownResource(Exception):
    pass


def resource(rtype, credenvelope):
    """Resource factory method."""
    if rtype == "location":
        resource = LocationList(credenvelope)
    elif rtype == "service":
        resource = ServiceList(credenvelope)
    else:
        raise UnknownResource('{0} not found. Please select from {1}'.format(rtype,
                              AVAIL_RESOURCES))
    return resource
