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
#
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

#Refer 'convensions' for labelling conventions used below

#Plus motors--Digital PWM
# =============================================================================
# sm_fl_p = D2
# dm_fl_p = D3
# sm_fr_p = D4
# dm_fr_p = D5
# sm_ml_p = D6
# dm_ml_p = D7
# sm_mr_p = D8
# dm_mr_p = D9
# sm_bl_p = D10
# dm_bl_p = D11
# sm_br_p = D12
# dm_br_p = D13
# =============================================================================

#Minus motors--Digital
# =============================================================================
# sm_fl_n = D22
# dm_fl_n = D23
# sm_fr_n = D24
# dm_fr_n = D25
# sm_ml_n = D26
# dm_ml_n = D27
# sm_mr_n = D28
# dm_mr_n = D29
# sm_bl_n = D30
# dm_bl_n = D31
# sm_br_n = D32
# dm_br_n = D33
# =============================================================================

#Potentiometers--Analog
#==============================================================================
# pr_fl = A0
# pr_fr = A1
# pr_ml = A2
# pr_mr = A3
# pr_bl = A4
# pr_br = A5
# =============================================================================

# =========-=========-=========-=========-=========-=========-=========-
# Step 3: Initialise the board and all the pins to be used as mentioned in Step 2.
board = ArduinoMega(PORT)  # Initialising the Arduino Mega

it = util.Iterator(board)  # Initialising the iterator to read the data from the board.
it.start()  # Starting the iterator. These two lines are needed if you want to take inputs.



# initialising 12 PWM digital output pins for the plus sides of the 12 motors
sm_fl_p = board.get_pin('d:2:p') 
dm_fl_p = board.get_pin('d:3:p')
sm_fr_p = board.get_pin('d:4:p')
dm_fr_p = board.get_pin('d:5:p')
sm_ml_p = board.get_pin('d:6:p')
dm_ml_p = board.get_pin('d:7:p')
sm_mr_p = board.get_pin('d:8:p')
dm_mr_p = board.get_pin('d:9:p')
sm_bl_p = board.get_pin('d:10:p')
dm_bl_p = board.get_pin('d:11:p')
sm_br_p = board.get_pin('d:12:p')
dm_br_p = board.get_pin('d:13:p')


# initialising 12 non-PWM digital output pins for the minus sides of the 12 motors
sm_fl_n = board.get_pin('d:22:o') 
dm_fl_n = board.get_pin('d:23:o')
sm_fr_n = board.get_pin('d:24:o')
dm_fr_n = board.get_pin('d:25:o')
sm_ml_n = board.get_pin('d:26:o')
dm_ml_n = board.get_pin('d:27:o')
sm_mr_n = board.get_pin('d:28:o')
dm_mr_n = board.get_pin('d:29:o')
sm_bl_n = board.get_pin('d:30:o')
dm_bl_n = board.get_pin('d:31:o')
sm_br_n = board.get_pin('d:32:o')
dm_br_n = board.get_pin('d:33:o')

# initialising 6 analog input pins for the potentiometer
pr_fl = board.get_pin('a:0:i')
pr_fr = board.get_pin('a:1:i')
pr_ml = board.get_pin('a:2:i')
pr_mr = board.get_pin('a:3:i') 
pr_bl = board.get_pin('a:4:i') 
pr_br = board.get_pin('a:5:i') 
