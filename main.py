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
    dead = False

    def __init__(self, acceleration, maxSpeed, sBird, screen):
            self.acceleration = acceleration
            self.maxSpeed     = maxSpeed

    def update(self):
        if self.dead == False:

            if self.speed < self.maxSpeed:
                self.speed += self.acceleration

            self.y += self.speed

        elif self.x > -51:
            self.x -= 10

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

def collission(pipe, bird):
    if bird.y >= 500-36:
        bird.dead = True

    if ( bird.y + 36 > pipe.y + (pipe.gap/2) ) and ((bird.x > pipe.x) and (bird.x < pipe.x + 60)):
        bird.dead = True

    if ( bird.y < pipe.y - (pipe.gap/2) ) and ( (bird.x > pipe.x) and (bird.x < pipe.x + 60) ):
        bird.dead = True

    #if ( bird.y <pipe.y + (pipe.gap/2) ) and




    pygame.draw.circle(screen, (255,0,0), (bird.x, bird.y), 5)
    pygame.draw.circle(screen, (255,0,0), (int(pipe.x), int(pipe.y - (pipe.gap/2))), 5)


def movePipes(pipes, closestPipe):

    for pip in pipes:
        pip.move()
        pip.show()

        if pip.x < -60:
            pip.x = 800

            if closestPipe[0] < 2:
                closestPipe[0] += 1
            else:
                closestPipe[0] = 0

def gameLoop():

    bg = background(0, 0, 5, sBackground, screen)
    brd = bird(1, 5, sBird, screen)

    closestPipe = [1] #Just to make it mutable
    closestPipe[0] = 0
    pipes = [pipe(860/3, 300, 10, sPipe, screen), pipe(2*860/3, 300, 10, sPipe, screen), pipe(860, 300, 10, sPipe, screen)]

    running = True
    while running:

        screen.fill((255, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    brd.jump()

        bg.update()
        movePipes(pipes, closestPipe)
        collission(pipes[ closestPipe[0] ], brd)
        brd.update()
        print(closestPipe[0])

        clock.tick(0)
        print(clock)
        pygame.display.update()

gameLoop()
