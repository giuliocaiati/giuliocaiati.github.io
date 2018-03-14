# -*- coding: utf-8 -*-
score=0

def quiz():
  global score
  score=0
  print("answer a, b, c, or d")
  question1()
  question2()
  question3()
  question4()
  question5()
  question6()
  question7()
  question8()
  question9()
  question10()
  print("your score was",score,"/10")

def question1():
  print("1. What year was Hawaii submitted as a state into the U.S.?")
  print("a) 1930")
  print("b) 1896")
  print("c) 1")
  print("d) 1959")
  check("d")

def question2():
  print("2. Which year did the U.S. get involved in World War 1?")
  print("a) 2018")
  print("b) 3021")
  print("c) 4")
  print("d) 1917")
  check("d")

def question3():
  print("3. What is Giulio Caiati's third period class?")
  print("a) Computer Science")
  print("b) Computer Science and Software Engineering")
  print("c) CS&SE Scope and Sequence 2017-2018")
  print("d) Latin")
  check("b")

def question4():
  print("4. What does GE stand for in concerns of electronics?")
  print("a) GED")
  print("b) Giant Eggplant")
  print("c) General Electric")
  print("d) General Engine")
  check("c")

def question5():
  print("5. Who invented HP?")
  print("a) Kim Jong Un & Abraham Lincoln")
  print("b) Donald Trump & Thomas Edison")
  print("c) Barak Obama & Steve Harvey")
  print("d) David Packard & William Redington Hewlett")
  check("d")

def question6():
  print("6. How many continents are on Earth?")
  print("a) 4,416")
  print("b) 7")
  print("c) 195")
  print("d) 10")
  check("b")

def question7():
  print("7. What must be operational to start the emulator?")
  print("a) The AiStarter")
  print("b) Enthought canopy")
  print("c) Google chrome")
  print("d) Internet cable")
  check("a")

def question8():
  print("8. How many keys, should, be on the keyboard you’re using?")
  print("a) 103")
  print("b) 100")
  print("c) 666")
  print("d) 10")
  check("a")

def question9():
  print("9. What year was the first satellite sent into orbit, successfully?")
  print("a) 2000")
  print("b) 1959")
  print("c) 1738")
  print("d) 1969")
  check("b")

def question10():
  print("10. When did German U-boats sink the passenger ship, Lusitania?")
  print("a) 2003")
  print("b) 1900")
  print("c) 1915")
  print("d) 1869")
  check("c")

def check(answer):
  global score
  useranswer=raw_input()
  while useranswer!="a" and useranswer!="b" and useranswer!="c" and useranswer!="d":
    print("not a valid input")
    useranswer=raw_input()
  if useranswer==answer:
    score+=1
    print("corrrect!")
  else:
    print("Wrong answer was",answer)