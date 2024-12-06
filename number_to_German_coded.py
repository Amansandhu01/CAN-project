import math as ma
a = "77707"

def num2GermanStyle():
    ones=str(a[-1]) if a[-1] !=0 else None
    tens=str(a[-2])

    hun = str(a[-3]) if a[-3] !=0 and len(a) >=3 else None

    thou= str(a[-5:-3]) if len(a) >=4 else None

    m = [' ','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    n = [' ','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    o = int(ones) % 10
    h = int(hun)
    t = int(thou) % 10 if thou is not None else None
    t1 = ma.floor(int(thou) / 10) if thou is not None else None

    p1 = f"{n[t]} and {m[t1]} Thousand" if str(a[-4]) != '0' and thou is not None and len(a) > 4  else f"{n[t]} Thousand" if thou is not None and len(a) == 4 else ''
    #p2 = f"{m[t1]} Thousand" if thou is not None else ''
    p2 = f"{n[h]} hundred, " if str(a[2]) != '0' else ''
    p3 = f"and {m[int(tens)]}" if str(a[-2]) != '0' else ''

    print(f"{p1} {p2}{n[int(ones)]} {p3}" )

if len(a) >= 4:
    if __name__ == '__main__':
        num2GermanStyle()

else:
   print( "Wrong Input")