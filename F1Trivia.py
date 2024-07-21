#f1 trivia questions
def kbc(ans,correct_ans):  
   if(ans.strip().lower()==correct_ans.strip().lower()): #makes the correct answer either into lower or upper case according to user input
    print("correct!")
    return 100
   else:
    print("incorrect!")
    return 0

total_prize=0
Questions=["Veteran Formula One driver Kimi Raikkonen is from which country?","What does DRS stand for?","What drink is sprayed by winning drivers at the end of a Formula One race?"," When did Michael Schumacher first drive for Ferrari in formula one?","Where was the first Formula One race held at night?","Where was the first Formula One race held?","Which engine does current f1 cars have?"]
Answers=["Finland","Drag Reduction System","champagne","1996","Singapore","silverstone","v6"]
print("F1 Trivia ")
for i in range(len(Questions)):
   print(Questions[i])
   ans=input("enter your answer")
   total_prize+=kbc(ans,Answers[i])
   i=i+1

print("You have won RS:",total_prize)

