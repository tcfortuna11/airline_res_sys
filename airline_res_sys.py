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
      self.plane = []
      # generate first class rows
      for row in range(1,5):
         for seat in first_seat:
            self.plane.append(Seat(row,seat))
      # generate cabin rows
      for row in range(5,31):
         for seat in cabin_seat:
            self.plane.append(Seat(row,seat))

   def __str__(self):
      plane_str = 'The plane is:'
      plane_row = 0
      for seat in self.plane:
         if seat.row == plane_row:
            plane_str += '|{0:9}'.format(seat.__str__())
         else:
            plane_str += '\n{0:9}'.format(seat.__str__())
            plane_row += 1
      return plane_str

plane_test = Plane()
print(plane_test)