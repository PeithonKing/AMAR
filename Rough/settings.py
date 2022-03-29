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

#Refer 'convensions' for labelling conventions used below

#Plus motors--Digital PWM
# =============================================================================
# sm_f_l_p = D2
# dm_f_l_p = D3
# sm_f_r_p = D4
# dm_f_r_p = D5
# sm_m_l_p = D6
# dm_m_l_p = D7
# sm_m_r_p = D8
# dm_m_r_p = D9
# sm_b_l_p = D10
# dm_b_l_p = D11
# sm_b_r_p = D12
# dm_b_r_p = D13
# =============================================================================

#Minus motors--Digital
# =============================================================================
# sm_f_l_n = D22
# dm_f_l_n = D23
# sm_f_r_n = D24
# dm_f_r_n = D25
# sm_m_l_n = D26
# dm_m_l_n = D27
# sm_m_r_n = D28
# dm_m_r_n = D29
# sm_b_l_n = D30
# dm_b_l_n = D31
# sm_b_r_n = D32
# dm_b_r_n = D33
# =============================================================================

#Potentiometers--Analog
#==============================================================================
# pr_f_l = A0
# pr_f_r = A1
# pr_m_l = A2
# pr_m_r = A3
# pr_b_l = A4
# pr_b_r = A5
# =============================================================================

# =========-=========-=========-=========-=========-=========-=========-
# Step 3: Initialise the board and all the pins to be used as mentioned in Step 2.
board = ArduinoMega(PORT)  # Initialising the Arduino Mega

it = util.Iterator(board)  # Initialising the iterator to read the data from the board.
it.start()  # Starting the iterator. These two lines are needed if you want to take inputs.

# initialise 12 non-PWM digital output pins for the minus sides of the 12 motors
sm_f_l_p = board.get_pin('d:2:p') 
dm_f_l_p = board.get_pin('d:3:p')
sm_f_r_p = board.get_pin('d:4:p')
dm_f_r_p = board.get_pin('d:5:p')
sm_m_l_p = board.get_pin('d:6:p')
dm_m_l_p = board.get_pin('d:7:p')
sm_m_r_p = board.get_pin('d:8:p')
dm_m_r_p = board.get_pin('d:9:p')
sm_b_l_p = board.get_pin('d:10:p')
dm_b_l_p = board.get_pin('d:11:p')
sm_b_r_p = board.get_pin('d:12:p')
dm_b_r_p = board.get_pin('d:13:p')

sm_f_l_n = board.get_pin('d:22:o') 
dm_f_l_n = board.get_pin('d:23:o')
sm_f_r_n = board.get_pin('d:24:o')
dm_f_r_n = board.get_pin('d:25:o')
sm_m_l_n = board.get_pin('d:26:o')
dm_m_l_n = board.get_pin('d:27:o')
sm_m_r_n = board.get_pin('d:28:o')
dm_m_r_n = board.get_pin('d:29:o')
sm_b_l_n = board.get_pin('d:30:o')
dm_b_l_n = board.get_pin('d:31:o')
sm_b_r_n = board.get_pin('d:32:o')
dm_b_r_n = board.get_pin('d:33:o')

pr_f_l = board.get_pin('a:54:i')
pr_f_r = board.get_pin('a:55:i')
pr_m_l = board.get_pin('a:56:i')
pr_m_r = board.get_pin('a:57:i') 
pr_b_l = board.get_pin('a:58:i') 
pr_b_r = board.get_pin('a:59:i') 

#





# initialise 12 PWM digital output pins for the plus sides of the 12 motors
# Do here similarly as the above example
#





# initialise 6 analog input pins for the potentiometer
# Do here similarly as the above example
#







