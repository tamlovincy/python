from functools import reduce
def str2float(s):
    def char2int(char):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[char]
    s1=s.split(".")[0]
    s2=s.split(".")[1][::-1]
    f1=reduce(lambda x,y:10*x+y,map(char2int,s1))
    f2=reduce(lambda x,y:x*0.1+y,map(char2int,s2))
    return f1+f2*0.1

print(str2float('123.456'))
