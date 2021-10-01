#!/usr/bin/env python
# coding: utf-8

# In[1]:


lines = []
#user_input = input()

with open('A:\Github Materials\sampleinput.txt', 'r') as read:
    lines = read.readlines()


def decipher():
    emb=list(emblem)
    check1=0
    check2=len(emb)
    
    for i in word:
        count=0
        for j in emb:
            if i==j:
                emb.pop(count)
                check1=check1+1
                #break
            count=count+1   

    if check1==check2:
        print(cipher.kingdom)
       
    
        
def cipher():
    b=len(emblem)
    cipher.kingdom=words.pop(0)
    joint =''.join(words)
    z=[]
    numbers = []
    word = []
    for letter in joint:
        letter = letter.lower()
        number = ord(letter) - 96
        numbers.append(number)
    for i in numbers:
        c=i-b
        if c<=0:
            c=c+26
        z.append(c)
    for letter in z:
        number = (chr(letter+96))
        word.append(number)
    print(word)
    cipher.variable=word



def land():
    print("its land")
    cipher()
    
    

def air():
    print("its air")
    cipher()
    

def fire():
    print("its fire")
    cipher()
    

def water():
    print("its water")
    cipher()

def ice():
    print("its ice")
    cipher()
    


for line in lines:
    words = line.split()

    if(words[0] == "LAND"):
        emblem=("panda")
        land()
        word=cipher.variable
        decipher()
        
        
    if(words[0] == "WATER"):
        emblem=("octopus")
        water()
        word=cipher.variable
        decipher()
        
    if(words[0] == "ICE"):
        emblem=("mammoth")
        ice()
        word=cipher.variable
        decipher()
        
    if(words[0] == "FIRE"):
        emblem=("dragon")
        fire()
        word=cipher.variable
        decipher()
        
    if(words[0] == "AIR"):
        emblem=("owl")
        air()
        word=cipher.variable
        decipher()
        
    




# In[ ]:




