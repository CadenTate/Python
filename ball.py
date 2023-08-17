import math

import pygame

# Define constants
WIDTH = 640
HEIGHT = 480
FPS = 60
RADIUS = 20
COLOR = (255, 255, 255)
GRAVITY = 0.5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball in a Sphere")
clock = pygame.time.Clock()


# Define Ball class
class Ball:
    def __init__(self, x, y, radius, color, gravity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.gravity = gravity
        self.vx = 0
        self.vy = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self, sphere):
        # Apply gravity
        self.vy += self.gravity

        # Update position
        self.x += self.vx
        self.y += self.vy

        # Check collision with sphere
        dx = self.x - sphere.x
        dy = self.y - sphere.y
        distance = math.sqrt(dx * dx + dy * dy)
        if distance < sphere.radius - self.radius:
            # Ball is inside sphere, move it to the surface
            angle = math.atan2(dy, dx)
            self.x = sphere.x + (sphere.radius - self.radius) * math.cos(angle)
            self.y = sphere.y + (sphere.radius - self.radius) * math.sin(angle)

            # Reflect velocity
            dot_product = (self.vx * dx + self.vy * dy) / distance
            self.vx = -2 * dot_product * dx / distance + self.vx
            self.vy = -2 * dot_product * dy / distance + self.vy

        # Check collision with walls
        if self.x - self.radius < 0:
            self.vx = abs(self.vx)
        elif self.x + self.radius > WIDTH:
            self.vx = -abs(self.vx)
        if self.y - self.radius < 0:
            self.vy = abs(self.vy)
        elif self.y + self.radius > HEIGHT:
            self.vy = -abs(self.vy)


# Define Sphere class
class Sphere:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)


# Create objects
sphere = Sphere(WIDTH / 2, HEIGHT / 2, 100, COLOR)
ball = Ball(WIDTH / 2, 0, RADIUS, COLOR, GRAVITY)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update objects
    ball.update(sphere)

    # Draw objects
    screen.fill((0, 0, 0))
    sphere.draw(screen)
    ball.draw(screen)
    pygame.display.flip()

    # Limit FPS
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
