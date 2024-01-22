import board

import digitalio 


from kmk.modules.oneshot import OneShot




from kb import KMKKeyboard, isRight

from storage import getmount



from kmk.keys import KC

from kmk.modules.layers import Layers

from kmk.modules.split import Split, SplitSide, SplitType

from kmk.modules.mouse_keys import MouseKeys

from kmk.extensions.media_keys import MediaKeys

from kmk.handlers.sequences import simple_key_sequence





keyboard = KMKKeyboard()

keyboard.tap_time = 100



layers = Layers()



split_side = SplitSide.RIGHT if isRight else SplitSide.LEFT



# data_pin = board.GP2

data_pin = board.GP14 if split_side == SplitSide.LEFT else board.GP14



# data_pin2 = board.GP2 if split_side == SplitSide.LEFT else board.GP15


                 
        

split = Split(

#     split_side=split_side,

    split_type=SplitType.UART,
#     split_type=SplitType.BLE,

    split_flip=False,

    data_pin=data_pin,

#     data_pin2=data_pin2,
    
    uart_flip = True,
    
    use_pio = True,

)

keyboard.modules = [layers, split, MouseKeys(),OneShot()]





# Select line 

SEL_LINE = simple_key_sequence(

        (

                KC.END,

                KC.LSHIFT(KC.HOME)

        )

)






LOWER =KC.LT(1,KC.OS(KC.MO(1),tap_time=1000))

RAISE =KC.LT(2,KC.OS(KC.MO(2),tap_time=1000))



OS_LCTL = KC.OS(KC.LCTL, tap_time=None)
keyboard.keymap = [

    [  #QWERTY
                                           KC.RALT,			 KC.TAB,\

        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                        KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,\

        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                        KC.H,    KC.J,    KC.K,    KC.L, KC.BSPC,\

        KC.Z,    KC.X,    KC.C,    KC.V,    KC.COMM,                        KC.DOT,    KC.N, KC.M,  KC.B, KC.ESC,\

                          KC.LSFT,   LOWER,KC.SPACE,              		 KC.ENT,     RAISE,   KC.LCTL
                          

    ],

    [  #LOWER
                                           					       KC.RALT, 			KC.TAB,\

        KC.N1,          KC.N2,           KC.N3,           	 KC.N4,                KC.N5,                           KC.N6,      KC.N7,     KC.N8,     KC.N9,    KC.N0,\

        KC.LCTL(KC.A),  KC.LCTL(KC.S),   KC.LCTL(KC.RALT(KC.T)), KC.QUES,              KC.LCTL(KC.V),                   KC.N0,      KC.LEFT,   KC.UP,     KC.RIGHT, KC.DEL,\

        KC.LCTL(KC.Z),  KC.LCTL(KC.X),   KC.LCTL(KC.INSERT),     KC.LSFT(KC.INSERT),   KC.LCTL(KC.C),                   KC.GRAVE,   KC.LABK,   KC.DOWN,   KC.RABK,  KC.SLSH,\
 
                                         KC.LSFT,                KC.RALT,   KC.SPACE,                                      KC.ENT,      KC.TAB,    KC.LCTL

    ],

    [  #RAISE
                                              KC.RALT,			    KC.TAB,\

        KC.EXLM,   KC.AT, KC.HASH,  KC.DLR,   KC.PERC,                      KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,\

        KC.F2,     KC.F5,   KC.F9,  KC.QUOT,  KC.SCLN,                      KC.UNDS,  KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE,\

        KC.F12,    KC.F11,  KC.F10, KC.DQUO,  KC.COLON,                     KC.MINS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS,\

                                         KC.LSFT,                KC.RALT,   KC.SPACE,                                      KC.ENT,      KC.TAB,    KC.LCTL

    ]

]



if __name__ == '__main__':

    keyboard.go()

