import turtle 
import random
import time
# Screen setup
wn = turtle.Screen()
wn.title("REDSHIFT")
wn.setup(width=800, height=600)
wn.tracer(0)

score = 0
highscore = 0 

fragments = []

class Fragment(turtle.Turtle):
    def __init__(self, x, y, color):
        super().__init__(shape="square")
        self.penup()
        self.color(color)
        self.shapesize(0.2, 0.2) 
        self.goto(x, y)
        
        #==== RANDOM EXPLOSION VELOCITY ====

        self.dx = random.uniform(-1, 1)#INCREASE SPREAD
        self.dy = random.uniform(1, 3)# INCREASE UPWARD BURST
        self.gravity = -0.03 # GRAVITY
        self.life = 100 # LIFETIME

    def move(self):
        self.dy += self.gravity # Apply gravity
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)
        self.life -= 1
        current_size = (self.life / 60) * 0.2
        if current_size > 0:
            self.shapesize(current_size, current_size)
        if self.life <=0:
            self.hideturtle()

class GameItem:
    def __init__(self, shape, color, stretch_wid=1, stretch_len=1, x=0, y=0):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len)
        self.turtle.penup()
        self.turtle.goto(x, y)

class Player(GameItem):
    def __init__(self,x,y):
        super().__init__("square","black",x=x,y=y)
        self.speed = .75

    def move_up(self):
        y = self.turtle.ycor()
        if y < 287:
            y += self.speed
            self.turtle.sety(y)
    
    def move_down(self):
        y = self.turtle.ycor()
        if y > - 280:
            y -= self.speed
            self.turtle.sety(y)
    def move_left(self):
        x = self.turtle.xcor()
        if x > - 387:
            x-=self.speed
            self.turtle.setx(x)

    def move_right(self):
        x = self.turtle.xcor()
        if x < 380:
            x+=self.speed
            self.turtle.setx(x)
    def check_collision(self,other):
        player_x = self.turtle.xcor()
        player_y = self.turtle.ycor()
        enemy_x = other.turtle.xcor()
        enemy_y = other.turtle.ycor()

        #===== FIND PLAYERS EDGE ====
        player_width = (self.turtle.shapesize()[1] * 20) / 2
        player_height = (self.turtle.shapesize()[0] * 20) / 2
        
        # ==== FIND ENEMIES EDGE ====
        enemy_width = (other.turtle.shapesize()[1] * 20) / 2
        enemy_heigth = (other.turtle.shapesize()[0] * 20) / 2

        #==== CHECK COLLISION ====
        x_collision = abs(player_x - enemy_x) < (player_width + enemy_width - 2)
        y_collision = abs(player_y - enemy_y) < (player_height + enemy_heigth - 2)

        return x_collision and y_collision
    
    def explode(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        color = self.turtle.pencolor()

        for _ in range(15): 
            fragments.append(Fragment(x, y, color))

class Enemy(GameItem):
    def __init__(self):
        super().__init__("square","red")
        self.reset_position()

    def reset_position(self):
            side = random.choice(["top", "bottom", "left", "right"])
            
            thickness = 1
            wall_size = random.uniform(3, 12) 

            if side == "top":
                self.turtle.shapesize(stretch_wid=thickness, stretch_len=wall_size)
                self.turtle.goto(random.randint(-380, 380), 300)
                self.dx = 0
                self.dy = -random.uniform(0.1, 0.5)
                
            elif side == "bottom":
                self.turtle.shapesize(stretch_wid=thickness, stretch_len=wall_size)
                self.turtle.goto(random.randint(-380, 380), -300)
                self.dx = 0
                self.dy = random.uniform(0.1, 0.5)
                
            elif side == "left":
                self.turtle.shapesize(stretch_wid=wall_size, stretch_len=thickness)
                self.turtle.goto(-400, random.randint(-280, 280))
                self.dx = random.uniform(0.1, 0.5)
                self.dy = 0
                
            elif side == "right":
                self.turtle.shapesize(stretch_wid=wall_size, stretch_len=thickness)
                self.turtle.goto(400, random.randint(-280, 280))
                self.dx = -random.uniform(0.1, 0.5)
                self.dy = 0


    def move(self):
        global score,highscore
        speed_multi = 1 + (score/100)
        new_x = self.turtle.xcor() + (self.dx * speed_multi)
        new_y = self.turtle.ycor() + (self.dy * speed_multi)
    
        self.turtle.goto(new_x, new_y)


        # ==== CHECK FOR RESET ====
        if abs(self.turtle.xcor()) > 420 or abs(self.turtle.ycor()) > 320:
            self.reset_position()
            score += 1
            pen.clear()
            pen.write(f"SCORE: {score} HIGH SCORE: {highscore}", align="center", font=("Consolas", 24, "bold"))
            if score >= 100 and wn.bgcolor() != "#2c3e50":
                wn.bgcolor("#2c3e50")
            elif score >= 80 and wn.bgcolor() != "#00cc11":
                wn.bgcolor("#00cc11")
            elif score >= 60 and wn.bgcolor() != "#00ffff":
                wn.bgcolor("#00ffff")
            elif score >= 40 and wn.bgcolor() != "#ffb3b3":
                wn.bgcolor("#ffb3b3")
            elif score >= 20 and wn.bgcolor() != "#ffe5e5":
                wn.bgcolor("#ffe5e5")
            elif score < 20 and wn.bgcolor() != "white":
                wn.bgcolor("white")



#==== SCORE BOARD ====
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("SCORE: 0  HIGH SCORE: 0", align="center", font=("Consolas", 24, "bold"))

#==== KEY BINDINGS ====
keys = {"w": False, "s": False, "a": False, "d": False}

def press_w(): keys["w"] = True
def release_w(): keys["w"] = False

def press_s(): keys["s"] = True
def release_s(): keys["s"] = False

def press_a(): keys["a"] = True
def release_a(): keys["a"] = False

def press_d(): keys["d"] = True
def release_d(): keys["d"] = False


wn.listen()

wn.onkeypress(press_w, "w")
wn.onkeyrelease(release_w, "w")

wn.onkeypress(press_s, "s")
wn.onkeyrelease(release_s, "s")

wn.onkeypress(press_a, "a")
wn.onkeyrelease(release_a, "a")

wn.onkeypress(press_d, "d")
wn.onkeyrelease(release_d, "d")

player = Player(0,0)
enemies = [Enemy() for i in range(2)]

try:
    while True:
        wn.update()
        player.turtle.up()

        # ==== MOVE PLAYER ON KEY PRESS ====

        if keys["w"]:  player.move_up()
        if keys["s"]: player.move_down()
        if keys["a"]: player.move_left()
        if keys["d"]: player.move_right()

        #==== INCREASE DIFFICULTY ====

        if score < 20:
            pass  
        elif score < 40:
            if len(enemies) < 4:
                enemies.append(Enemy()) 
                enemies.append(Enemy())    
        elif score < 60:
            if len(enemies) < 6:
                enemies.append(Enemy()) 
                enemies.append(Enemy())     
        elif score < 80:
            if len(enemies) < 8:
                enemies.append(Enemy()) 
                enemies.append(Enemy())         
        elif score < 100:
            if len(enemies) < 10:
                enemies.append(Enemy()) 
                enemies.append(Enemy())       
        else:
            if len(enemies) < 12:
                enemies.append(Enemy()) 
                enemies.append(Enemy()) 

        #==== DEATH ANIMATION ====
        for fragment in fragments[:]: # Use a slice [:] to safely remove items while looping
            fragment.move()
            if fragment.life <= 0:
                fragments.remove(fragment)

        #==== ENEMY MOVEMENT ====
        for enemy in enemies:
            enemy.move()

            if player.check_collision(enemy):
                player.explode()
                if score > highscore:
                    highscore = score
                score = 0
                wn.bgcolor("white")
                for enemy in enemies:
                    enemy.turtle.hideturtle()
                enemies.clear()
                enemies = [Enemy() for i in range(2)]

                pen.clear()
                pen.write(f"SCORE: {score} HIGH SCORE: {highscore}", align="center", font=("Consolas", 24, "bold"))

                print("HIT RESET SCORE")
                player.turtle.goto(0,0)

        time.sleep(0.0001)
except:
    print("Game Closed.")
    exit()
