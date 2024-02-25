# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hFgjSg4gdr1T9VOt3sS5RAim02SZEqVt
"""

class Passenger:
    def __init__(self, name, electronic_ticket):
        self.name = name
        self.electronic_ticket = electronic_ticket

class Flight:
    def __init__(self, flight_number, departure_city, destination_city, departure_date, boarding_time, arrival_time, terminal, gate):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.departure_date = departure_date
        self.boarding_time = boarding_time
        self.arrival_time = arrival_time
        self.terminal = terminal
        self.gate = gate

class BoardingPass:
    def __init__(self, seat, boarding_time, gate, flight, passenger):
        self.seat = seat
        self.boarding_time = boarding_time
        self.gate = gate
        self.flight = flight
        self.passenger = passenger

class Seat:
    def __init__(self, seat_number, availability=True):
        self.seat_number = seat_number
        self.availability = availability

# Create objects
passenger = Passenger(name="Maryam matar", electronic_ticket="629")
flight = Flight(flight_number="NA4321", departure_city="CHICAGO ORD", destination_city="NEW YORK JFK", departure_date="06 DEC 20",
                boarding_time="11:20", arrival_time="13:30", terminal="2", gate="03")
seat = Seat(seat_number="09A")
boarding_pass = BoardingPass(seat=seat, boarding_time="11:40", gate="03", flight=flight, passenger=passenger)

# Display boarding pass details
print("Passenger:", boarding_pass.passenger.name)
print("From:", flight.departure_city)
print("Flight:", flight.flight_number)
print("Gate:", boarding_pass.gate)
print("Date:", flight.departure_date)
print("Boarding till:", boarding_pass.boarding_time)
print("Electronic ticket:", passenger.electronic_ticket)
print("Time:", flight.arrival_time)
print("Seat:", boarding_pass.seat.seat_number)
print("To:", flight.destination_city)
print("Arrival time:", flight.arrival_time)
print("Terminal:", flight.terminal)

