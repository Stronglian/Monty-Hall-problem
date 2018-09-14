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
#公用變數
frequency = 1000
door_amount = 3
door_car_npz = "door_car3_"+str(door_amount)+'_'+str(frequency)+".npy"
##是否重新算
#userInput = input("重新算 T/F:")
#if userInput in ['T', 't', 'True']:
#    userInput = True
#else:
#    userInput = False
#算
if door_car_npz not in os.listdir('./') or True:
    print('建表')
    #初始化，0~door_amount:門在哪(0沒1有車)，n-2(door_amount):使用者回答，n-1(door_amount+1):使用者換答案
    ansArr = np.zeros((frequency, door_amount+2))
    for i in range(frequency):
        #設門，固定順序
#        door_car = random.randint(0, door_amount-1)
        door_car = i%door_amount
        ansArr[i][door_car] = 1
#        print("car:", door_car, end=",")
        #參加者回答，隨機
        partiAns = random.randint(0, door_amount-1)
        ansArr[i][door_amount] =  partiAns
#        print("ans:", partiAns, end=",")
        
#        #主持人行為 but it is change user's reponse
#        tempLi = list(range(door_amount))
#        if door_car != partiAns:
#            
#            tempLi.remove(partiAns)
#            tempLi.remove(door_car)
#            hostAsk = random.choice(tempLi)
#        else:
#            tempLi.remove(door_car)
#            hostAsk = random.choice(tempLi)
##        print("host:", hostAsk, end=",")
        #參加者行為 - 改變答案，用二分法定義答案
#        tempLi_new = list(range(door_amount))
#        tempLi_new.remove(partiAns)
#        tempLi_new.remove(hostAsk)
#        partiNewAns = random.choice(tempLi_new)
        if partiAns != door_car:
            partiNewAns = door_car
        else:
            tempLi = list(range(door_amount))
            tempLi.remove(door_car)
            partiNewAns = random.choice(tempLi)
        
        
        ansArr[i][door_amount+1] = partiNewAns
        
#        print("ansN:", partiNewAns)
        #儲存
        np.save(door_car_npz, ansArr)
            
else:
    ansArr = np.load(door_car_npz)
    
#統計
print('Analysis')
getCarNum_noChange = 0
getCarNum_Change = 0
for i in range(frequency):
#    print(ansArr[i])
    ansTemp = ansArr[i][0:3]
    partiTemp = int(ansArr[i][door_amount])
    partiNewTemp = int(ansArr[i][door_amount+1])
    if ansTemp[partiTemp] ==1:
       getCarNum_noChange += 1
    if ansTemp[partiNewTemp] ==1:
       getCarNum_Change += 1
print('If no change:',  round(getCarNum_noChange/frequency, 3)*100, "%")
print('If change:',  round(getCarNum_Change/frequency, 3)*100, "%")