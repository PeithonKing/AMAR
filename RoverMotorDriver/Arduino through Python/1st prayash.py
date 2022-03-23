# # from pyfirmata import Arduino, util
# # import time
# # board = Arduino('com7')
# # # board.digital[13].write(1)
# # # it = util.Iterator(board)
# # # it.start()
# # while True:
# # 	time.sleep()
# # 	board.analog[3].enable_reporting()
# # 	test=board.analog[3].read()
# # 	print(test)

# from pyfirmata import Arduino, util
from time import sleep
# board = Arduino('com7')
# it = util.Iterator(board)
# it.start()
# # pin = board.get_pin("d:11:p")
# board.analog[0].enable_reporting()
# # pin.write(0.6)
# while True:
#     print(board.analog[0].read())
#     sleep(1)

from pyfirmata import Arduino, util
board = Arduino('com7')
it = util.Iterator(board)
it.start()
board.digital[13].write(1)
board.analog[0].enable_reporting()

sleep(1)

while True:
    print(board.analog[0].read())