instring = "aBCdef..gh*ijkl mno pqrst/uvw x yz"
rdystring = ""
outstring = ""
a = 5
b = 9
x = 0


for i in range (0,len(instring)):
    if (instring[i]<"a" or instring[i]>"z") and instring[i]!=" ":
        if instring[i]>="A" and instring[i]<="Z":
            rdystring+=chr(ord(instring[i])+32)
    else:
        rdystring+=instring[i]


for i in range (0,len(rdystring)):
    if rdystring[i]==" ":
        outstring+="xwx"
    else:
        x = ord(rdystring[i])-97
        outstring+= chr(((a*x+b) % 26)+97)
        
deinstring = outstring
deoutstring = ""

i=0
while i<len(deinstring):
    if deinstring[i:(i+3)]=="xwx":
        deoutstring+=" "
        i+=3
    else:
        x=ord(deinstring[i])-97
        while x<b:
            x+=26
        while (x-b)%a!=0:
            x+=26
        
        x=int((x-b)/a)
        deoutstring+=chr(x+97)
        i+=1
#for i in range (0,len(deinstring)):
#    if deinstring[i:(i+3)]=="xwx":
#        deoutstring+=" "
#        i+=2
#    else:
#        x=ord(deinstring[i])-97
#        while x<b:
#            x+=26
#        while (x-b)%a!=0:
#            x+=26
#        
#        x=int((x-b)/a)
#        deoutstring+=chr(x+97)