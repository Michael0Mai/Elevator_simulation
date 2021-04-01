#coding=utf8

'''

在电梯里按要去的楼层,没有分上下,
在电梯外呼叫电梯分上下.
用一个数组 target_floors 记录一批人呼叫电梯或在电梯里按要去的楼层,
将 target_floors 合并到 self.next_floors 里进入电梯的候选楼层,
然后在 self.next_floors 里选出要去的楼层
'''

import time
import random

########################################################################
class Elevator:
    def __init__(self, position = 1, direct = 0):
        self.position = position #电梯的楼层
        self.direct = direct #电梯的运行方向 向上1,向下-1,停止0
        self.next_floors = []
        
    def run(self, target_floors):#每运行经过一层,就重新算一次目标楼层
        self.next_floors = self.next_floors + target_floors
        if self.next_floors != [] :
            self.schedule()
            print("全部目标楼层:%s" %self.next_floors)
            if self.position != self.next_floor[0]:#每次上下一层
                if self.direct == 1:
                    self.position = self.position + 1
                    if self.position == self.next_floor[0] and self.next_floor != self.find_max():
                        self.del_floor(self.next_floor) #到达就从列表删去目标楼层
                else:
                    self.position = self.position - 1
                    if self.position == self.next_floor[0] and self.next_floor != self.find_min():
                        self.del_floor(self.next_floor) #到达就从列表删去目标楼层                    
            else:
                if self.direct == 1:
                    if self.position == self.find_max()[0]:# 看是不是到达了请求的最高层
                        self.direct = -1#反方向运行电梯
                if self.direct == -1:
                    if self.position == self.find_min()[0]:
                        self.direct = 1#反方向运行电梯
                self.del_floor(self.next_floor) #到达就从列表删去目标楼层        
                
            print("现在在 %s 楼" %self.position)
            print("准备去 %s 楼" %self.next_floor[0])
            print("------------")            
            time.sleep(0.3)#电梯运到下一层要一点时间        
        if self.next_floors == []:
            print("没有人要搭电梯")
            print("==============")
            self.direct = 0
        
    def schedule(self):#规划运行方向
        if self.direct == 1:#如果电梯向上运行
            self.next_floor = self.find_higher()#找到下一个要停留的楼层
            if self.next_floor == [float("inf"), 0]:#如果没有更高的楼层需要去
                self.next_floor = self.find_max()# 去最高的呼叫下楼楼层接人
        elif self.direct == -1:#如果电梯向下运行
            self.next_floor = self.find_lower()   
            if self.next_floor == [0, 0]:#没有了向下的请求
                self.next_floor = self.find_min()# 去最低的呼叫上楼楼层接人
        else:#电梯停止时,去#最近的请求
            self.next_floor = self.find_nearest()
            if self.next_floor[0] > self.position:
                self.direct = 1
            elif self.next_floor[0] < self.position:
                self.direct = -1
            else:
                self.direct = 0
        
                
    def find_higher(self):# 寻找比当前楼层高的目标楼层中最矮的楼层
        mini = [float("inf"), 0]
        for i in self.next_floors:
            if i[1] == 1 or i[1] == 0:                
                if i[0] > self.position and i[0] < mini[0]:
                    mini = i
        return mini
    
    def find_max(self):#找到最高的呼叫楼层
        maxi = self.next_floors[0]
        for i in self.next_floors:
            if maxi[0] < i[0]:
                maxi = i
        return maxi
    
    def find_min(self):#找到最低的呼叫楼层
        mini = self.next_floors[0]
        for i in self.next_floors:
            if mini[0] > i[0]:
                mini = i
        return mini    
    
    def find_lower(self):# 寻找比当前楼层低的目标楼层中最高的楼层
        maxi = [0, 0] 
        for i in self.next_floors:
            if i[1] == -1 or i[1] == 0:
                if i[0] < self.position and i[0] > maxi[0]:
                    maxi = i
        return maxi
    
    def find_nearest(self):#找到最近的请求
        diff = float("inf")
        nearest = []
        for i in range(len(self.next_floors)):
            if diff > abs(self.position - self.next_floors[i][0]):
                diff = abs(self.position - self.next_floors[i][0])
                nearest = self.next_floors[i]
        return self.next_floors[i]
    
    def del_floor(self, target_floor):#删除目标楼层数组专用
        for floor in self.next_floors:#找出有人重复按的楼层
            if target_floor[0] == floor[0] and (target_floor[1] == 0 or target_floor[1] == floor[1]):
                self.next_floors.remove(floor)

  
 
            
##################################################################
def go_to_floors():#模拟不断有人按电梯
    #第一个数是的楼层,第二个数是方向:-1向下, 1向上, 0是在电梯里面按的,没有分上下
    #如果第二个数全部都是0,那么就是忽略了电梯外面的呼叫,相当于磁头调度算法
    for i in range(random.randint(0, 10)):#随机多的人按电梯
        if i > 8:#不让电梯超载, 加一个限制
            floor_list.append([random.randint(1, 40), random.randint(-1, 1)])#去随机楼层

elevator = Elevator()
while True:
    floor_list = []
    go_to_floors()
    elevator.run(floor_list)
    if elevator.direct == 1:
        print("上升")
    elif elevator.direct == -1:
        print("下降")
    else:
        print("停止")    

   