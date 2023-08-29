from bus_stop import BusStop
class Bus:
    def __init__(self, input_route_number, input_destination):
        self.route_number = input_route_number
        self.destination = input_destination
        self.passengers = []

    def drive(self):
        return("Brum Brum")
    
    def get_passenger_number(self):
        return(len(self.passengers))
    
    def pick_up_passenger(self, input_passenger):
        self.passengers.append(input_passenger)

    def drop_off_passenger(self, input_passenger):
        self.passengers.remove(input_passenger)
        
    def empty_passengers(self):
        self.passengers = []

    def pick_up_from_stop(self, input_bus_stop: BusStop):
        for passenger in input_bus_stop.queue:
            self.pick_up_passenger(passenger)
        input_bus_stop.empty_queue()



