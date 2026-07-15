print("Starting")

import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.display.builtin import BuiltInDisplay


keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

# Define your matrix pins (adjust to match your wiring)
keyboard.col_pins = (board.D0, board.D1)
keyboard.row_pins = (board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define what each key does
keyboard.keymap = [
    [
    KC.MBRIU, 
    KC.MPRV,
    KC.MBRID, 
    KC.MNXT
    ],
]
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]

# Regular GPIO Encoder
encoder_handler.pins = (
    (board.D7, board.D8, board.D9),
)
encoder_handler.map = [ ( KC.VOLD, KC.VOLU, KC.MPLY) ]

# Replace display, sleep_command, and wake_command according to your hardware configuration.
driver = BuiltInDisplay(
    # Mandatory:
    display=board.DISPLAY,
    sleep_command=0xAE,
    wake_command=0xAF
)
i2c_bus = busio.I2C(board.D4, board.D5)

driver = SSD1306(
    # Mandatory:
    i2c=i2c_bus,
    # Optional:
)

# For all display types
display = Display(
    # Mandatory:
    display=driver,
    entries = [
        ImageEntry(image = "base.bmp", x = 0, y = 0)
    ]
)

keyboard.extensions.append(display)


if __name__ == "__main__":
    keyboard.go()