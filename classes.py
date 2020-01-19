class background:
    x = 0
    y = 0
    speed = 0

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def update():
        x = 0

        screen.blit(sBackground, (-backgroundPos,0))
        screen.blit(sBackground, (410-backgroundPos,0))
        screen.blit(sBackground, (820-backgroundPos,0))

        if backgroundPos >= 410:
            x = 0
            x += 1
