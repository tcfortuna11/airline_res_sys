import pdb
first_seat = ['a','b','c','d']
cabin_seat = first_seat + ['e','f']

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
   attributes: plane (list of Seat() class objects)
   methods: reserve_reserve
   '''

   def __init__(self):
      self.plane = {}
      # generate first class rows
      for row in range(1,5):
         for seat in first_seat:
            self.plane.update({str(row)+seat:Seat(row,seat)})
      # generate cabin rows
      for row in range(5,31):
         for seat in cabin_seat:
            self.plane.update({str(row)+seat:Seat(row,seat)})

   def __str__(self):
      plane_str = 'The plane is:'
      plane_row = 0
      for key,seat in self.plane.items():
         if seat.row == plane_row:
            plane_str += '|{0:9}'.format(seat.__str__())
         else:
            plane_str += '\n{0:9}'.format(seat.__str__())
            plane_row += 1
      return plane_str

   def reserve_seat(self,row,seat):
      self.plane[str(row)+seat].status = "R"

def reserve_input(plane):
   '''
   This function takes the input from the user on what seat
   they would like to reserve. It continues to ask the user
   which seat until they pick an available seat.
   '''
   while True:
      try:
         seat_key = str(input("What seat would you like to sit in? (ex. 1a or 30b)"))
      except:
         print("Please enter a string value")
         continue
      else:
         if plane.plane[seat_key].status == "R":
            print("Seat not available. Please select another seat")
            continue
         else:
            plane.reserve_seat(plane.plane[seat_key].row,plane.plane[seat_key].seat)
            break

plane_test = Plane()
#pdb.set_trace()
print(plane_test)
plane_test.reserve_seat(1,'a')
print(plane_test)
reserve_input(plane_test)
print(plane_test)