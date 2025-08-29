import os
import socket
import pygame

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('multispeciesresearchcluster.ddnsfree.com', 19061))
#client_socket.connect(('127.0.0.0', 19061))
print("Connected to socket")

os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1" #Get input even if not focused on a pygame window
pygame.init()
joysticks = []
clock = pygame.time.Clock()
# screen = pygame.display.set_mode((300, 300))

pygame.joystick.init()
print(f"Detected {pygame.joystick.get_count()} joysticks")
joystick = pygame.joystick.Joystick(0)
joystick.init()

last_axis_0x = 0
last_axis_0y = 0
last_axis_1x = 0
last_axis_1y = 0

axis_threshold = 0.5


def send_socket_message(message):
    print("Sending message: "+message)
    client_socket.send(message.encode())

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEREMOVED:
            print("Joystick removed")
            joystick.quit()

        elif event.type == pygame.JOYDEVICEADDED:
            print("Joystick added")
            joystick = pygame.joystick.Joystick(0)
            joystick.init()

        if event.type == pygame.JOYAXISMOTION:

            # Handle joystick axis motion
            axis_0x, axis_0y = (joystick.get_axis(0), joystick.get_axis(1) )

            if axis_0x > axis_threshold and last_axis_0x < axis_threshold:
                send_socket_message(f"Joystick 0: X+")
            if axis_0x < -axis_threshold and last_axis_0x > -axis_threshold:
                send_socket_message(f"Joystick 0: X-")
            if (axis_0x < axis_threshold and last_axis_0x > axis_threshold) or (axis_0x > -axis_threshold and last_axis_0x < -axis_threshold):
                send_socket_message(f"Joystick 0: X")

            if axis_0y > axis_threshold and last_axis_0y < axis_threshold:
                send_socket_message(f"Joystick 0: Y+")
            if axis_0y < -axis_threshold and last_axis_0y > -axis_threshold:
                send_socket_message(f"Joystick 0: Y-")
            if (axis_0y < axis_threshold and last_axis_0y > axis_threshold) or (axis_0y > -axis_threshold and last_axis_0y < -axis_threshold):
                send_socket_message(f"Joystick 0: Y")

            last_axis_0x = axis_0x
            last_axis_0y = axis_0y

            axis_1x, axis_1y = (joystick.get_axis(2), joystick.get_axis(3) )

            if axis_1x > axis_threshold and last_axis_1x < axis_threshold:
                send_socket_message(f"Joystick 1: X+")
            if axis_1x < -axis_threshold and last_axis_1x > -axis_threshold:
                send_socket_message(f"Joystick 1: X-")
            if (axis_1x < axis_threshold and last_axis_1x > axis_threshold) or (axis_1x > -axis_threshold and last_axis_1x < -axis_threshold):
                send_socket_message(f"Joystick 1: X")

            if axis_1y > axis_threshold and last_axis_1y < axis_threshold:
                send_socket_message(f"Joystick 1: Y+")
            if axis_1y < -axis_threshold and last_axis_1y > -axis_threshold:
                send_socket_message(f"Joystick 1: Y-")
            if (axis_1y < axis_threshold and last_axis_1y > axis_threshold) or (axis_1y > -axis_threshold and last_axis_1y < -axis_threshold):
                send_socket_message(f"Joystick 1: Y")

            last_axis_1x = axis_1x
            last_axis_1y = axis_1y

        elif event.type == pygame.JOYBUTTONDOWN:
            print(event.button)
            # Handle button press
            if joystick.get_button(0):
                send_socket_message(f"Button down: 0")
            elif joystick.get_button(1):
                send_socket_message(f"Button down: 1")
            elif joystick.get_button(2):
                send_socket_message(f"Button down: 2")
            elif joystick.get_button(3):
                send_socket_message(f"Button down: 3")
            elif joystick.get_button(4):
                send_socket_message(f"Button down: 4")
            elif joystick.get_button(5):
                send_socket_message(f"Button down: 5")
            elif joystick.get_button(6):
                send_socket_message(f"Button down: 6")
            elif joystick.get_button(7):
                send_socket_message(f"Button down: 7")
            elif joystick.get_button(8):
                send_socket_message(f"Button down: 8")
            elif joystick.get_button(9):
                send_socket_message(f"Button down: 9")
            elif joystick.get_button(10):
                send_socket_message(f"Button down: 10")
            elif joystick.get_button(11):
                send_socket_message(f"Button down: 11")
            elif joystick.get_button(12):
                send_socket_message(f"Button down: 12")
        
        elif event.type == pygame.JOYBUTTONUP:
            # Handle button press
            print(event.button)
            if event.button == 0:
                send_socket_message(f"Button up: 0")
            elif event.button == 1:
                send_socket_message(f"Button up: 1")
            elif event.button == 2:
                send_socket_message(f"Button up: 2")
            elif event.button == 3:
                send_socket_message(f"Button up: 3")
            elif event.button == 4:
                send_socket_message(f"Button up: 4")
            elif event.button == 5:
                send_socket_message(f"Button up: 5")
            elif event.button == 6:
                send_socket_message(f"Button up: 6")
            elif event.button == 7:
                send_socket_message(f"Button up: 7")
            elif event.button == 8:
                send_socket_message(f"Button up: 8")
            elif event.button == 9:
                send_socket_message(f"Button up: 9")
            elif event.button == 10:
                send_socket_message(f"Button up: 10")
            elif event.button == 11:
                send_socket_message(f"Button up: 11")

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                send_socket_message(f"Key down: Up Arrow")
            elif event.key == pygame.K_DOWN:
                send_socket_message(f"Key down: Down Arrow")
            elif event.key == pygame.K_LEFT:
                send_socket_message(f"Key down: Left Arrow")
            elif event.key == pygame.K_RIGHT:
                send_socket_message(f"Key down: Right Arrow")