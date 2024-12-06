import math as ma

def num2GermanStyle():
    ones=int(a[-1]) 
    tens=int(a[-2])

    hun = int(a[-3]) if a[-3] !=0 and len(a) >=3 else None

    thou= int(a[-5:-3]) if len(a) >=4 else None

    m = [' ','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    n = [' ','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    o = ones % 10 if ones !=0 else None
    t = (thou % 10) if thou is not None else None
    t1 = ma.floor(int(thou) / 10) if thou is not None else None
   
    p1 = f"{n[t]} {m[t1]} Thousand" if str(a[-4]) != '0' and thou is not None and len(a) > 4  else f"{m[t1]} Thousand" if str(a[-4]) == '0' and thou is not None and len(a) > 4 else f"{n[t]} Thousand" if thou is not None and len(a) == 4 else ''
 
    p2 = f"{n[hun]} hundred" if str(a[-3]) != '0' else ""
    p3 = f"{n[o]}" if o is not None else ""
    p4 = f"and {m[int(tens)]}" if str(a[-2]) != '0' else ""
    print(f"{p1} {p2} {p3}{p4}")
    

a = "90090"
if len(a) >= 4:
    if __name__ == '__main__':
        num2GermanStyle()

else:
   print( "Wrong Input")