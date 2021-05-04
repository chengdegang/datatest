from random import choice

class Ramdomwalk:
    """生成随机漫步数据类"""

    def __init__(self,num_pionts=5000):
        self.num_points = num_pionts

        self.x_value = [0]
        self.y_value = [0]

    def fillwalk(self):
        """计算随机漫步的所有点"""
        while len(self.x_value) < self.num_points:
            """决定前进方向及距离"""
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_distance * x_direction
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            if x_step==0 or y_step==0:
                continue
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)
