e=eval(input('enter english marks'))
h=eval(input('enter hindi marks'))
m=eval(input('enter maths marks'))
s=eval(input('enter science marks'))
g=eval(input('enter geography marks'))
ma=((e+h+m+s+g)/500)*100
if ma>75:
    print('o grade')
else:
    if ma>=60 and ma<75:
        print('a grade')
    else:
        if ma>=45 and ma<60:
            print('b grade')
        else:
            if ma>=35 and ma<45:
                print('c grade')
            else:
                if ma<35:
                    print('fail')
print('result',ma)
                    
                     
