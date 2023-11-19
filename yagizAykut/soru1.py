def f(x):
    return (x * x * x) - (2 * x **2) - 5


baslangicDeger = 2
bitisDeger = 4


x = f(baslangicDeger)
y = f(bitisDeger)



for i in range(4):
    if x * y < 0:
        
        
        
        x0 = (baslangicDeger + bitisDeger)/2
        y0 = f(x0)
        
        if y0 * x < 0:
            bitisDeger = x0
            
        elif y0 * y < 0:
            baslangicDeger = x0


print(x0)
print(y0)