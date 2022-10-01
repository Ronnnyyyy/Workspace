#-----------------------------------------BASIC BMI CALCULATOR-----------------------------------------------------

'''def bmi(w,h):
    return  (w/(h*h))
wt=float(input("Enter your Weight(kg): "))
ht=float(input("Enter your Height(m): "))
a=bmi(wt,ht)
if a<18:
    print('You are Underweight \n BMI=' + str(a)[:5])
elif a>25:
    print('You are Overweight \n BMI=' + str(a)[:5])
else:
    print('You are Healthy \n BMI=' + str(a)[:5])'''

'''a=[2,7,1,65,43]
a.sort()

print(a)

a.reverse()
print(a)

rohit=[2, 4, 5, 9, 39]
print(rohit)

print(len(rohit))
print(rohit.index(9))

dic={}
print(type(dic))'''
##--------------------------------------------------------------------------------------------------------------------
#make a list(mutable)

''' listvar= [5, 3, 5, 3, "pikachu"]'''

#make a tuple(non mutable)

'''tupvar=(5, 3, "silver")'''

#make a set

'''setvar= {2, 3, 2, 3, "school"}

for item in setvar:

    print(item)'''

#make a dictionary

'''dictvar={"Rohit" : "python", "Prateek": "Java"}'''

#print a dict

'''print(dictvar["Prateek"])'''

#to check if item in a list is number or not

'''list_1=[45, "kelvin", 76, 89, 45.0, 2, 6, 'punneet']
for item in list_1:
    if type(item)==int:
        print("It is a number")
    elif type(item)==float:
        print("It is a Number")
    else:
        print("It is not a number")'''

#------------------------------------------------Number Guessing Game--------------------------------------------------
'''class numberGuessingGame:


    import random 
    #random number
    n=random.randint(1,10)
    print("-----------------------------------Welcome to Number Guessing game---------------------------------------- \n Guess the number from 1-10")
    def __init__(self):
        self.LOWER=1
        self.HIGHER=10
    def start(self):
        print()

#heart of the game

    chances=0
    while True:

        userinput=int(input("Enter the guessed number:  "))
        if userinput == n:
            print(f"Congratulations You got it in {chances+1} step{'s' if chances > 1 else ''}!")
            break
        elif userinput < n:
            print("Your number is less than the random number")
        else:
            print("Your number is greater than the random number")
        chances=chances+1

# Starting the game
numberGuessingGame=numberGuessingGame()
numberGuessingGame.start()'''

#---------------------------------------------------------------------------------------------------------------------


'''while True:
    i=int(input())
    if (i<100):
        continue

    else:
        print("conggo")  
        break'''


#-----------------------------------

#exception handling

'''try:
    o=int(input())
except:
    print('error input no. only')'''

#-----------------------------------

# f=open('opnfl.txt', 'r+')

# f.write('\n')
# # f.seek(0)
# # f.write('\n he is king')
# # content=f.read()
# # print(content)
# # f.seek(0)
# # print(content)
# f.write('')
# f.close()


#------------stone  paper  scissors---------------

# import random
# import time

# sps=['stone', 'paper', 'scissors']
# sps2=['paper', 'paper', 'stone']
# sps3=['paper', 'stone', 'scissors']

# cup=random.choice(sps)
# sup=random.choice(sps2)
# yup=random.choice(sps3)

# stone='s'
# paper='p'
# scissors='r'

# you=str(input('Enter your name:\n'))

# us=int(0)
# cs=int(0)

# round=1
# while round<4:
#     print('Round', round)
#     time.sleep(1)
#     up=str(input('Enter your weapon(s:stone, p:paper, r:scissors) \n:'))
#     time.sleep(1)
#     if up==stone:
#         print(f'{you} chose: stone \ncomputer chose: {cup}')
#         time.sleep(1)
#         if cup=='stone':
#             print('draw')
#         elif cup=='paper':
#             print('computer won')
#             cs=cs+1
#         else:
#             print(f'{you} won')
#             us=us+1
        
#     elif up==paper:
#         print(f'{you} chose: paper \ncomputer chose: {sup}')

#         if sup=='paper':
#             print('draw')
#         elif sup=='scissors':
#             print('computer won')
#             cs=cs+1
#         else:
#             print(f'{you} won')
#             us=us+1
        
#     elif up==scissors:
#         print(f'{you} chose: scissors \ncomputer chose: {yup}')

#         if yup=='scissors':
#             print('draw')
#         elif yup=='stone':
#             print('computer won')
#             cs=cs+1
#         else:
#             print(f'{you} won')
#             us=us+1
        
#     else:
#         print('Please a valid weapon')
#         continue
#     round=round+1
#     print('______________________')
# time.sleep(1)
# print(f'final score:\n{you}: {us}pts\ncomputer: {cs}pts')
# if us>cs:
#     print(f'{you} won')
# elif cs>us:
#     print('computer won')
# else:
#     print('draw')

#--------------------------------------------

'''
f=open('ppr.txt', 'r+')
f.write('prateeek')
f.seek(0)
content=f.read()
print(content)
f.close()'''

#--------------------------------------------

# add= lambda x,y: x+y
# s=add(4,9)
# print(s)

#--------------------------------------------
# import time
# print('Good Evening')
# nm=input('Enter your name: ')
# chance=1
# if nm=='rohit' :
#     time.sleep(1)
#     print("Congrats you are eligible for lottery\nyou have two chances to enter lucky number")
#     while chance<3:
#         time.sleep(1)
#         s=int(input('Enter your lucky number(1-9):\n'))
#         if s==7:
#             time.sleep(2)
#             print('Congo your redeem code is 7745')
#             time.sleep(2)
#             l=int(input('Enter redeem code: '))
#             if l==7745:
#                 print('Here is your $50')
#             else:
#                 print('Here is your $100')
            
           
#             break
#         elif s==2:
#             time.sleep(2)
            
#             print('Congo your redeem code is 2249')
#             p=int(input('Enter redeem code: '))
#             if p==7745:
#                 print('Here is your $50')
#             else:
#                 print('Here is your $100')
#         else:
#             print('Oops you didnt win')
        
#         chance=chance+1
#         break
# else:
#     print('Thankyou for visiting')
# time.sleep(2)



# print('\n\nDo come again :)')


#----------------------------------------------------------------

