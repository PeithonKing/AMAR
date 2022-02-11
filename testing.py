from pyfirmata import Arduino, util
board = Arduino("com7")

board.digital[10].write(1)
board.digital[9].write(0)
board.digital[11].write(1)
board.digital[8].write(1)
