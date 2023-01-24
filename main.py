import os,pygame

pygame.font.init()

# Globle Vars & Conts

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
main_font = pygame.font.SysFont("comicsans", 35)
lost_font = pygame.font.SysFont("comicsans", 45)

# Global Functions
#detect collision between two objects
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


# Draw Screen UI
def draw_lives(lives):
    lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
    WIN.blit(lives_label, (10, 10))


def draw_level(level):
    level_label = main_font.render(f"level: {level}", 1, (255, 255, 255))
    WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))


def draw_lost():
    lost_label = lost_font.render(f"You Lost!", 1, (255, 255, 255))
    WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))


# Loading Assets
RED_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_green_small.png")) 
BLUE_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_blue_small.png"))  

# player Ship
YELLOW_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_yellow.png"))


# Lasers
RED_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_green.png"))    
BLUE_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_yellow.png"))        


# Background
BG = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))    