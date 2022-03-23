# Checked till line #66
# calpt is a dictionary containg 3 dictionaries 
# its structure will be like this:
# the_three_sensors = (f"sen{i+1}" for i in range(3))
# calpt**={
#     sensor_number:[
#         sensed_value(position) for position in 360 degree
#     ]
#     for sensor_number in the_three_sensors
# } 4 such calpt** dicts have to be saved in files for each motor

from pyfirmata import Arduino, util
import time

class Steering_Motor():
    def __init__(self, ID,  mp1, mp2, sp1, sp2, sp3, calpt): # Initializing this class!
        '''
        Defining general properties of steering motors!
            We are assuming that the sensors are parts of the motors!
            
        ID is to define which leg we are talking about!
        ID consists of 2 letters:-
        ID letter 1 :- F = Front, B = Back
        ID letter 2 :- L = Left, R = Right

        "calpt" is the value of the sensor 1 (among the 3),
        when the wheel is @ zero degrees
        as described in calibration file! (which will be created soon)
        '''
        self.ID = ID # string
        
        self.mp1 = mp1 # Motor Pin 1, positive terminal (according to convension defined)
        self.mp2 = mp2 # Motor Pin 2, negative terminal (see ""../Conventions and Assumptions.txt" file)
        
        self.ms1 = 0 # State (0/1) of mp1 (motor state 1)
        self.ms2 = 0 # State (0/1) of mp1 (motor state 2)
        
        self.sp1 = sp1 # First Sensor is attached to this pin
        self.sp2 = sp2 # Second Sensor is attached to this pin
        self.sp3 = sp3 # Third Sensor is attached to this pin
        
        self.calpt = calpt # Let me understand then I will write what this is (till then read line 2)


    def status(self):
        '''
        A quiet unnecessary function except for debugging:
			Method to know the state of the motor!
			Call this when you want to know where each leg is.
			This doesn't return things, it only prints
        '''
        if self.ms1 == 1 and self.ms2 == 0: print(self.ID + " Motor is Moving Anticlockwise!")
        elif self.ms1 == 0 and self.ms2 == 1: print(self.ID + " Motor is Moving Clockwise!")
        else: print(self.ID + " Motor is NOT moving!")


    def calibrate(self, sPos): # Calculation of RPM is included
        '''Method to calibrate the motors'''
        last = 0            # To find the slope at the point described in line 117
        flag = 0            # Refer to line 152 to understand!
        
        # Deleting existing values and also keeps us on the safe side if didn't exist in the first place
        self.calpt = {f"sen{i+1}":[None]*360 for i in range(3)}
        
        # Starting the motor in anticlockwise direction:-
        board.digital[self.mp1].write(1)
        self.ms1 = 1
        board.digital[self.mp2].write(0)
        self.ms2 = 0

        if ID == "fl": sen1 = senfl1
        if ID == "fr": sen1 = senfr1
        if ID == "bl": sen1 = senbl1
        if ID == "br": sen1 = senbr1
        while len(sen1) <= 360:
            # Reading the sensors :-
            s1 = board.analog[self.sp1].read()
            s2 = board.analog[self.sp2].read()
            s3 = board.analog[self.sp3].read()
                
            # To start Recording the read values from a certain point!
            if flag == 0 and s1 > last and s1 == calpt: # To fint that certain point described at line 150
                flag = 1            # Refer to line 92 to understand!
                last = s1
                start = time.time()
                print("Started Recording!")

            # That certain point has been found, now we should start recording!
            if flag == 1:
                if ID == "fl":
                    senfl1.append(s1)
                    senfl2.append(s2)
                    senfl3.append(s3)
                if ID == "fr":
                    senfr1.append(s1)
                    senfr2.append(s2)
                    senfr3.append(s3)
                if ID == "bl":
                    senbl1.append(s1)
                    senbl2.append(s2)
                    senbl3.append(s3)
                if ID == "br":
                    senbr1.append(s1)
                    senbr2.append(s2)
                    senbr3.append(s3)
                # print("\nAt " + str(sen1.index(s1)) + " degree sensor 1 = " + str(s1) + ", sensor 2 = " + str(s2) + ", sensor 3 = " + str(s3) +".")

                if ID == "fl": RPM = RPMfl
                if ID == "fr": RPM = RPMfr
                if ID == "bl": RPM = RPMbl
                if ID == "br": RPM = RPMbr
                wait = 500/(3*RPM)
                time.sleep(wait/1000)

        end = time.time()
        taken = end - start
        RPM = 60/taken
        if ID == "fl": RPMfl = RPM
        if ID == "fr": RPMfr = RPM
        if ID == "bl": RPMbl = RPM
        if ID == "br": RPMbr = RPM
        print("Recorded!")

        # Stopping the motors when calibration is done
        #       Making the positive terminal low
        if ID == "fl" or ID == "fr":
            boardf.digital[mp1].write(0)
            if ID == "fl": msfl1 = 0
            if ID == "fr": msfr1 = 0
        if ID == "bl" or ID == "br":
            boardb.digital[mp1].write(0)
            if ID == "bl": msbl1 = 0
            if ID == "br": msbr1 = 0
        #       Making the negative terminal low
                # There is no need for the next 8 lines because this pin is already low,
                # but I am writing them just for adverse conditions!
        if ID == "fl" or ID == "fr":
            boardf.digital[mp2].write(0)
            if ID == "fl": msfl2 = 0
            if ID == "fr": msfr2 = 0
        if ID == "bl" or ID == "br":
            boardb.digital[mp2].write(0)
            if ID == "bl": msbl2 = 0
            if ID == "br": msbr2 = 0


    def current_position(self, ID):
        '''Method to know the current position of the wheel!'''
        # Telling it to take input from which sensor for which leg
        if ID == "fl" or ID == "bl":
            sp1 = "A0"
            sp2 = "A1"
            sp3 = "A2"
        if ID == "fr" or ID == "br":
            sp1 = "A3"
            sp2 = "A4"
            sp3 = "A5"
        # Taking the input!
        if ID == "fl" or ID == "fr":
            s1 = boardf.analog[sp1].read()
            s2 = boardf.analog[sp2].read()
            s3 = boardf.analog[sp3].read()
        if ID == "bl" or ID == "br":
            s1 = boardb.analog[sp1].read()
            s2 = boardb.analog[sp2].read()
            s3 = boardb.analog[sp3].read()

        if ID == "fl":
            sen1 = senfl1
            sen2 = senfl2
            sen3 = senfl3
        if ID == "fr":
            sen1 = senfr1
            sen2 = senfr2
            sen3 = senfr3
        if ID == "bl":
            sen1 = senbl1
            sen2 = senbl2
            sen3 = senbl3
        if ID == "br":
            sen1 = senbr1
            sen2 = senbr2
            sen3 = senbr3

        for i in range(360):
            if s1 in range(sen1[i]-1, sen1[i]+2):
                if s2  in range(sen2[i]-1, sen2[i]+2):
                    if s3  in range(sen3[i]-1, sen3[i]+2):
                        # print("Position of the wheel is " + str(i) + " degree!")
                        return i

