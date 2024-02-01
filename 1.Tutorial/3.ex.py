import pygame
import pygame_gui
from pygame_gui.core import ObjectID

pygame.init()
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("comment")
ui_manager = pygame_gui.UIManager((width, height), r"C:\theme.json")

white = (30,) * 3

title_label = pygame_gui.elements.UILabel(
    pygame.Rect(20, 40, 300, 30),
    "Exercise 1: comment",
    ui_manager,
    object_id=ObjectID(class_id='@title_label',
                       object_id='#title_label')
)

label = [
    pygame_gui.elements.UILabel(
        pygame.Rect(50, 100, 200, 30),
        "    This is a comment",
        ui_manager
    ),
    pygame_gui.elements.UILabel(
        pygame.Rect(50, 100+30, 200, 30),
        'print("Hello, World!")',
        ui_manager
    ),
]
input_text = pygame_gui.elements.UITextEntryLine(
    pygame.Rect(50, 100, 25, 30),
    ui_manager
)
ok_label = pygame_gui.elements.UILabel(
    pygame.Rect(50 + 25 + 200 + 5, 100, 50, 30),
    "ok",
    ui_manager,
    object_id=ObjectID(class_id='@ok_label',
                       object_id='#ok_label')
)
ok_label.visible = False
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0  # 60 FPS
    for event in pygame.event.get():
        ui_manager.process_events(event)
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.USEREVENT:
            text = event.dict['text']
            if text:
                text = text[-1]
            input_text.set_text(text)
            if text == '#':
                ok_label.visible = True
            else:
                ok_label.visible = False
    ui_manager.update(time_delta)

    screen.fill(white)
    ui_manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
