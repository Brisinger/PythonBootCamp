# Train class
"""
Class for booking a Train
"""
class Train:
    Organization = "Indian Railways"
    Pricing = {
        '1A': 1500,
        '2A': 1000,
        '3A': 780,
        'SL': 420
    }
    Booking = {
        '1A': 0,
        '2A': 0,
        '3A': 0,
        'SL': 0
    }

    def __init__(self, name, train) -> None:
        self.name = name
        self.train = train
        self.seats = sum(Train.Booking.values())
        match self.train:
            case "Duronto Express":
                self.available = 120
            case "Rajdhani Express":
                self.available = 90
            case _:
                self.available = 78

    def bookTickets(self, ticket, obj):
        if (self.getStatus(obj)>0):
            obj.Booking[ticket[0:2]] += 1
            obj.seats = sum(obj.Booking.values())

    def getStatus(self, obj):
        return self.available - obj.seats

    def getFareInfo(self, obj):
        totalFare = 0.0
        file = "10_practice05.txt"
        with open(file=file, mode="at") as writer:
            text = f"Ticket booking details of {obj.name}:\nBooking\t\tNo. of seats\tPrice\n"
            writer.write(text)

        for item in self.Booking:
            totalFare += obj.Booking[item] * self.Pricing[item]
            if (obj.Booking[item] > 0):
                with open(file=file, mode="at") as writer:
                   text = f"{item:<12}\t{obj.Booking[item]:<10}\t{self.Pricing[item]:<10.2f}\n"
                   writer.write(text)
        else:
            with open(file=file, mode="at") as writer:
               text = f"\n{obj.name}, your total fare is: INR {totalFare:.2f}\n\n"
               writer.write(text)
            return f"Fare info successfully generated for {obj.name}"


# Creating Train Booking objects
shubho = Train(name="Shubhojit Dasgupta", train="Rajdhani Express")
harry = Train(name="Harry", train="Rajdhani Express")

# Booking tickets for objects
shubho.bookTickets(ticket="SL12", obj=shubho)
shubho.bookTickets(ticket="2A01", obj=shubho)

harry.bookTickets(ticket="SL10", obj=harry)
harry.bookTickets(ticket="SL14", obj=harry)

# Get total fare for passenger
print(shubho.getFareInfo(shubho))
print(harry.getFareInfo(harry))

# Total seats available
print(harry.getStatus(harry), "seats available.")
harry.Booking = {}
print(Train.Booking)
print(harry.getStatus(harry), "seats available.")
print(harry.Booking)