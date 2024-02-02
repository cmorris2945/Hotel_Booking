
import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id":str})

class Hotel:

    watermark = "The Real Estate Company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to "NO"  """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)


    def available(self):
        """This checks to see if the hotel is available..."""
        availability =  df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False
    def _add__(self, other):
        total = self.price + other.price
        return total

class Ticket:
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    def generate(self):
        content = f""" 
          Thank you for your reservation!
        Here is your booking and reservation data: 
        Name: {self.the_customer_name}
        Hotel Name: {self.hotel}
           """
        return content
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = self.title()
        return name



    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    @staticmethod
    def convert(amount):
        return amount *1.2

class DigitalTicket(Ticket):
    def generate(self):
        return "hello, this is your digital ticket"

    def download(self):
class DigitalTicket(Ticket):
    def generate(self):


hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="135")



















