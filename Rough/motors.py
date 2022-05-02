

# Step 4: Define a class for Steering Motor.
class SteeringMotor:
    """SteeringMotor(plus, minus, pot)

    A class to represent a Steering Motor.

    Attributes
    ----------
    plus : type = pyfirmata.pyfirmata.Pin
        The plus pin of the steering motor.
        This is a PWM output pin.
    minus : type = pyfirmata.pyfirmata.Pin
        The minus pin of the steering motor.
        This is a non-PWM output pin.
    pot : type = pyfirmata.pyfirmata.Pin
        The input pin which the potentiometer is connected to.
    name : str
        This is a string defining position of this steering motor.
        This variable will only help in debugging purpose.
        for example, for the front left steering motor:
            name = "Front Left"

    Methods
    -------
        # complete this
        get_position() :
            Returns current of the steering motor in degrees.
        move(v,t=1) : 
            Dynamically rotates the steering motor base on velocity and time.
        goto(position) :
            Rotates the motor to a specific angle at full speed.
    """

    def __init__(self, plus, minus, pot, name="Unknown"):
        """
        Construct all the necessary attributes of a Steering wheel.
        This function runs every time an instance of a steering motor is created.

        Parameters
        ----------
        plus : type = pyfirmata.pyfirmata.Pin
            The plus pin of the steering motor.
            This is a PWM output pin.
        minus : type = pyfirmata.pyfirmata.Pin
            The minus pin of the steering motor.
            This is a non-PWM output pin.
        pot : type = pyfirmata.pyfirmata.Pin
            The input pin the potentiometer is connected to.
        name : str
            This is a string defining position of this steering motor.
            for example, for the front left steering motor:
                name = "Front Left"
        """
        self.plus = plus
        self.minus = minus
        self.pot = pot
        self.name = name
        self.current_position = self.get_position()

    def get_position(self):
        """
        Reads the potentiometer value and Returns the current position of the
        steering motor in degrees. Its value is between 0 and 360 degrees.
        """
        # some code will be here which will do the job, but you don't need to
        # do this right now! It will be done once the Rover is up and running.
        # for now, we are just going to return a linear function.
        #
        ll = 0.1  # lower limit of x (>=0)
        ul = 0.9  # upper limit of x (<=1)
        # x = self.pot.read()  # x ∈ [ll, ul] (closed interval)
        x = 0.69
        return 360 * (x - ll) / (ul - ll)

    def move(self, v, t=1):  # t in seconds
        # write the appropriate docstrings here
        # write code for moving the motor clockwise for t seconds at speed v (v ∈ [-100, 100]).
        # Meaning of "Speed":
        #       The potenial difference between self.plus and self.minus = 5v/100 = pd (say)
        # If v is positive, the motor will move counterclockwise and self.minus will be at 0V and
        # self.plus will be at pd. Similarly if v is negative, the motor will move clockwise
        # and self.minus will be at 5V and self.plus will be at (5-pd)V. (don't forget self.minus can
        # only have binary values, 0V  and 5V and self.plus can only have values between 0V and 5V)
        #

        pass

    def goto(self, position):
        started_from = self.get_position()
        # write the appropriate docstrings here
        # position is a float/integer between 0 and 360 degrees
        # objective of this function is to move the steering motor to the required position
        # 
        # Process: Start by calculating the difference between the current position and the
        # required position (say θ degrees). Call the move() function in full speed
        # (v = 100 if θ > 0 and v = -100 if θ < 0) for t = 1s. Then proportionally decrease the speed
        # of the motor with respect to the new distance (θnew) and call move(). Continue until the
        # [required position ± ERROR (defined at the beginning)] is reached.
        #
        print(f"The {self.name} steering motor moved to {round(position, 2)}° from {round(started_from, 2)}°")  # comment this line on completion


# =========-=========-=========-=========-=========-=========-=========-
# Step 5: similarly write a class for the Driving Motors
class DrivingMotor:
    """DrivingMotor(plus, minus, pot)

    A class to represent a Steering Motor.

    Attributes
    ----------
    plus : type = pyfirmata.pyfirmata.Pin
        The plus pin of the steering motor.
        This is a PWM output pin.
    minus : type = pyfirmata.pyfirmata.Pin
        The minus pin of the steering motor.
        This is a non-PWM output pin.
    pot : type = pyfirmata.pyfirmata.Pin
        The input pin which the potentiometer is connected to.
    name : str
        This is a string defining position of this steering motor.
        This variable will only help in debugging purpose.
        for example, for the front left steering motor:
            name = "Front Left"

    Methods
    -------
        # complete this
        forward(speed) :
            Rotates the motor such that it moves forward.
        backward(speed) :
            Rotates the motor such that it moves backward.
        stop() :
            Stops any rotation in the motor.
    """

    def __init__(self, plus, minus, steering):
        # Docstring
        self.plus = plus
        self.minus = minus
        self.steering = steering  # the instance of the SteeringMotor() corresponding to this motor will be passed
        self.name = steering.name
    
    def forward(self, speed):
        # complete and add docstring
        # starts this driving motor in forward direction in speed = speed
        # Note: let p = steering.get_position(). if p>180, forward will be equal to p<180 backward.
        # 
        pass
    
    def backward(self, speed):
        # complete and add docstring
        # starts this driving motor in backward direction in speed = speed
        # 
        pass
    
    def stop(self):
        # complete and add docstring
        # stops the motor whichever direction it was moving in.
        pass


if __name__ == "__main__":
    from settings import *
    # fl = SteeringMotor(smflp, smflm, smflpot, "Front Left")  # initialising the front left steering motor
    fl = SteeringMotor(None, None, None, "Front Left")  # initialising the front left steering motor

    fl.goto(75.488)  # moving the front left steering motor to 75 degrees