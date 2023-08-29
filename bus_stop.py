class BusStop:
    def __init__(self, input_name):
        BusStop.name = input_name
        BusStop.queue = []

    def add_to_queue(self, input_person):
        BusStop.queue.append(input_person)

    def empty_queue(self):
        BusStop.queue = []

    def queue_length(self):
        return(len(BusStop.queue))