#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets):
    """
    YOUR CODE HERE
    """
    trip=[]
    routes = {}
    for ticket in tickets:
        routes[ticket.source]=ticket.destination
    
    # print(routes)

    src_dest_airport="NONE"
    
    route_src = src_dest_airport
    while routes[route_src] != src_dest_airport:
        route_dest = routes[route_src]
        trip.append(route_dest)
        # dest of prev lag of trip is src of next lag of trip
        route_src = route_dest

    # add final dest airport that ends the whole trip
    trip.append(src_dest_airport)

    return trip 
    
# test
trip = reconstruct_trip([
    Ticket ("PIT", "ORD"),
    Ticket ("XNA", "CID"),
    Ticket ("SFO", "BHM"),
    Ticket ("FLG", "XNA"),
    Ticket ("NONE", "LAX"),
    Ticket ( "LAX", "SFO"),
    Ticket ("CID", "SLC"),
    Ticket ("ORD", "NONE"),
    Ticket ("SLC", "PIT"),
    Ticket ("BHM", "FLG")
])
print(trip)