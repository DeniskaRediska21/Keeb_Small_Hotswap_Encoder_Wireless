import board
import digitalio

from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.encoder import RotaryioEncoder


# VBus pin config
VBUS_PIN = board.VBUS_SENSE  # RPi Pico
# VBUS_PIN = board.GP29      # WeAct RP2040 + resistors on Piantor PCB

# split side detection using vbus sense
# vbus = digitalio.DigitalInOut(VBUS_PIN)
# vbus.direction = digitalio.Direction.INPUT
# isRight = False if vbus.value == True else False
# isRight = False


# alternate option: set side based on drive names
name = str(getmount('/').label)
isRight = True if name.endswith('R') else False

# GPIO to key mapping, Left
_KEY_CFG_LEFT = [
board.GP1,
board.GP7,board.GP9,board.GP11,board.GP19,board.GP16,
board.GP6,board.GP8,board.GP12,board.GP18,board.GP17,
board.GP5,board.GP10,board.GP13,board.GP21,board.GP22,
board.GP27,board.GP20,board.GP26,board.GP28
]

# GPIO to key mapping, Left
_KEY_CFG_RIGHT = [
board.GP22,
board.GP12,board.GP13,board.GP18,board.GP19,board.GP26,
board.GP5,board.GP10,board.GP17,board.GP20,board.GP27,
board.GP3,board.GP11,board.GP16,board.GP21,board.GP28,
board.GP0,board.GP4,board.GP1,board.GP9
]


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = [KeysScanner(
            pins = _KEY_CFG_RIGHT if isRight == True else _KEY_CFG_LEFT
        ),
        RotaryioEncoder(
            pin_a= board.GP7 if isRight == True else board.GP4,
            pin_b=board.GP8 if isRight == True else board.GP3,)
        ]



    coord_mapping = [
    			 0,   22,
         1,  2,  3,  4,  5,   23, 24, 25, 26, 27,
         6,  7,  8,  9, 10,   28, 29, 30, 31, 32,
        11, 12, 13, 14, 15,   33, 34, 35, 36, 37,
                16, 17, 18,   38, 39, 40, 
                19, 21, 20,   43, 42, 41
    ]

