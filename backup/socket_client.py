import os
import socket
import pygame

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('multispeciesresearchcluster.freeddns.org', 9999))
print("Connected to socket")

os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1" #Get input even if not focused on a pygame window
pygame.init()
joysticks = []
clock = pygame.time.Clock()
screen = pygame.display.set_mode((300, 300))

# pygame.joystick.init()
# print(f"Detected {pygame.joystick.get_count()} joysticks")
# joystick = pygame.joystick.Joystick(0)
# joystick.init()


def send_socket_message(message):
    print("Sending message: "+message)
    client_socket.send(message.encode())


while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            # Handle joystick axis motion
            pass
        elif event.type == pygame.JOYBUTTONDOWN:
            # Handle button press
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                send_socket_message(f"Key down: Up Arrow")
            elif event.key == pygame.K_DOWN:
                send_socket_message(f"Key down: Down Arrow")
            elif event.key == pygame.K_LEFT:
                send_socket_message(f"Key down: Left Arrow")
            elif event.key == pygame.K_RIGHT:
                send_socket_message(f"Key down: Right Arrow")