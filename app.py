import random
import sys
import turtle
from settings import *


def gen_food():
    """
        每运行一次，就在窗口上生成一个食物，往foods列表中添加一个食物
    """
    x = random.randrange(-WIDTH//2, WIDTH//2, size)
    y = random.randrange(-HEIGHT//2, HEIGHT//2, size)
    food = (x, y, random.choice(colors))
    foods.append(food)

"""
turtle中键盘事件的处理
1、创建键盘处理函数
2、建立监听
3、关联键盘事件与键盘处理函数    
"""
def key_left():
    global direction_x, direction_y
    direction_x = -1
    direction_y = 0

def key_right():
    global direction_x, direction_y
    direction_y = 0
    direction_x = 1

def key_up():
    global direction_y, direction_x
    direction_y = 1
    direction_x = 0

def key_down():
    global direction_y, direction_x
    direction_y = -1
    direction_x = 0

def key_Q():
    global quit
    quit = True

def key_P():
    global pause
    pause = not pause

def init():
    """
        初始化
    """
    turtle.setup(WIDTH, HEIGHT)
    turtle.tracer(0)
    turtle.hideturtle()
    turtle.listen() # 2 创建监听
    # 3 关联事件与事件处理函数
    turtle.onkey(key_left, 'Left')
    turtle.onkey(key_right, 'Right')
    turtle.onkey(key_down, 'Down')
    turtle.onkey(key_up, 'Up')
    turtle.onkey(key_Q, 'Q')
    turtle.onkey(key_Q, 'q')
    turtle.onkey(key_P, 'p')
    turtle.onkey(key_P, 'P')

    for i in range(3):
        gen_food()

def draw_rect(x, y, s=size, clr='red'):
    turtle.up()
    turtle.goto(x, y)
    turtle.color(clr)
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(s)
        turtle.lt(90)
    turtle.end_fill()
    turtle.up()

def update_snake():
    global snake_pos
    headx = snake_pos[-1][0] + direction_x * speed
    heady = snake_pos[-1][1] + direction_y * speed
    snake_pos.append([headx, heady])
    snake_pos.pop(0)

def draw_foods():
    for food in foods:
        x, y, clr = food
        draw_rect(x, y, clr=clr)

def draw_snake():
    for pos in snake_pos:
        if pos == snake_pos[-1]:
            draw_rect(pos[0], pos[1], clr='black')
        else:
            draw_rect(pos[0], pos[1])

def draw_pause():
    turtle.goto(0,0)
    turtle.down()
    turtle.write('PAUSE', align='center', font=('Arial', 100, 'bold'))
    turtle.up()

def collision():
    global foods, score
    """监测蛇是否与食物碰撞"""
    eated = []
    sx, sy = snake_pos[-1]
    for food in foods:
        x, y, c = food
        if sx == x and sy == y:
            eated = x, y, c
            snake_pos.insert(0, [x, y])
            break
    if len(eated):
        foods.remove(eated)
        score += 1

def draw_score():
    turtle.up()
    turtle.goto(-WIDTH/2+20, HEIGHT/2-30)
    turtle.down()
    turtle.write('得分: '+str(score), align='left', 
                 font=('楷体', 14, 'normal'))
    turtle.up()

def run():
    global clock
    # 游戏的逻辑处理和画面更新
    turtle.clear()
    if pause:
        draw_pause()
    else:
        clock += 1
        # 每3秒生成一个食物
        if clock >= food_clock:
            clock = 0
            gen_food()

        collision()
        update_snake()

        draw_foods()
        draw_snake()
        draw_score()

    turtle.update() # 更新画面

    if quit:
        sys.exit(0)
    turtle.ontimer(run, 100)

def mainloop():
    run()
    turtle.done()

"""
1、增加死亡的条件
    - 撞墙
    - 撞自己了
2、增加生命数
3、增食物种类
    - 高级：吃了之后，增加生命
    - 负面：吃了之后，扣分的
4、增加关卡
    - 关卡地图设计（地图中有墙）
    - 关卡难度（通过地形设计）
5、其他内容

"""