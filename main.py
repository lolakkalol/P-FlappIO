import pygame

class background:
    x = 0
    y = 0
    speed = 0

    def __init__(self, x, y, speed, sBackground, screen):
        self.x     = x
        self.y     = y
        self.speed = speed

    def update(self):
        x = self.x

        screen.blit(sBackground, (0   - self.x, 0))
        screen.blit(sBackground, (410 - self.x, 0))
        screen.blit(sBackground, (820 - self.x, 0))

        if x >= 410:
            self.x = 0
        self.x += self.speed

class bird:
    x = 100
    y = 0
    speed = 0
    acceleration = 0
    maxSpeed = 0

    def __init__(self, acceleration, maxSpeed, sBird, screen):
            self.acceleration = acceleration
            self.maxSpeed     = maxSpeed

    def update(self):
        if self.speed < self.maxSpeed:
            self.speed += self.acceleration

        self.y     += self.speed

        screen.blit(sBird, (self.x, self.y))

    def jump(self):
        self.speed = -15

class pipe:
    pipeSpeed = 10
    x = 0
    y = 0
    gap = 100

    def __init__(self, x, y, pipeSpeed, sPipe, screen):
        self.x         = x
        self.y         = y
        self.pipeSpeed = pipeSpeed

    def show(self):
        screen.blit(sPipe, (self.x, self.y + (self.gap/2)))
        screen.blit( pygame.transform.rotate(sPipe, 180) , (self.x, self.y-400 - (self.gap/2)) )

    def move(self):
        self.x -= self.pipeSpeed

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("FlappIO")
clock = pygame.time.Clock()
events = pygame.event.get()

sBackground = pygame.image.load("./images/background.png")
sBird = pygame.image.load("./images/bird.png")
sPipe = pygame.image.load("./images/pipe.png")
sBirdIcon = pygame.image.load("./images/birdicon.png")

pygame.display.set_icon(sBirdIcon)

bg = background(0, 0, 10, sBackground, screen)
brd = bird(1, 5, sBird, screen)

pipes = [pipe(0, 300, 10, sPipe, screen), pipe(800/2, 300, 10, sPipe, screen), pipe(800, 300, 10, sPipe, screen)]

def colission():
    pass

def movePipes():

    for pip in pipes:
        pip.move()
        pip.show()

        if pip.x < -60:
            pip.x = 800

def gameLoop():

    running = True
    while running:

        screen.fill((255, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    brd.jump()
                elif event.key == pygame.K_a:
                    tmp -= 1

        bg.update()
        brd.update()
        movePipes()

        #print(pygame.key)

        #print(clock)
        clock.tick(60)
        pygame.display.update()

gameLoop()
