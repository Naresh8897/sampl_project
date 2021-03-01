word =str(input())
print("enter a word")
keywords = ("break","case","default","continue","defer","else","for","func","goto","if","map","range","return","struct","type","var")
if word in keywords:
    print(word +"  is a keyword. ")
else:
    print(word +" is not a keyword. ")