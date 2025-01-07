import pygame

pygame.init()
pygame.display.set_caption('Движущийся круг 2')
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
screen2 = pygame.Surface(screen.get_size())
x1, y1, w, h = 0, 0, 100, 100
dx, dy = 0, 0
drawing = False  # режим рисования выключен
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (x1 <= x <= x1 + w) and (y1 <= y <= y1 + h):
                drawing = True  # включаем режим рисования
                # запоминаем координаты одного угла
                dx, dy = x1 - event.pos[0], y1 - event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP:

            drawing = False
        if event.type == pygame.MOUSEMOTION:
            # запоминаем текущие размеры
            if drawing:
                x1, y1 = event.pos[0] + dx, event.pos[1] + dy
    # рисуем на экране сохранённое на втором холсте
    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))
    pygame.draw.rect(screen, (0, 255, 0), ((x1, y1), (w, h)))
    pygame.display.flip()
pygame.quit()