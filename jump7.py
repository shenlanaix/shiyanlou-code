for i in range(1,101):            #从1到100循环
    if i//10 == 7 or i%10 == 7 :  #含数字7
        continue
    elif i%7 == 0:                #是7的倍数
        continue
    else:                         #其他数字
        print(i)                  #打印数字
