# Import required libraries and the other files in this directory.


# =========-=========-=========-=========-=========-=========-=========-
# Step 6: Write a class for the Rover
class Rover:
    # Docstring here
    def __init__(self, Steering, Driving):
        # Docstring
        # states
        self.vx = 0  # forward speed ∈ [-100, 100]
        self.vy = 0  # leftways speed ∈ [-100, 100]
        # Steering and Driving are lists of len 6 contanining the
        # instances of the SteeringMotor() and DrivingMotor()
        self.front_left_steering = Steering[0]
        self.front_left_driving = Driving[0]
        self.middle_left_steering = Steering[1]
        self.middle_left_driving = Driving[1]
        # and so on for the other 6*2 = 12 motors
    
    # Define the following methods and make them work. Don't forget
    # to write the appropriate docstrings for each:
    # let max speed = 100
    #   1. forward(self, speed)  # moves the rover forward
    #   2. backward(self, speed)  # moves the rover backwards
    #   3. stop(self, speed)  # stops the rover
    #   4. left(self, speed)
    #   5. right(self, speed)
    #   6. revolve(self, speed)  # revolves without translation
    #   7. turn(self, angle, radius)  # takes turns while self.vx!=0
    #         radius is a positive float in meters
    #         angle belongs to set of whole numbers (both positive and negative)
    #         this is complex bit of code, so write with care.
    #   8. move(self, speed, angle)  # moves the rover in a straight line at angle with its principle axis.
    #   9. we would add more methods here
    # 
    # 
    #     This is the toughest part of the code. You need to write this part
    # with utmost care. You need to learn how to simulate multithreading in
    # python to move all the steerings symultaneously. Simulate because python
    # does not support multithreading. If you can't write some part of the code,
    # leave it. If you are stuck, consult in the Discord server. If you think
    # some function is redundant and that job can be taken care of by another
    # function, leave it. This is quite an open ended problem and we want your
    # inovative mind to solve it.


if __name__ == "__main__":
    # Import the libraries and all the other modules defined
    # write some code here to test your model
    pass