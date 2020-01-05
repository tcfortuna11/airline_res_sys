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

def reserve_input(plane):
   '''
   This function takes the input from the user on what seat
   they would like to reserve. It continues to ask the user
   which seat until they pick an available seat. It returns
   the key of the seat they would like to reserve.
   '''
   while True:
      try:
         seat_key = str(input("What seat would you like to sit in? (ex. 1a or 30b)"))
      except:
         print("Please enter a string value")
         continue
      else:
         if plane.seats[seat_key].status == "R":
            print("Seat not available. Please select another seat");
            continue
         else:
            return seat_key
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

# prompt user to select flight and class
# display seats available
# prompt user to select seat
# ask user to confirm purchase
# book seat and break


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
