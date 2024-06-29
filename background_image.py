import pygame
pygame.init()

w_width = 700
w_height = 700
screen = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Adding Jump Logic")

# Creating object
x = 0
y = w_height - 50  # Start at the bottom of the screen
width = 50
height = 50
vel = 5

clock = pygame.time.Clock()

# Jump variables
is_jump = False
jump_count = 10

bg_img = pygame.image.load("images/bg_img.jpeg")
bg_img = pygame.transform.scale(bg_img,(w_width,w_height))


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < w_width - width:
        x += vel
    if not is_jump:
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < w_height - height:
            y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jump_count = 10
            is_jump = False

    # Ensuring the rectangle stays within the boundaries
    if x < 0:
        x = 0
    if x > w_width - width:
        x = w_width - width
    if y < 0:
        y = 0
    if y > w_height - height:
        y = w_height - height

    screen.blit(bg_img,(0,0))
    pygame.draw.rect(screen, "yellow", (x, y, width, height))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
