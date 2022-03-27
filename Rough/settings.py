# Import required libraries and the other files in this directory.




# Step 1: Import the required libraries including PyFirmata
from pyfirmata import ArduinoMega, util
import time  # time.sleep(time in seconds) is equivalent to Arduino function delay(time in milliseconds)
# other libraries (if needed)



# Defining some constants
PORT = "COM7"  # defining the port the arduino is connected to
# Change the port number according to your setup.
ERROR = 2  # Backlash error in DEGREES


# =========-=========-=========-=========-=========-=========-=========-
# Step 2: Define variables for the pins for each motor
# Example:
# smflpn = <an integer denoting the pin number> # Steering Motor Forward Left Plus pin Number
# Note: You need not use this particular naming patterns of the variables, but be
#       consistent with your own pattern and clearly define it (in the *Convensions*
#       section at the README.md file) before using.
#
#    We have two types of motors, Steering motors and Driving motors.
# In each leg we will have a potentiometer to know the current position of the steering
# motor. We have 6 legs in our rover. So you need to define two pins (plus and minus)
# for each of the 12 (6legs*2types of motors (steering and driving)) motors. Moreover,
# you need to define a pin for the potentiometer. That makes 24+6=30 pins. The 6 pins
# from the potentiometers will go to the analog input pins, and the rest should go to
# the PWM pins (because we need to control the speed).
# PROBLEM: Arduino MEGA has only 14 pwm pins (but we need 24).
# But wait a second! Do we really need to have 24 PWM pins?
# We need to regulate only the difference between two pins of the same motor.
# So we can keep one pin of each leg a normal digital pin, and other can be PWM.
# Thus we can have the difference in potential between the two pins of the same
# motor anything between -5V to +5V. (Arduino MEGA works on 5V potensial)
# Long story Short:
#       1. Name the variables wisely and define your convension.
#       2. Study the pin diagram of Arduino MEGA.
#           Link: https://github.com/PeithonKing/AMAR/blob/master/RoverMotorDriver/Arduino-Mega-Pinout.png
#       3. Assign all(12) minus pins of both types of motors to the non-PWM digital pins.
#       4. Assign all(12) plus pins of both types of motors to the PWM digital pins.
#       5. Assign all(6) pins of the potentiometer to the analog input pins.
#















# =========-=========-=========-=========-=========-=========-=========-
# Step 3: Initialise the board and all the pins to be used as mentioned in Step 2.
board = ArduinoMega(PORT)  # Initialising the Arduino Mega

it = util.Iterator(board)  # Initialising the iterator to read the data from the board.
it.start()  # Starting the iterator. These two lines are needed if you want to take inputs.

# initialise 12 non-PWM digital output pins for the minus sides of the 12 motors
# Example:
# smflp = board.get_pin("d:" + str(smflpn) + ":o") # Steering Motor Forward Left Plus pin
#





# initialise 12 PWM digital output pins for the plus sides of the 12 motors
# Do here similarly as the above example
#





# initialise 6 analog input pins for the potentiometer
# Do here similarly as the above example
#







