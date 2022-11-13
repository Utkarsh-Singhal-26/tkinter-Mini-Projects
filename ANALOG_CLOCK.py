import pygame
import math
import time

#===== SCREEN SIZE =====
screen_width = 400
screen_height = 400

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ANALOG CLOCK")

#===== DRAW MARKINGS FUNCTION =====
def draw_markings():
    d1 = 100
    d2 = 10
    for i in range(0, 350, 30):
        x1 = screen_width // 2 + d1 * math.cos(math.radians(i))
        y1 = screen_height // 2 + d1 * math.sin(math.radians(i))

        x2 = x1 + d2 * math.cos(math.radians(i))
        y2 = y1 + d2 * math.sin(math.radians(i))

        pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 5)

#===== DRAW ARCS FUNCTION =====
def arc(center, radius, start, end, thickness, color):
    for i in range(start, end):
        x = center[0] + radius * math.cos(math.radians(i - 90))
        y = center[1] + radius * math.sin(math.radians(i - 90))
        
        pygame.draw.circle(screen, color, (int(x), int(y)), thickness)

#===== DRAW CLOCK HANDS FUNCTION =====
def clock_hand(center, radius, angle, thickness, color):
    x = center[0] + radius * math.cos(math.radians(angle - 90))
    y = center[1] + radius * math.sin(math.radians(angle - 90))

    pygame.draw.line(screen, color, center, (int(x), int(y)), thickness)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    #===== CALLING DRAW MARKINGS FUNCTION =====
    draw_markings()

    curr_time = time.strftime("%I%M%S", time.localtime(time.time()))
    s = int(curr_time[4]) * 10 + int(curr_time[5])
    m = int(curr_time[2]) * 10 + int(curr_time[3])
    h = int(curr_time[0]) * 10 + int(curr_time[1])

    #===== CALLING DRAW ARCS FUNCTION =====
    arc((screen_width // 2, screen_height //2), 180, 0, s * 6, 9, (0, 255, 0))
    arc((screen_width // 2, screen_height //2), 160, 0, m * 6, 9, (0, 0, 255))
    arc((screen_width // 2, screen_height //2), 140, 0, h * 30, 9, (255, 0, 0))

    #===== CALLING DRAW CLOCK HANDS FUNCTION =====
    clock_hand((screen_width // 2, screen_height // 2), 110, s * 6, 5, (0, 255, 0))
    clock_hand((screen_width // 2, screen_height // 2), 90, m * 6, 5, (0, 0, 255))
    clock_hand((screen_width // 2, screen_height // 2), 70, h * 6, 5, (255, 0, 0))

    pygame.display.update()