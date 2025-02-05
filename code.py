import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.layers import Layers

print("Starting")
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# Pines de filas y columnas corregidos
keyboard.row_pins = (
    board.GP1,  # Fila 1
    board.GP17,  # Fila 2
    board.GP18,  # Fila 3
    board.GP19,  # Fila 4
    board.GP20,  # Fila 5
    board.GP21,  # Fila 6
    board.GP22,  # Fila 7
    board.GP26,  # Fila 8
)
keyboard.col_pins = (
    board.GP2,   # Columna 1
    board.GP3,   # Columna 2
    board.GP4,   # Columna 3
    board.GP5,   # Columna 4
    board.GP6,   # Columna 5
    board.GP7,   # Columna 6
    board.GP8,   # Columna 7
    board.GP9,   # Columna 8
    board.GP10,  # Columna 9
    board.GP11,  # Columna 10
    board.GP12,  # Columna 11
    board.GP13,  # Columna 12
    board.GP14,  # Columna 13
    board.GP15,  # Columna 14
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap ajustado al teclado
keyboard.keymap = [
    # Capa base
    [
        KC.LSFT,  KC.V,   KC.TRNS,   KC.C,   KC.CAPS,   KC.RSFT,   KC.SCROLLLOCK,   KC.HOME,   KC.INS,   KC.PAUS,   KC.PGUP,  KC.DOT,  KC.COMM,  KC.B,  # Fila 1
        KC.TAB, KC.R,  KC.W,   KC.E,   KC.Q,   KC.P,   KC.LBRC,   KC.BSPC,   KC.RBRC,   KC.O,   KC.I,   KC.U, KC.Y,  KC.T,  # Fila 2
        KC.A,  KC.G,    KC.D,    KC.F,    KC.S,    KC.QUOT,    KC.TAB,    KC.UP,    KC.ENT,    KC.SCLN,    KC.L,    KC.K, KC.J, KC.H, # Fila 3
        KC.ESC, KC.F4,    KC.F2, KC.F3,    KC.F1, KC.F10, KC.F11, KC.PSCREEN,  KC.F12,  KC.F9, KC.F8, KC.F7, KC.F6,    KC.F5,    # Fila 4 
        KC.GRAVE, KC.N4,    KC.N2,    KC.N3,    KC.N1,    KC.N0,    KC.MINS,    KC.TRNS,    KC.EQL,    KC.N9,    KC.N8, KC.N7, KC.N6,         # Fila 5
        KC.N5, KC.NLCK,    KC.X,    KC.LALT,    KC.Z,    KC.BSLS,    KC.PENT,    KC.TRNS,    KC.END, KC.DEL,  KC.RALT, KC.PGDN, KC.SLSH,            # Fila 6
        KC.M, KC.N, KC.TRNS,  KC.P5, KC.APP,  KC.P6, KC.P8, KC.PMNS, KC.PSLS, KC.P7, KC.P4, KC.PPLS, KC.P1,        # Fila 7
        KC.P2,   KC.P3,   KC.PDOT,   KC.PAST,   KC.SPC,   KC.TAB,   KC.TRNS, KC.LCTL,  KC.TAB, KC.RCTL, KC.DOWN, KC.LEFT                       # Fila 8
    ],
]

if __name__ == '__main__':
    keyboard.go()
