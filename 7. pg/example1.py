import sys
from hexss import check_packages

check_packages(
    'pygame',
    auto_install=True, verbose=False,
)
import pygame

pygame.init()
pygame.display.set_caption("Pygame Example")
width, height = 800, 600
display = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

rect_width, rect_height = 50, 50
rect_x, rect_y = (width - rect_width) // 2, (height - rect_height) // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= 1
    if keys[pygame.K_RIGHT]:
        rect_x += 1
    if keys[pygame.K_UP]:
        rect_y -= 1
    if keys[pygame.K_DOWN]:
        rect_y += 1

    display.fill(WHITE)
    pygame.draw.rect(display, BLUE, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()

pygame.quit()
sys.exit()
