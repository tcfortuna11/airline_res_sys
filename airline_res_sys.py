import pdb
import numpy
first_seat = ['a','b','c','d']
econ_seat = first_seat + ['e','f']

#create Seat class
class Seat():
   '''
   This is the Seat class
   attributes: row, seat, status
   '''

   def __init__(self,row,seat):
      self.row = row
      self.seat = seat
      self.status = "A"

   def __str__(self):
      return str(self.row)+str(self.seat)+ ", (" +self.status + ")"

#create Plane class
class Plane():
   '''
   This is the Plane class
   attributes: seats (dictionary of Seat() class objects)
               first_prices is list of prices
               econ_prices is list of prices
   methods: reserve_reserve
   '''

   def __init__(self):
      self.seats = {}
      self.first_prices = []
      self.econ_prices = []
      # generate first class rows
      for row in range(1,5):
         for seat in first_seat:
            self.seats.update({str(row)+seat:Seat(row,seat)})
            self.first_prices.append(round(numpy.random.normal(300,10,None),2))
      # generate economy rows
      for row in range(5,31):
         for seat in econ_seat:
            self.seats.update({str(row)+seat:Seat(row,seat)})
            self.econ_prices.append(round(numpy.random.normal(100,10,None),2))
      # sort
      self.first_prices.sort()
      self.econ_prices.sort()

   def __str__(self):
      plane_str = 'The plane is:'
      plane_row = 0
      for key,seat in self.seats.items():
         if seat.row == plane_row:
            plane_str += '|{0:9}'.format(seat.__str__())
         else:
            plane_str += '\n{0:9}'.format(seat.__str__())
            plane_row += 1
      return plane_str

   def reserve_seat(self,row,seat):
      self.seats[str(row)+seat].status = "R"
      if row <= 4:
         self.first_prices.pop(0)
      else:
         self.econ_prices.pop(0)

   def cancel_seat(self,row,seat):
      self.seats[str(row)+seat].status = "A"

   def seats_avail(self):
      for key,seat in self.seats.items():
         if seat.status == "R":
            return False
      return True

def flight_input(flight_schedule):
   '''
   This function takes the input from the user on what flight
   they would like. It continues to ask the user
   which flight until they pick an available flight. It returns
   the key of the flight they would like.
   '''
   while True:
      try:
         flight_key = str(input("What flight would you like to reserve? (ex. 0600 or 0900)"))
      except:
         print("Please enter a string value")
         continue
      else:
         if not(flight_schedule[flight_key].seats_avail):
            print("No seats available on this flight. Please select another flight");
            continue
         else:
            return flight_key
            #break

def reserve_input(plane):
   '''
   This function takes the input from the user on what seat
   they would like to reserve. It continues to ask the user
   which seat until they pick an available seat. It returns
   the key of the seat they would like to reserve.
   '''
   while True:
      try:
         row = int(input("What row would you like to sit in?\n"))
         seat = str(input("What seat would you like to sit in?\n"))
         seat_key = str(row)+seat
      except:
         print("Please enter a string value")
         continue
      else:
         if plane.seats[seat_key].status == "R":
            print("Seat not available. Please select another seat");
            continue
         else:
            return row,seat
            #break

def confirm_reservation(row,seat):
   '''
   This function takes the input from the user to confirm
   the seat they would like to reserve. It continues to ask
   the user which to confirm until they enter y or n. It
   returns a boolean.
   '''
   while True:
      try:
         confirm_input = str(input("Confirm you would like to make the reservation? y/n\n"))
      except:
         print("Please enter a string value")
         continue
      else:
         if confirm_input.lower() == "y":
            return True
         else:
            return False
            #break

# create flight schedule (dictionary of flights -> time; = key, plane instance = value)
flight_schedule = {'0600':Plane(),'0900':Plane(),'1200':Plane(),'1900':Plane()}
# display cheapest economy and first class fares for each flight
flight_times = ['0600','0900','1200','1900']
for time in flight_times:
    print('Flight {} prices:'.format(time))
    print('first class:') 
    print('{0:>8.2f}'.format(flight_schedule[time].first_prices[0])) #right align >, 2 decimals .2f
    print('econ  class:')
    print('{0:>8.2f}\n'.format(flight_schedule[time].econ_prices[0])) #right align >, 2 decimals .2f

while True:
   # prompt user to select flight
   flight_key = flight_input(flight_schedule)
   print(flight_key)
   # display seats available
   print(flight_schedule[flight_key])
   # prompt user to select seat
   row,seat = reserve_input(flight_schedule[flight_key])
   # ask user to confirm purchase
   if confirm_reservation(row,seat):
      # book seat and break
      flight_schedule[flight_key].reserve_seat(row,seat)
      break
   else:
      continue


#plane_test = Plane()
#pdb.set_trace()
#print(flight_schedule['0600'])
#print(flight_schedule['0900'])
#print(flight_schedule['1200'])
#print(flight_schedule['1900'])
#plane_test.reserve_seat(1,'a')
#plane_test.reserve_seat(1,'a')
#print(plane_test)
#reserve_input(plane_test)
#print(plane_test)
