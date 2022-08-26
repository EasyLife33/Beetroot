#Task 1
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('helloworld'))
print(string_both_ends('my'))
print(string_both_ends('x'))


#Task 2
string1 = '1234556'
string2 = '221a322'
print ("Initial Strings : ", string1, string2)
if string1.isdigit():
    print ("String1 include all numbers")
else:
    print ("String1 don't include all numbers")     
if string2.isdigit():
    print ("String2 include all numbers")
else:
    print ("String2 don't include all numbers")
    
#Task 3    
    import random
score=0
questions = {}
for i in range(10):
    int_a = random.randint(0,10)
    int_b = random.randint(0,10)
    operators = ['+','-','*']
    operator_value = random.choice(operators)
    question = str(int_a)+" "+operator_value+" "+str(int_b)
    answer = str(eval(question))
    question+=": "       
    questions.update({question:answer})
for q in questions.keys():
    user_answer=input(q)
    if questions.get(q)==user_answer:
        print("Correct!")
        score+=1
    else:
        print("You're Wrong!")
print("You got "+str(score)+" right!")


#Task 4 
def abceck(abc):
 
    if (abc >= 'Yura' and abc <= 'Yura'):
        print(abc,"is an UpperCase ");
 
    elif (abc >= 'yura' and abc <= 'Yura'):
        print(abc,"is an LowerCase ");
abc = 'Yura';
abceck(abc);
abc = 'yura';
abceck(abc); 
abc = '0';
abceck(abc);
