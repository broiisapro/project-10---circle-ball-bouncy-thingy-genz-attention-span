import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine: Colliding Balls")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Ball class
class Ball:
    def __init__(self, x, y, vx, vy, radius, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color

    def move(self):
        # Update position
        self.x += self.vx
        self.y += self.vy

        # Bounce off walls
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.vx = -self.vx
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.vy = -self.vy

    def collide(self, other):
        # Check for collision with another ball
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance < self.radius + other.radius:
            # Elastic collision logic
            self.vx, other.vx = other.vx, self.vx
            self.vy, other.vy = other.vy, self.vy

            # Increase speed
            self.vx *= 1.1
            self.vy *= 1.1
            other.vx *= 1.1
            other.vy *= 1.1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Create balls
balls = []
for _ in range(10):
    radius = random.randint(15, 30)
    x = random.randint(radius, WIDTH - radius)
    y = random.randint(radius, HEIGHT - radius)
    vx = random.uniform(-2, 2)
    vy = random.uniform(-2, 2)
    color = random.choice(COLORS)
    balls.append(Ball(x, y, vx, vy, radius, color))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw balls
    for ball in balls:
        ball.move()
        for other_ball in balls:
            if ball != other_ball:
                ball.collide(other_ball)
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
