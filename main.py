import random
import pyttsx3
def speak(a):
    engine=pyttsx3.init()
    engine.say(a)
    engine.runAndWait()
def complete():
    speak("this is snake water gun  game, enter the value 1 for snake , 2 for water , 3 for gun")
    print("this is snake water  gun game, enter the value \n1 for snake  \n2 for water  \n3 for gun")
    print("choose : 1 for you versus computer \n 2 for two player game")
    speak("choose 1 for you versus computer and 2 for two player game")
    z=int(input("enter the choice:"))
    def game2():
        for i in range (1):
                speak("enter the value, player 1")
                option=int(input("enter the value  player 1 for snake or water or gun:"))
                speak(option)
                if option==1:
                    print("player 1 choose snake")
                    speak("player 1 choose snake")
                elif option==2:
                    print("player 1 choose water")
                    speak("player 1 choose water")
                elif option==3:
                    print("player 1 choose gun")
                    speak("player 1 choose gun")
                else:
                    print("invalid input")
                    speak("invalid input ")
                speak("enter the value player 2")
                c_option=int(input("enter the value player 2 for snake or water or gun:"))
                if c_option==1:
                    print("player 2 choose snake")
                    speak("player 2 choose snake")
                elif c_option==2:
                    print("player 2 choose water")
                    speak("player 2 choose water")
                elif c_option==3:
                    print("player 2 choose gun")
                    speak("player 2 choose gun")
                else:
                    print("invalid input")
                    speak("invalid input")
                    break
                if (c_option==1 and option==1):
                    print("tie")
                    speak("tie")
                elif (c_option==2 and option==2):
                    print("tie")
                    speak("tie")
                elif (c_option==3 and option==3):
                    print("tie")
                    speak("tie")
                elif(c_option==1 and option==2):
                    print("player 2 won")
                    speak("player 2 won")
                elif(c_option==1 and option==3):
                    print("player 1 won")
                    speak("player 1 won")
                elif(c_option==2 and option==1):
                    print("player 1 won")
                    speak("player 1 won")
                elif(c_option==2 and option==3):
                    print("player 2 won")
                    speak("player 2 won")
                elif(c_option==3 and option==2):
                    print("player 1 won")
                    speak("player 1 won ")
                elif(c_option==3 and option==1):
                    print("player 2 won")
                    speak("player 2 won ")
                def ask():
                    speak("if you want to play next round click 1 else click 2 !")
                    print("if you want to play next round click 1 else click 2 !")
                    a=int(input("enter the value:"))
                    if a==1:
                        game()
                    elif a==2:
                        print("bye")
                        speak("bye")
                    else:
                        ask()
                if c_option==1:
                    print("player 2 choose snake")
                    speak("player 2 choose snake")
                elif c_option==2:
                    print("player 2 choose water")
                    speak("player 2 choose water")
                elif c_option==3:
                    print("player 2 choose gun")
                    speak("player 2 choose gun")
                if (c_option==1 and option==1):
                    print("tie")
                    speak("tie")
                elif (c_option==2 and option==2):
                    print("tie")
                    speak("tie")
                elif (c_option==3 and option==3):
                    print("tie")
                    speak("tie")
                elif(c_option==1 and option==2):
                    print("player 2 won")
                    speak("player 2 won")
                elif(c_option==1 and option==3):
                    print("player 1 won")
                    speak("player 1 won")
                elif(c_option==2 and option==1):
                    print("player 1 won")
                    speak("player 1 won")
                elif(c_option==2 and option==3):
                    print("player 2 won")
                    speak("player 2 won")
                elif(c_option==3 and option==2):
                    print("player 1 won")
                    speak("player 1 won ")
                elif(c_option==3 and option==1):
                    print("player 2 won")
                    speak("player 2 won ")
                def ask():
                    speak("if you both  want to play next round click 1 else click 2 !")
                    print("if you both  want to play next round click 1 else click 2 !")
                    a=int(input("enter the value:"))
                    if a==1:
                        complete()
                    elif a==2:
                        print("bye")
                        speak("bye")
                    else:
                        ask()
                ask()
    def game():
            for i in range (1):
                speak("enter the value")
                option=int(input("enter the value of snake or water or gun:"))
                speak(option)
                if option==1:
                    print("you choose snake")
                    speak("you choose snake")
                elif option==2:
                    print("you choose water")
                    speak("you choose water")
                elif option==3:
                    print("you choose gun")
                    speak("you choose gun")
                else:
                    print("invalid input")
                    speak("invalid input ")
                c_option=random.randint(1,3)
                if c_option==1:
                    print("computer choose snake")
                    speak("computer choose snake")
                elif c_option==2:
                    print("computer choose water")
                    speak("computer choose water")
                elif c_option==3:
                    print("computer choose gun")
                    speak("computer choose gun")
                if (c_option==1 and option==1):
                    print("tie")
                    speak("tie")
                elif (c_option==2 and option==2):
                    print("tie")
                    speak("tie")
                elif (c_option==3 and option==3):
                    print("tie")
                    speak("tie")
                elif(c_option==1 and option==2):
                    print("computer won")
                    speak("computer won")
                elif(c_option==1 and option==3):
                    print("you won")
                    speak("you won")
                elif(c_option==2 and option==1):
                    print("you won")
                    speak("you won")
                elif(c_option==2 and option==3):
                    print("computer won")
                    speak("computer won")
                elif(c_option==3 and option==2):
                    print("you won")
                    speak("you won ")
                elif(c_option==3 and option==1):
                    print("computer won")
                    speak("computer won ")
                def ask():
                    speak("if you want to play next round click 1 else click 2 !")
                    print("if you want to play next round click 1 else click 2 !")
                    a=int(input("enter the value:"))
                    if a==1:
                        complete()
                    elif a==2:
                        print("bye")
                        speak("bye")
                    else:
                        ask()
                ask()
    if z==1:
        game()
    elif z==2:
        game2()
    else:
        print("invalid input")

complete()
print("the end")
speak("the end")