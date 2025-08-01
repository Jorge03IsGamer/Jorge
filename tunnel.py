import pygame
import pyautogui
import sys
import time
import math

# Take real desktop screenshot using pyautogui
screenshot_image = pyautogui.screenshot()
screenshot_image = screenshot_image.resize((1366, 768))  # Resize to fit window
screenshot = pygame.image.fromstring(screenshot_image.tobytes(), screenshot_image.size, screenshot_image.mode)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("REAL Tunnel GDI Effect")
clock = pygame.time.Clock()

# Start timer
start_time = pygame.time.get_ticks()
duration = 3000  # 3 seconds
running = True

# Main loop
while running:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False

    if current_time - start_time >= duration:
        running = False

    # Time effect
    t = (current_time - start_time) / 1000.0
    angle = t * 100
    scale = 1 + math.sin(t * 5) * 0.5

    # Tunnel transform
    tunnel = pygame.transform.rotozoom(screenshot, angle, scale)
    rect = tunnel.get_rect(center=(1366 // 2, 768 // 2))
    screen.blit(tunnel, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
