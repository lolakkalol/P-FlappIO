import pygame

class background:
    speed  = 10
    x, y   = 0, 0
    screen = None
    sprite = None

    def __init__(self, position, speed, sprite, screen):
        self.x, self.y = position
        self.speed     = speed
        self.sprite    = sprite
        self.screen    = screen

    def update(self):

        # 0, 410 and 820 is offsets to get the sprite to line up properly
        self.screen.blit(self.sprite, (0   + self.x, 0))
        self.screen.blit(self.sprite, (410 + self.x, 0))
        self.screen.blit(self.sprite, (820 + self.x, 0))

        if self.x <= -410: # Will check if the visible segment of the sprite is visible
            self.x = 0

        # Moves the sprites to the left
        self.x -= self.speed

class bird:
    x, y = 0, 0
    dead = False

    acceleration = 0
    speed        = 0
    maxFallSpeed = 0

    screen = None
    sprite = None

    def __init__(self, position, maxFallSpeed, acceleration, sprite, screen):
        self.x, self.y    = position
        self.maxFallSpeed = maxFallSpeed
        self.acceleration = acceleration
        self.sprite       = sprite
        self.screen       = screen

    def update(self):
        if self.dead == False:

            if self.speed < self.maxFallSpeed:
                self.speed += self.acceleration

            self.y += self.speed

        elif self.x > -51:
            self.x -= 10 # Need to be the speed of the pipes

        self.screen.blit(self.sprite, (self.x, self.y)) # Prints bird to screen

    def jump(self):
        self.speed = -15

class pipe:
    speed  = 0
    x, y   = 0, 0
    gap    = 200
    screen = None
    sprite = None

    def __init__(self, position, speed, sprite, screen):
        self.x, self.y = position
        self.speed     = speed
        self.sprite    = sprite
        self.screen    = screen

    def show(self):
        self.screen.blit( self.sprite, (self.x, self.y + (self.gap/2)) )                                     # Shows the bottom pipe
        self.screen.blit( pygame.transform.rotate( self.sprite, 180 ), (self.x, self.y-400 - (self.gap/2)) ) # Shows the top pipe

    def move(self):
        self.x -= self.speed

# --------------------------------------------- END OF CLASSES ------------------------------------------------------

pygame.init()

def collission(pipe, bird):

    # Checks if the bird hit the ground
    if bird.y >= 500-36:
        bird.dead = True

    # Checks if birds bottom left corner hit the bottom pipe
    if ( bird.y + 36 > pipe.y + (pipe.gap/2) ) and ((bird.x > pipe.x) and (bird.x < pipe.x + 60)):
        bird.dead = True

    # Checks if birds top left corner hit the bottom pipe
    if ( bird.y < pipe.y - (pipe.gap/2) ) and ( (bird.x > pipe.x) and (bird.x < pipe.x + 60) ):
        bird.dead = True

    # Checks if birds top right corner hit the bottom pipe
    if ( bird.y < pipe.y - (pipe.gap/2) ) and ( ((bird.x + 51 > pipe.x) and (bird.x + 51 < pipe.x + 60)) ):
        bird.dead = True

    # Checks if birds bottom right corner hit the bottom pipe
    if ( bird.y + 36 > pipe.y + (pipe.gap/2) ) and ((bird.x + 51 > pipe.x) and (bird.x + 51 < pipe.x + 60)):
        bird.dead = True

def movePipes(pipes, closestPipe):

    for pipe in pipes:
        pipe.move()
        pipe.show()

        if pipe.x < -60:
            pipe.x = 800

            if closestPipe[0] < 2:
                closestPipe[0] += 1
            else:
                closestPipe[0] = 0

def main():

    # Window settings
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("FlappIO")

    sBirdIcon = pygame.image.load("./images/birdicon.png")
    pygame.display.set_icon(sBirdIcon)
    # ----------------

    # Sprites
    sPipe = pygame.image.load("./images/pipe.png")
    sBird = pygame.image.load("./images/bird.png")
    sBackground = pygame.image.load("./images/background.png")
    # -------

    # Misc.
    clock = pygame.time.Clock()
    events = pygame.event.get()
    # -----

    # Temporary lines to be change
    bg = background((0, 0), 10, sBackground, screen)
    brd = bird((20, 250), 10, 1, sBird, screen)

    closestPipe = [1] # Creates a list so that the number is mutable
    closestPipe[0] = 0
    pipeSpeed = 5
    pipes = [ pipe( (860/3, 300), pipeSpeed, sPipe, screen ),
              pipe( (2*860/3, 300), pipeSpeed, sPipe, screen ),
              pipe( (860, 300), pipeSpeed, sPipe, screen )]
    # ------------------------

    # Game/window loop
    running = True
    while running:

        screen.fill((255, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    brd.jump()

        bg.update()                               # Updates background
        movePipes(pipes, closestPipe)             # Moves the pipes
        collission(pipes[ closestPipe[0] ], brd)  # Checks for collission between bird and the closest pipe
        brd.update()                              # Updates the birds posistion

        clock.tick(30)          # Sets the frame rate
        pygame.display.update() # Updates the window

if __name__ == "__main__":
    main()
