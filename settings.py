# 窗口相关
WIDTH = 400  # -WIDTH/2, WIDTH/2
HEIGHT = 400

# 系统相关
score = 0
size = 20
quit = False
pause = False
clock = 0  # 0 ~ 3秒之间
food_clock = 30
colors = ['pink', 'sky blue', 'yellow', 'gray']

# 蛇
snake_pos = [[0, 0]]
speed = size
direction_x = 1  # x方向运动， 0， 表示不动，1表示向右，-1向左
direction_y = 0  # y方向运动，0， 表示不动，1表示向上，-1向下


# 食物相关
foods = []
