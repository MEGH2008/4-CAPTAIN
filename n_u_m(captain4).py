from ast import pattern
from itertools import chain
import random
from unittest import result
import time
import sys

def game():
    Score=0
    print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("* Hello my friend. This game is the fourth series of 'numbers up mountain' games. Next: Choose the level you want to play. Then...... answer and get points!!!")
    print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")



    deg=int(input("* enter a Degree(1 to 10) : "))
    start = int(time.time())
    
    print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")

    if deg>=11 :
        print("* false ")
        sys.exit(0)
    if deg<=0:
        print("* false ")
        sys.exit(0)

    for i in range(1,deg+1):
        number1=random.randint(i*i,i*10)
        number2=random.randint(i*i,i*i*i+10)
        result=number1+number2
        print("*",number1,"+",number2)
        answer=int(input("* enter result : "))
        if result==answer:
            Score += i*7
        else:
            Score -= 4
            print("* result : ", result)

        print("* your Score: ",Score)
        print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")


    for j in range(1,deg+1):
        number1=random.randint(j*j,j*10)
        number2=random.randint(j,j*5)
        result=number1-number2
        print("*",number1,"-",number2)
        answer=int(input("* enter result : "))
        if result==answer:
            Score += j*5
        else:
            
            
            Score-=4
            print("* result : ", result)

        print("* your Score: ",Score)
        print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")

    for g in range(1,deg+1):
        number1=random.randint(g,g*3)
        number2=random.randint(g,g*2)
        
        result=number1*number2
        print("*",number1,"*",number2)
        answer=int(input("* enter result : "))
        if result==answer:
            Score += g*16
        else:
            Score -= 8
            print("* result : ", result)
        print("* your Score: ",Score)
        print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")

    for z in range(1,deg+1):
        result=random.randint(z,z+12)
        Coefficient=random.randint(z,z*3)
        number1=random.randint(z+2,(z*3)+20)
        number2=Coefficient*result-+number1
        print("*",Coefficient,"(x)",-+ number1,"=",number2)

        answer=int(input("* enter result x : "))
        if result==answer:
            Score+=z*13
        else:
            Score-=4
            print("* x : ", result)
        print("* your Score: ",Score)
        print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")

    for d in range(1,deg+1):
        Chance1=random.randint(d,d*4)
        Chance2=random.randint(d,d*3)
        Chance3=random.randint(d,d*2)
        Chance4=random.randint(d,d*10)
        Chance5=random.randint(d,d*5)
        

        print("*",Chance1,"+",Chance2,"*",Chance3,"-",Chance4,"+",Chance5," : ")
        result=Chance1+(Chance2*Chance3)-Chance4+Chance5
        answer=int(input("* enter result : "))
        if answer == result:
            Score+=d*40
        else:
            Score-=40
            
            print("* result : ",result)
        print("* your score : ",Score)
        print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")
 
    for c in range(1,deg+1):
        Specified=random.randint(1,15) 
        number=random.randint(c+2,c*2+5)
        pattern1=number+Specified
        pattern=number+Specified+Specified+Specified
        result=pattern+Specified
        print("*",number,",",pattern1,",",pattern1+Specified,",",pattern,", ...")
        answer=int(input("* enter Continue the pattern : "))
        if answer==result:
            Score+=c*12
        else:
            Score-=10
            
            print("* Continue the pattern : ",result)
        print("* your Score: ",Score)
        print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")


    run=(int(time.time())-start)
    
    print("* Run Time: ", run)
    
    print("* score= (score(one)/run time)")

    finished=(Score/run)+1
    print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("* Score = ", finished)
    print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("* 0 to 3: Very weak")
    print("* 3 to 5 : weak")
    print("* 5 to 7 : normal")
    print("* 7 to 9 : good")
    print("* 9 to 11: very good")
    print("* +12 : Genius!")
    print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")
    if finished<=3:
        print("* Your descriptive record: very weak")
    if 3<=finished<=5:
        print("* Your descriptive record:  weak")
    if 5<=finished<=7:
        print("* Your descriptive record:  normal")
    if 7<=finished<=9:
        print("* Your descriptive record:  good")
    if 9<=finished<=11:
        print("* Your descriptive record:  very good")
    if 12<=finished:
        print("* Your descriptive record:  GENIUS!!!!")
    print("* ----------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print()
    print("* programmer : mohammad erfan ghoroghchian in group 'the number up mountain'")
    print()
    print()





    exit2=input("* play gain ? (yes) : ") 

    if exit2=="yes":
        game()
        for i in range(1000):
            print()

 
game()

