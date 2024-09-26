ss = "This is my dog. That is your dog. Where is her dog?"
print("Replace All:",ss.replace("dog","cat"))
print("Replace One:",ss.replace("dog","cat",1))
print("Replace Two:",ss.replace("dog","cat",2))
print()
s1 = "This is my {0}. That is your {1}."
s2 = "This is my {1}. That is your {0}."
s3 = "This is my {0}. That is your {0}."
s4 = "This is my {}. That is your {}."
print("With format('dog','cat')...)")
print(s1+" : "+s1.format("dog","cat"))
print(s2+" : "+s2.format("dog","cat"))
print(s2+" : "+s3.format("dog","cat"))
print(s2+" : "+s4.format("dog","cat"))
print()
s11 = "This is my {mypet}. That is your {yourpet}."
print("With format(mypet='dog',yourpet='cat')...)")
print(s11+" : "+s11.format(mypet="dog",yourpet="cat")) 
s12 = "This is my {0}. That is your {yourpet}."
print("With format('dog',yourpet='cat')...)")
print(s12 + " : " + s12.format("dog",yourpet="cat")) 
print()

def ffp(s):
    """ find first placeholder """
    start = s.find("{")
    if start >= 0:
        end = s.find("}")
        if end > 0:
            return "{:16}".format(s[start:end+1])
    return "<no placeholder>"            
s21 = "My score is {0}."
s22 = "My score is {0:6}."
s23 = "My score is {0:<6}."
s24 = "My score is {:.3f}."
s25 = "My score is {:.2%}."
myscore = 99
print("myscore is :",myscore)
print(ffp(s21),":",s21.format(myscore)) 
print(ffp(s22),":",s22.format(myscore))
print(ffp(s23),":",s23.format(myscore))
print(ffp(s24),":",s24.format(myscore))
print(ffp(s25),":",s25.format(myscore/100))
print()
s26 = "I have ${:,.2f}."
mymoney = 9999
print("mymoney is :",mymoney)
print(ffp(s26),":",s26.format(mymoney)) 
print()
s31 = "I have {:,.2f} Dollar"
mymoney = 100
print(s31.format(mymoney))
print("After buying breakfast...")
mymoney -= 30
print(s31.format(mymoney))
print()
print("Using a function to create f-string")
def showmymoney():
    return f"I have {mymoney:,.2f} Dollar"
mymoney = 100
print(showmymoney())
print("After buying breakfast...")
mymoney -= 30
print(showmymoney())
