s=0
Prizemoney=[2000,4000,6000,8000,10000]
Total=sum(Prizemoney)
name = (input("Please enter you name :"))
N = name.upper()
print("HELLO!", N, "WELCOME TO THE SHOW CALLED KAUN BANEGA CAROREPATI")
print('''There are some rules in this show as shown as following :-''')
b = input("[<==Press ENTER button to see the rules==>]")
print('''(i) There are total 5 question in this show.
(ii) Every question has 4 option.
(iii)For every correct answer money is add in your acount.
(iv) If your answer is wrong then game was over there.''')
a = input("[<==Press the ENTER button to start the game==>]")
print("BEST OF LUCK")
print("<<<<<====================GAME STARTED====================>>>>>")
Ques = [
  '''1- Who developed the Python language?
      (a)-   Zim Den
      (b)-   Guido van Rossum
      (c)-   Niene Stom
      (d)-   Wick van Rossum''',
  '''2-  In which year was the Python language developed?
      (a)-   1972
      (b)-   1981
      (c)-   1986
      (d)-   1989''',
  '''3- Which one of the following is the correct extension of the Python file?
      (a)-   .py
      (b)-   .python
      (c)-   .p
      (d)-   None of these''',
  '''4- Which character is used in Python to make a single line comment?
      (a)-   /
      (b)-   //
      (c)-   #
      (d)-   !''',
  '''5- What is the method inside the class in python language?
      (a)-   Object
      (b)-   Function
      (c)-   Attribute
      (d)-   Argument'''
]
print(Ques[0])
Ques0 = (input("PLEASE ENTER THE ANSWER (a/b/c/d) :"))
if (Ques0.lower() == "b"):
  print('Congratulations!', name, 'you have won RS' ,Prizemoney[0])
  s=s+Prizemoney[0]
else:
 print('OH! it is a wrong answer you have not won any prize.But you still have 4 questions')
print(Ques[1])
Ques1 = (input("PLEASE ENTER THE ANSWER (a/b/c/d) :"))
if (Ques1.lower() == "d"):
  print('Congratulations!', name, 'you have won RS',Prizemoney[1])
  s=s+Prizemoney[1]
else:
  print('OH! it is a wrong answer you have not won any prize.But you still have 3 questions')
print(Ques[2])
Ques2 = (input("PLEASE ENTER THE ANSWER (a/b/c/d) :"))
if (Ques2.lower() == "a"):
  print('Congratulations!', name, 'you have won RS',Prizemoney[2])
  s=s+Prizemoney[2]
else:
  print('OH! it is a wrong answer you have not won any prize.But you still have 2 questions')
print(Ques[3])
Ques3 = (input("PLEASE ENTER THE ANSWER (a/b/c/d) :"))
if (Ques3.lower() == "c"):
  print('Congratulations!', name, 'you have won RS',Prizemoney[3])
  s=s+Prizemoney[3]
else:
  print('OH! it is a wrong answer you have not won any prize.But you still have 1 questions')
print(Ques[4])
Ques4 = (input("PLEASE ENTER THE ANSWER (a/b/c/d) :"))
if (Ques4.lower() == "b"):
  print('Congratulations!', name, 'you have won RS',Prizemoney[4])
  s=s+Prizemoney[4]
else:
  print('OH! it is a wrong answer you have not won any prize.')
print("THANKS FOR PLAYING")
print("You earn total of RS",s,"out of RS",Total)
print("<<<<<====================GAME ENDED====================>>>>>")
