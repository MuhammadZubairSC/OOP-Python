class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        
        self.bottom = bottom
        self.top = top
        self.current= current
        pass
    def __str__(self):
        return "Current floor:{}".format(self.current)
    
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current<self.top:
            self.current = self.current +1 
        else:
            pass
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current>self.bottom:
            self.current = self.current -1 
        else:
            pass
        pass
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        floor=floor
        if floor>self.current:
            count=floor-self.current
            for i in range(1, (floor+1)):
                self.current = self.current +1
 
        if floor<self.current:
            count=self.current-floor
            for i in range(1, (count+1)):
                self.current = self.current -1

elevator = Elevator(-1, 10, 0)

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1