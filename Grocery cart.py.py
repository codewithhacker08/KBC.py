dic={'chips':30,
     'kurkure':20
     ,'oyes':6,
     'maggie':12,
     'cream roll':10,
     'lazy':15,
     'crax':5,
     'noodle':14,
     'toffee':1,
     'coffee':25,
     'pastery':50,
     'good day':100,
     'ice cream':40,
     'choclate':200,
     'pizza':199,
     'burger':80}
print("-----------------------MENU----------------------")
for key, value in dic.items():
        print(f"{key:15}: RS{value:.2f}")        
print("-------------------------------------------------")
r={}
i=1
total=0
while True:
        Name=(input("Enter the name of thing(press q for quit) :"))
        lo=Name.lower()
        if(Name.lower()=="q"):
            break
        Prize=dic[lo]
        total=total+Prize
        r[Prize]=lo
        i=i+1
print("--------------------YOUR CART--------------------")
print("Prize\t\tName")
print("-------------------------------------------------")
for k,v in r.items():
	print(k,"\t\t",v)
print("-------------------------------------------------")
print("Total number of things is:",len(r))
print("Your total is :",total)
print("-------------------------------------------------")



