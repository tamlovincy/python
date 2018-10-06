import math
def quadratic(a, b, c):
    if b**2-4*a*c>=0:
        
        x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2
    else:
        print('方程式','ax^2+bx+c=0','无实根')

print('二元一次方程为：ax^2+bx+c=0')
a=int(input('请输入a的值：'))
b=int(input('请输入b的值：'))
c=int(input('请输入c的值：'))
print('二元一次方程的解为：',quadratic(a,b,c))

