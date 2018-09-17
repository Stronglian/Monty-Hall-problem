# -*- coding: utf-8 -*-
"""
題目:
    提霍爾悖論（Monty Hall problem）三門問題（Monty Hall problem）
三道門，其中一道後面有車
主持人一開始讓參賽者選一道門
主持人開啟一道沒有車且不是參賽者所說的一道門
參賽者決定是否改變答案
主持人公布正確與否
統計，換與不換的獲勝(得到車)機率差異
"""
"""
參考資料:
    list:
        https://www.douban.com/note/277146395/
    random:
        https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
    np.save:
        https://docs.scipy.org/doc/numpy/reference/generated/numpy.save.html
"""

import numpy as np
import random
import os

class MontyHallProblem():
    def __init__(self, reBuild = True):
        #公用變數
        self.frequency = 1002
        self.door_amount = 3
        self.door_car_npz = "MontyHallProblem_"+str(self.door_amount)+'_'+str(self.frequency)+".npy"
        self.reBuild = reBuild
    def makeTheTable(self):
        print('建表')
        #初始化，0~door_amount:門在哪(0沒1有車)，n-2(door_amount):使用者回答，n-1(door_amount+1):使用者換答案
        self.ansArr = np.zeros((self.frequency, self.door_amount+2))
        #設門，固定
        for i in range(self.frequency):
#            self.door_car = random.randint(0, self.door_amount-1)
            self.door_car = i % self.door_amount
            self.ansArr[i][self.door_car] = 1
    def ParticipantAns(self, i):
        self.partiAns = random.randint(0, self.door_amount-1)
        self.ansArr[i][self.door_amount] =  self.partiAns
    def HostPickUp(self, i):
        tempArr = self.ansArr[i][:self.door_amount].copy()
        tempList = list()
        for j, num in enumerate(tempArr):
            if num == 1:
                continue
            if j == self.partiAns:
                continue
            tempList.append(j)
#        print(tempArr, num, self.partiAns, tempList)
        self.hostAsk = random.choice(tempList)
    def ParticipantAns_Change(self, i):
        tempArr = self.ansArr[i][:self.door_amount].copy()
        tempList = list()
        for j, num in enumerate(tempArr):
            if j == self.partiAns or j == self.hostAsk:
                continue
            tempList.append(j)
        if len(tempList) != 1:
            print('ParticipantAns_Change')
        self.partiNewAns = random.choice(tempList)
        self.ansArr[i][self.door_amount+1] =  self.partiNewAns
    
    def Analysis_noChange(self):
        print('統計')
        self.getCarNum_noChange = 0
        for i in range(self.frequency):
        #    print(ansArr[i])
            ansTemp = self.ansArr[i][0:3]
            partiTemp = int(self.ansArr[i][self.door_amount])
            if ansTemp[partiTemp] ==1:
               self.getCarNum_noChange += 1
        print('If no change:',  round(self.getCarNum_noChange * 100 / float(self.frequency), 2), "%")
    def Analysis_change(self):
        print('統計')
        self.getCarNum_Change = 0
        for i in range(self.frequency):
        #    print(ansArr[i])
            ansTemp = self.ansArr[i][0:3]
            partiNewTemp = int(self.ansArr[i][self.door_amount+1])
            if ansTemp[partiNewTemp] ==1:
               self.getCarNum_Change += 1
        print('If change:',     round(self.getCarNum_Change   * 100 / float(self.frequency), 2), "%")
    def mainGame_noChange(self):
        if self.reBuild or (self.door_car_npz not in os.listdir('./')):
            self.makeTheTable()
            for i in range(self.frequency):
                self.ParticipantAns(i)
            np.save(self.door_car_npz, self.ansArr)
        else:
            self.ansArr = np.load(self.door_car_npz)
        self.Analysis_noChange()
    def mainGame_change(self):
        if self.reBuild or (self.door_car_npz not in os.listdir('./')):
            self.makeTheTable()
            for i in range(self.frequency):
                self.ParticipantAns(i)
                self.HostPickUp(i)
                self.ParticipantAns_Change(i)
            np.save(self.door_car_npz, self.ansArr)
        else:
            self.ansArr = np.load(self.door_car_npz)
        self.Analysis_change()

if __name__ == '__main__' :
    #是否重新算
#    userInput = input("重新算 T/F:")
#    if userInput in ['T', 't', 'True']:
#        userInput = True
#    else:
#        userInput = False
    print("如果不換")
    game1 = MontyHallProblem()
    game1.mainGame_noChange()
    
    print("如果換")
    game2 = MontyHallProblem()
    game2.mainGame_change()
    