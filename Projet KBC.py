# lets make KBC using python



Questions=[
    ["Who is more powerfull?","God Emperor Doom","Thanos","Rune king thor","Beyonder"],

    ["Who is the president of israel?","Nitin Yahu","Trump","Modi","Beyonce"],

    ["Who is more sexy?","Elizabeth oalson","Tylor swift","Nitin gathkari","Harry Bhai"]

    




]


Correct_answers=[4,1,1]


Prize_money=[10000,100000,10000000,700000000]

print("Welcom into KBC")

for i in range (0,len(Questions)):# jehetu i loop e ache sutoran i ek ek kore execute hobe 
    Each_of_the_questions=Questions[i]


    print(f"Your question for Rs:{Prize_money[i]}")
    print(f'''Ready for game
          Let get started,
          {Each_of_the_questions}''')
    print(f'''Your options are here:
          1:{Each_of_the_questions[1]}             2:{Each_of_the_questions[2]}
          3:{Each_of_the_questions[3]}             4:{Each_of_the_questions[4]}''')
    


    Answer=int(input("Enter your option:"))

    if Answer==Correct_answers[i]:
        print("Your answer is correct\n" \
        "       You Have won",{Prize_money[i]})

    else:
        print("Sorry,Your answe is not correct")
        print("Go home")
        break

else:
    print("You are champion")
    print("You have won total",{Prize_money[2]})
    