def SMgoto(ID, f):          # "f" denotes final position
    '''Function to take the wheel to a specific position'''
    ID = Steering_Motor(ID)
    for i in range(3):
        i = ID.current_position()
        if f < i:
            if ID == "fl" or ID == "fr":
                boardf.digital[mp1].write(1)
                if ID == "fl": msfl1 = 1
                if ID == "fr": msfr1 = 1
            if ID == "bl" or ID == "br":
                boardb.digital[mp1].write(1)
                if ID == "bl": msbl1 = 1
                if ID == "br": msbr1 = 1

            if ID == "fl" or ID == "fr":
                boardf.digital[mp2].write(0)
                if ID == "fl": msfl2 = 0
                if ID == "fr": msfr2 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp2].write(0)
                if ID == "bl": msbl2 = 0
                if ID == "br": msbr2 = 0

            if ID == "fl": RPM = RPMfl
            if ID == "fr": RPM = RPMfr
            if ID == "bl": RPM = RPMbl
            if ID == "br": RPM = RPMbr
            time.sleep((500*(i-f))/(3*RPM))

            if ID == "fl" or ID == "fr":
                boardf.digital[mp1].write(0)
                if ID == "fl": msfl1 = 0
                if ID == "fr": msfr1 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp1].write(0)
                if ID == "bl": msbl1 = 0
                if ID == "br": msbr1 = 0
            if ID == "fl" or ID == "fr":
                boardf.digital[mp2].write(0)
                if ID == "fl": msfl2 = 0
                if ID == "fr": msfr2 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp2].write(0)
                if ID == "bl": msbl2 = 0
                if ID == "br": msbr2 = 0
        if f > i:
            if ID == "fl" or ID == "fr":
                boardf.digital[mp2].write(1)
                if ID == "fl": msfl2 = 1
                if ID == "fr": msfr2 = 1
            if ID == "bl" or ID == "br":
                boardb.digital[mp2].write(1)
                if ID == "bl": msbl2 = 1
                if ID == "br": msbr2 = 1
            if ID == "fl" or ID == "fr":
                boardf.digital[mp1].write(0)
                if ID == "fl": msfl1 = 0
                if ID == "fr": msfr1 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp1].write(0)
                if ID == "bl": msbl1 = 0
                if ID == "br": msbr1 = 0

            if ID == "fl": RPM = RPMfl
            if ID == "fr": RPM = RPMfr
            if ID == "bl": RPM = RPMbl
            if ID == "br": RPM = RPMbr
            time.sleep((500*(f-i))/(3*RPM))

            if ID == "fl" or ID == "fr":
                boardf.digital[mp1].write(0)
                if ID == "fl": msfl1 = 0
                if ID == "fr": msfr1 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp1].write(0)
                if ID == "bl": msbl1 = 0
                if ID == "br": msbr1 = 0
            if ID == "fl" or ID == "fr":
                boardf.digital[mp2].write(0)
                if ID == "fl": msfl2 = 0
                if ID == "fr": msfr2 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp2].write(0)
                if ID == "bl": msbl2 = 0
                if ID == "br": msbr2 = 0

