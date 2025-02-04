m,h=input().split()
m=float(m);h=float(h)
bmi=m/h/h
if bmi<18.5:
    print('Underweight')
elif bmi<24:
    print('Normal')
else:
    print('%g\nOverweight' %(bmi))