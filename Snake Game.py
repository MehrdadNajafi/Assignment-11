import random
import time
import arcade

class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.GREEN
        self.speed = 3
        self.width = 16
        self.height = 16
        self.center_x = w // 2
        self.center_y = h // 2
        self.r = 8
        self.change_x = 0
        self.change_y = 0
        self.score = 0
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, arcade.color.GREEN)

    def move(self):
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
    
    def eat(self, object):
        if object == 'apple':
            self.score += 1
        
        elif object == 'pear':
            self.score += 2

        elif object == 'trap':
            self.score -= 1




class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.RED
        self.width = 16
        self.height = 16
        self.center_x = random.randint(5, w)
        self.center_y = random.randint(5, h)
        self.r = 8
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)

class Pear(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.YELLOW
        self.width = 16
        self.height = 16
        self.r = 8
        self.center_x = random.randint(5, w)
        self.center_y = random.randint(5, h)

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)

class Trap(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.DARK_BROWN
        self.width = 16
        self.height = 16
        self.r = 8
        self.center_x = random.randint(5, w)
        self.center_y = random.randint(5, h)

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)

class UpperWall(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.width = w
        self.center_x = w // 2
        self.center_y = h

class LowerWall(arcade.Sprite):
    def __init__(self, w):
        arcade.Sprite.__init__(self)
        self.width = w
        self.center_x = w // 2
        self.center_y = 0

class RightWall(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.width = 1
        self.height = h
        self.center_x = w
        self.center_y = h // 2

class LeftWall(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.width = 1
        self.height = h
        self.center_x = 0
        self.center_y = h // 2


class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 800, 600, 'Snake Game')
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(800, 600)
        self.apple = Apple(800, 600)
        self.pear = Pear(800, 600)
        self.trap = Trap(800, 600)
        self.upper_wall = UpperWall(800, 600)
        self.lower_wall = LowerWall(800)
        self.right_wall = RightWall(800, 600)
        self.left_wall = LeftWall(800, 600)
        self.walls_list = [self.upper_wall, self.lower_wall, self.right_wall, self.left_wall]
    
    def on_draw(self, massage = None):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.trap.draw()
        arcade.draw_text(text=f'Score: {self.snake.score}',start_x=0 ,start_y=600 - 50, width=800, font_size=20, align="center", color=arcade.color.BLACK)
        
    def on_update(self, delta_time: float):
        self.snake.move()
        
        for wall in self.walls_list:
            if arcade.check_for_collision(self.snake, wall):
                print('game over')
                exit()
        
        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat('apple')
            self.apple = Apple(800, 600)
            print(self.snake.score)

        elif arcade.check_for_collision(self.snake, self.pear):
            self.snake.eat('pear')
            self.pear = Pear(800, 600)
            print(self.snake.score)

        elif arcade.check_for_collision(self.snake, self.trap):
            self.snake.eat('trap')
            if self.snake.score <= 0:
                print('game over')
                exit()
            self.trap = Trap(800, 600)
            print(self.snake.score)
    
    def on_key_release(self, key, modifires):
        if key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1

        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

# class GameOver(arcade.View):
#     def __init__(self, w, h):
#         arcade.View.__init__(self)
#         self.color = arcade.color.BLACK
#         self.center_x = w // 2
#         self.center_y = h // 2
    
#     def draw(self):
#         arcade.set_background_color(arcade.color.ORANGE)
#         arcade.draw_text(text='game over',start_x=0 ,start_y=600 - 300, width=800, font_size=30, align="center", color=arcade.color.BLACK)
#         # arcade.draw_text('Game Over', self.center_x, self.center_y, self.color, 30, 30)


game = Game()
arcade.run()