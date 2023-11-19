def f(x):
    return (x * x * x )+ (4 * x**2 )- 10


baslangicDeger = 1
bitisDeger = 2
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