def SMmove(ID, angle, direction):   # Direction can take 2 values, "c" and "ac"! (clockwise/anticlockwise)
    '''
    Function to move the wheel in some specific
    direction, for some some specific angle!
    '''
    ID = Steering_Motor(ID)
    for i in range(3):
        if direction == "c":
            if ID == "fl" or ID == "fr":
                boardf.digital[mp1].write(1)
                if ID == "fl": msfl1 = 1
                if ID == "fr": msfr1 = 1
            if ID == "bl" or ID == "br":
                boardb.digital[mp1].write(1)
                if ID == "bl": msbl1 = 1
                if ID == "br": msbr1 = 1

            if ID == "fl" or ID == "fr":
                boardf.digital[mp2].write(0)
                if ID == "fl": msfl2 = 0
                if ID == "fr": msfr2 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp2].write(0)
                if ID == "bl": msbl2 = 0
                if ID == "br": msbr2 = 0

            if ID == "fl": RPM = RPMfl
            if ID == "fr": RPM = RPMfr
            if ID == "bl": RPM = RPMbl
            if ID == "br": RPM = RPMbr
            time.sleep((500*angle)/(3*RPM))

            if ID == "fl" or ID == "fr":
                boardf.digital[mp1].write(0)
                if ID == "fl": msfl1 = 0
                if ID == "fr": msfr1 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp1].write(0)
                if ID == "bl": msbl1 = 0
                if ID == "br": msbr1 = 0
            if ID == "fl" or ID == "fr":
                boardf.digital[mp2].write(0)
                if ID == "fl": msfl2 = 0
                if ID == "fr": msfr2 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp2].write(0)
                if ID == "bl": msbl2 = 0
                if ID == "br": msbr2 = 0
        if direction == "ac":
            if ID == "fl" or ID == "fr":
                boardf.digital[mp2].write(1)
                if ID == "fl": msfl2 = 1
                if ID == "fr": msfr2 = 1
            if ID == "bl" or ID == "br":
                boardb.digital[mp2].write(1)
                if ID == "bl": msbl2 = 1
                if ID == "br": msbr2 = 1
            if ID == "fl" or ID == "fr":
                boardf.digital[mp1].write(0)
                if ID == "fl": msfl1 = 0
                if ID == "fr": msfr1 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp1].write(0)
                if ID == "bl": msbl1 = 0
                if ID == "br": msbr1 = 0

            if ID == "fl": RPM = RPMfl
            if ID == "fr": RPM = RPMfr
            if ID == "bl": RPM = RPMbl
            if ID == "br": RPM = RPMbr
            time.sleep((500*angle)/(3*RPM))

            if ID == "fl" or ID == "fr":
                boardf.digital[mp1].write(0)
                if ID == "fl": msfl1 = 0
                if ID == "fr": msfr1 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp1].write(0)
                if ID == "bl": msbl1 = 0
                if ID == "br": msbr1 = 0
            if ID == "fl" or ID == "fr":
                boardf.digital[mp2].write(0)
                if ID == "fl": msfl2 = 0
                if ID == "fr": msfr2 = 0
            if ID == "bl" or ID == "br":
                boardb.digital[mp2].write(0)
                if ID == "bl": msbl2 = 0
                if ID == "br": msbr2 = 0

# The name of the ports for the Arduino Boards to be plugged in
port = "com7"          # Port for the arduino for the two front wheels

