class Person:
    def __init__(self, name, age, destination):
        self.name = name
        self.age = age
        self.destination = destination

    def check_destination_of_bus(self, bus):
        if bus.destination == self.destination:
            return True

    def get_on_bus(self, bus_stop):
        bus_stop.queue.append(self)
        if self.check_destination_of_bus(bus) == True:
            bus.pick_up_from_stop(bus_stop)
            


        

        
    