#给出圆的半径，返回圆的面积

def get_area_of_circle():
    r=input('请输入r=')
    #convert string to int 
    r = float(r) 
    y=float(3.14)*r
    return y


#area = get_area_of_circle()
#print("面积是 %.2f" % area)

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
def pay():
    hour=input('输入时间=')
    rate=input('输入每小时多少钱=')
    hour=float(hour)
    rate=float(rate)
    pay1=hour*rate
    return pay1


#a=pay()

#print('Your weekly earning is %.2f' % a)

#Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
def display_table():#[1,6)
    for i in range(1,6):
        print(i ,(i)**0, (i)**1, (i)**2, (i)**3)

#display_table()
#

s = "I am enjoying this challenge\". \t I just wonder what is next."
print(s)