# Initializing the 2 arduino boards
board = Arduino(port)
itf = util.Iterator(board)
itf.start()

# Defining Motor Pins:-
# "mp" denotes "motor pins",
# "ms" denotes "motor pin state(0/1)"
msfl1 = 0           # Motor State Front Left positive end (see convensions file)
msfl2 = 0           # Motor State Front Left negative end (see convensions file)

msfr1 = 0           # Motor State Front Right positive end
msfr2 = 0           # Motor State Front Right negative end

msbl1 = 0           # Motor State Back Left positive end
msbl2 = 0           # Motor State Back Left negative end

msbr1 = 0           # Motor State Back Right positive end
msbr2 = 0           # Motor State Back Right negative end

# # Store Calibration Info In Lists
# senfl1 = []         # Sensor Values for Front Left leg sensor 1
# senfl2 = []         # Sensor Values for Front Left leg sensor 2
# senfl3 = []         # Sensor Values for Front Left leg sensor 3

# senfr1 = []         # Sensor Values for Front Right leg sensor 1
# senfr2 = []         # Sensor Values for Front Right leg sensor 2
# senfr3 = []         # Sensor Values for Front Right leg sensor 3

# senbl1 = []         # Sensor Values for Back Left leg sensor 1
# senbl2 = []         # Sensor Values for Back Left leg sensor 2
# senbl3 = []         # Sensor Values for Back Left leg sensor 3

# senbr1 = []         # Sensor Values for Back Right leg sensor 1
# senbr2 = []         # Sensor Values for Back Right leg sensor 2
# senbr3 = []         # Sensor Values for Back Right leg sensor 3


# read values of sensors from front left
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
board.analog[2].enable_reporting()

# read values of sensors from front right
board.analog[3].enable_reporting()
board.analog[4].enable_reporting()
board.analog[5].enable_reporting()

# read values of sensors from back left
board.analog[6].enable_reporting()
board.analog[7].enable_reporting()
board.analog[8].enable_reporting()

# read values of sensors from back right
board.analog[9].enable_reporting()
board.analog[10].enable_reporting()
board.analog[11].enable_reporting()


RPMfl = 6           # RPM for front Front Left leg
RPMfr = 6           # RPM for front Front Right leg
RPMbl = 6           # RPM for front Back Left leg
RPMbr = 6           # RPM for front Back Right leg

# These calpts are the previous knowledge of value of sensor 1, 2 and 3 when the wheel is at 0 degree position
# These are representative values for now. Will be replaced by actual values on reading from the calibration file (coming soon)
calptfl = [209, 550, 891]
calptfr = [209, 550, 891]
calptbl = [209, 550, 891]
calptbr = [209, 550, 891]

# def start(ID, calpt):
#     return Steering_Motor(ID, calpt)


# digital pwm pins 12 to 5 (inclusive) in descending order have been used as motor pins
# analog pins 0 to 11 (inclusive) in ascending order have been used as sensor pins (3 sensors/motor)
# Have the value of "calpt"s and put below (find it in the calibration file which will be created soon))
fl = Steering_Motor("fl", mp1 = 12, mp2 = 11, sp1 = 0, sp2 = 1, sp3 = 2, calpt = calptfl)
fr = Steering_Motor("fr", mp1 = 10, mp2 = 9, sp1 = 3, sp2 = 4, sp3 = 5, calpt = calptfr)
bl = Steering_Motor("bl", mp1 = 8, mp2 = 7, sp1 = 6, sp2 = 7, sp3 = 8, calpt = calptbl)
br = Steering_Motor("br", mp1 = 6, mp2 = 5, sp1 = 9, sp2 = 10, sp3 = 11, calpt = calptbl)

'''
if ID == "fl":
            mp1 = 12
            mp2 = 11
            sp1 = 0
            sp2 = 1
            sp3 = 2
            calpt = calptfl
        if ID == "fr":
            mp1 = 10
            mp2 = 9
            sp1 = 3
            sp2 = 4
            sp3 = 5
            calpt = calptfr
        if ID == "bl":
            mp1 = 8
            mp2 = 7
            sp1 = 0
            sp2 = 1
            sp3 = 2
            calpt = calptbl
        if ID == "br":
            mp1 = 6
            mp2 = 5
            sp1 = 3
            sp2 = 4
            sp3 = 5
            calpt = calptbr
'''


if __name__ == "__main__":
    fl = Steering_Motor("fl")
    fl.status()
    fl.calibrate()
    fl.status()