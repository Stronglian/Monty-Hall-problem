# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
三道門，其中一道後面有車
主持人一開始讓參賽者選一道門
主持人開啟一道沒有車且不是參賽者所說的一道門
參賽者決定是否改變答案
主持人公布正確與否
"""

import numpy as np
import random
import os
#公用變數
frequency = 1000
door_amount = 3
door_car_npz = "door_car_"+str(door_amount)+'_'+str(frequency)+".npy"
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
        #設門
        door_car = random.randint(0, door_amount-1)
        ansArr[i][door_car] = 1
        print("car:", door_car, end=",")
        #參加者回答
        ParticipantAns = random.randint(0, door_amount)
        ansArr[i][door_amount] =  ParticipantAns
        print("ans:", ParticipantAns, end=",")
        
        #主持人行為 but it is change user's reponse
        if door_car != ParticipantAns:
            
#        
#        tempLi = list(range(door_amount))
#        
##        del tempLi[door_car]
#        #delete the ans and participent ans
#        try:
#            tempLi.remove(str(ParticipantAns))
#        except:
#            print("", end="")
#        try:
#            tempLi.remove(str(door_car))
#        except:
#            print("", end="")
#        hostAsk = tempLi[random.randint(0, len(tempLi)-1)]
#        print("host:", hostAsk, end=",")
#        
#        #主持人行為影響參加者
#        tempLi_new = list(range(door_amount))
#        try:
#            tempLi_new.remove(str(ParticipantAns))
#        except:
#            print("", end="")
#        try:
#            tempLi_new.remove(str(hostAsk))
#        except:
#            print("", end="")
        #使用者新回應
        partiNewAns = tempLi[random.randint(0, len(tempLi_new)-1)]
        ansArr[i][door_amount+1] = partiNewAns
        print("ansN:", partiNewAns)
        #
        np.save(door_car_npz, ansArr)
else:
    ansArr = np.load(door_car_npz)
    
#統計
print('\nAnalysis')
getCarNum_noChange = 0
getCarNum_Change = 0
for i in range(frequency):
    if ansArr[i][door_amount] ==1:
       getCarNum_noChange += 1
    if ansArr[i][door_amount+1] ==1:
       getCarNum_Change += 1
print('If no change:',  (getCarNum_noChange/frequency)*100, "%")
print('If change:',  (getCarNum_Change/frequency)*100, "%")