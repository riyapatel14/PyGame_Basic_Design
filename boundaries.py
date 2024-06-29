import pygame
pygame.init()

w_width = 500
w_height = 500
screen = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Adding boundaries")

# Creating object
x = 0
y = 0
width = 50
height = 50
vel = 5

clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel

    # Ensuring the rectangle stays within the boundaries
    if x < 0:
        x = 0
    if x > w_width - width:
        x = w_width - width
    if y < 0:
        y = 0
    if y > w_height - height:
        y = w_height - height

    screen.fill("white")
    pygame.draw.rect(screen, "black", (x, y, width, height))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
