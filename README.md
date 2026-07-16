# Musepad - Hackpad

Musepad is a four key macropad with a rotary encoder and an OLED display. It runs on KMK firmware and I learned so many new skills, from creating a PCB to coding with CircuitPython and KMK! Musepad is used to control media, specifically music, so the user doesn't have to break their focus to adjust which song is playing or change the volume.

# Features

CAD 3D Printed Case
128x32 OLED Display
EC11 Rotary encoder for volume control
4 Keys

Firmware of Musepad comes with following functions:
 - media control (prev track, pause track, next track)
 - Volume control (volume up and down with scroll knob, mute with a key)
 - Up, Down, Right and Left keys
 - Brightness Control (increase, decrease)

# CAD Model

The model has both the top and bottom parts combined in the assembly. I have also included the switches and encoder part, as well as a cutout for the USB-C plug.

<img width="556" height="478" alt="Screenshot 2026-07-16 181324" src="https://github.com/user-attachments/assets/d028876d-2904-4cba-8e87-d05ef6627fe0" />
<img width="802" height="564" alt="Screenshot 2026-07-16 181506" src="https://github.com/user-attachments/assets/be9f3644-8b99-4c9c-8e10-a3542008994f" />

# PCB

This is my PCB, made in KiCad.

Schematic!

<img width="918" height="634" alt="Screenshot 2026-07-16 182101" src="https://github.com/user-attachments/assets/20e22f49-8c36-48d4-bfa9-2b59398cba14" />


PCB!

<img width="840" height="674" alt="Screenshot 2026-07-16 181828" src="https://github.com/user-attachments/assets/77682bd8-dcfc-4bad-bb44-0a0b9d442ccd" />


3D PCB Model!

<img width="956" height="514" alt="Screenshot 2026-07-16 181853" src="https://github.com/user-attachments/assets/473e119c-78c0-42c0-a9ab-5ec928305736" />

# Firmware Overview
This hackpad uses KMK firmware for everything.

The rotary encoder changes volume. User can press to pause/play.
The 4 keys currently act as media controllers using the MediaKeys extension in KMK.
The OLED is a a homescreen that says "Saanvi's Musepad". YAY!


<img width="128" height="32" alt="base" src="https://github.com/user-attachments/assets/d26d8a21-69b0-4965-9551-41cf4d093778" />

# BOM
Here is everything I used to build my Musepad

4x Cherry MX Switches
4x DSA Keycaps
4x M3x5x4 Heatset inserts
4x 1N4148 DO-35 Diodes.
1x 0.91" 128x32 OLED Display
1x EC11 Rotary Encoder
1x XIAO RP2040
1x Case (2 3D printed parts!)
