#number to word converter
#minase zerfu
#insa summer camp assigment
words={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"one", 2:"two",
              11:"eleven",12:"tweleve",13:"thriteen",14:"fourteen",15:"five",16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen",20:"twenty",
              30:"thrity",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninty",
              100:"one hundred"}
number=int(input("enter your number"))
if number<=1000:
 if number in words:
   a=words.get(number)
   print( number , "in words is", a)
else:
     m=num%10
     n=names.get(m)
     c = num // 10
     c=c*10
     c=names.get(c)
     result =c+b
     print((num, "in words is", result))

 



