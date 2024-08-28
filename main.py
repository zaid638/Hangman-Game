from tkinter import *
import random


def score_board():

    def reset_score():
        nonlocal root3
        f = open('Score.txt','w')
        label = Label(root3, text="***SCORE SUCCESSFULLY RESETED***", font=('Bahnschrift SemiBold SemiConden',25), bg ='#ff914d')
        label.place(x=15, y=180)
        f.close()


    root3 = Tk()
    root3.title("Hangman")
    root3.geometry("550x300+400+150")
    root3.resizable(False, False)
    root3.configure(background='#ff914d')

    scrollbar = Scrollbar(root3)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(root3, font=('Bahnschrift SemiBold SemiConden',25), width=550, height=300, bg ='#ff914d')
    listbox.pack(side=RIGHT, fill=BOTH)

    B1 = Button(root3, text="RESET SCORE", font=("arial",20), bg="#ff914d", borderwidth=2, command=lambda: [scrollbar.destroy(), B1.destroy(), listbox.destroy(), reset_score()])
    B1.place(x=300, y=20)
    B2 = Button(root3, text="PLAY", width=13, font=("arial",20), bg="#ff914d", borderwidth=2, command=lambda: [root3.destroy(), main()])
    B2.place(x=300, y=100)   



    f2 = open('Score.txt')
    n1 = []
    for line in f2:
        n2 = line.strip()
        n1.append(n2)
        listbox.insert(END, n2)
    if n1 == []:
        l1 = Label(root3, text="***Score Board is Empty***", font=("arial",25), bg="#ff914d")
        l1.place(x=70, y=180)
    f2.close()

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    root3.mainloop()


def main():
    root2 = Tk()
    root2.title("Hangman")
    root2.geometry("550x300+400+150")
    root2.resizable(False, False)
    root2.configure(background='#ffde59')

    def play2():
        nonlocal name_entry
        name = name_entry.get()
        root2.destroy()
        play(name)



    frm5 = Frame(root2, width=550, height=300, bg="#ff914d", highlightbackground="black", highlightthickness=2)
    l1 = Label(frm5, text="ENTER YOUR NAME", font=("arial",25), bg="#ff914d")
    l1.place(x=105, y=60)
    name_entry = Entry(frm5, width=20, font='arial 20', bd=0)
    name_entry.place(x=120, y=120)
    name_entry.focus()
    B1 = Button(frm5, text="PLAY", font=("arial",25), bg="#ff914d", borderwidth=2, command=lambda: play2())
    B1.place(x=130, y=180)
    B2 = Button(frm5, text="SCORE", font=("arial",25), bg="#ff914d", borderwidth=2, command=lambda:[root2.destroy(), score_board()])
    B2.place(x=270, y=180) 

    frm5.pack()
    root2.mainloop()




def play(name):
    root = Tk()
    root.title("Hangman")
    root.geometry("800x560+400+150")
    root.resizable(False, False)
    root.configure(background='#ffde59')

    frm1 = Frame(root, width=400, height=250, bg="#ffde59")
    frm2 = Frame(root, width=400, height=250, bg="#ffde59")
    frm3 = Frame(root, width=800, height=250, bg="#ffde59")

    f = open('words.txt','r')

    wordss = f.read()

    words = wordss.split()

    word = random.choice(words).lower()

    guessed_correct = []

    already_guessed = ''

    tries = 6

    guess = ""

    print(word)
        


    def Guessing_Already_guessed_letter():
        nonlocal guess
        nonlocal already_guessed
        nonlocal tries
        print("Already guessed", guess)
        tries -= 1
        print(f"\nYou have {tries} guesses left.") 

    def Enter_correct_letter():
        nonlocal output
        nonlocal word
        nonlocal guess
        nonlocal guessed_correct
        print(f"Correct Letter")
        guessed_correct.append(guess)


    def Enter_the_wrong_letter():
        nonlocal tries
        print(f"Oops! That letter is not in my word")
        tries -= 1
        print(f"\nYou have {tries} guesses left.")
        if tries == 0:
            win_or_lose()  

    def win_or_lose():
        frm4 = Frame(root, width=550, height=350, bg="#ff914d", highlightbackground="black", highlightthickness=2)
        nonlocal tries
        nonlocal word
        a = []
        b = []
        if tries > 0:
   
            print("Congratulations You Win!!!")
            print("Word is ",word)
            for i in word:
                if i not in a:
                    a.append(i)
                    score = int(tries * len(a))  # Creating the score
            l7 = Label(frm4, text=f"***Congrats {name} You Win***\n\nWord is {word}\n\nYour Score is {score}", font=("arial",25), bg="#ff914d")
            l7.place(x=50, y=20)                
            print(f"Your Score is {score}")
            B1 = Button(frm4, text="PLAY", font=("arial",25), bg="#ff914d", borderwidth=2, command=lambda: [root.destroy(), main()])
            B1.place(x=125, y=235)
            B2 = Button(frm4, text="SCORE", font=("arial",25), bg="#ff914d", borderwidth=2, command=lambda: [root.destroy(), score_board()])
            B2.place(x=290, y=235)
            print(name) 
           
            f1 = open('Score.txt','a')  # Store the score in a file
            f1.write(f'{name} {score} \n')
            f1.close()

                
        else:
            print(f"Sorry, Better Luck Next Time\n\nThe Word is {word} \n\n")
            l6 = Label(frm4, text=f"Sorry, Better Luck Next Time\nThe Word is {word}", font=("arial",30), bg="#ff914d")
            l6.place(x=20, y=20)
            B1 = Button(frm4, text="PLAY", font=("arial",25), bg="#ff914d", borderwidth=2, command=lambda: [root.destroy(), main()])
            B1.place(x=120, y=200)
            B2 = Button(frm4, text="SCORE", font=("arial",25), bg="#ff914d", borderwidth=2, command=lambda: [root.destroy(), score_board()])
            B2.place(x=260, y=200)    
            f1 = open('Score.txt','a')  # Store the score in a file
            f1.write(f'{name} 0 \n')
            f1.close()         

        frm4.place(x=150, y=195)
        return ''         
        

    def gues(g):
        nonlocal word
        nonlocal guess
        nonlocal tries
        nonlocal already_guessed
        nonlocal output
        guess = g
        print(guess)

        if guess in word:
            Enter_correct_letter()
            letter_append()
        else:
            Enter_the_wrong_letter()
            letter_append()


        
    def letter_append(): 
        nonlocal guess
        nonlocal output
        output = ''
        for letter in word:
            if letter in guessed_correct:
                output += letter
            else:
                output += '_ '
        if output == word:
            win_or_lose()



        # im2 = PhotoImage(file=f'Hangman8.png')
        # l5 = Label(frm1, image= im2)
        # l5.place(x=0, y=0)

        l1 = Label(frm1, text=f"Guess the word\n\n{output}", font=("arial",30), bg="#ff914d")
        l1.place(x=60, y=50)


        im1 = PhotoImage(file=f'Hangman{tries}.gif',format ="gif")
        l4 = Label(frm2, image= im1, bd=0)
        l4.place(x=0, y=0)

        frm1.place(x=0, y=0)
        frm2.place(x=400, y=0)
        frm3.place(x=140, y=250)
        root.mainloop()


    a1 = Button(frm3, text="A", width=3, font=("arial",20), bg="#ff914d", command=lambda: gues("a")).grid(row=0, column=0, padx=10, pady=10)
    a2 = Button(frm3, text="B", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("b")).grid(row=0, column=1, padx=10, pady=10)
    a3 = Button(frm3, text="C", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("c")).grid(row=0, column=2, padx=10, pady=10)
    a4 = Button(frm3, text="D", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("d")).grid(row=0, column=3, padx=10, pady=10)
    a5 = Button(frm3, text="E", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("e")).grid(row=0, column=4, padx=10, pady=10)
    a6 = Button(frm3, text="F", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("f")).grid(row=0, column=5, padx=10, pady=10)
    a7 = Button(frm3, text="G", width=3, font=("arial",20), bg="#ff914d", command=lambda: gues("g")).grid(row=0, column=6, padx=10, pady=10)
    a8 = Button(frm3, text="H", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("h")).grid(row=1, column=0, padx=10, pady=10)
    a9 = Button(frm3, text="I", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("i")).grid(row=1, column=1, padx=10, pady=10)
    a10 = Button(frm3, text="J", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("j")).grid(row=1, column=2, padx=10, pady=10)
    a11 = Button(frm3, text="K", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("k")).grid(row=1, column=3, padx=10, pady=10)
    a12 = Button(frm3, text="L", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("l")).grid(row=1, column=4, padx=10, pady=10)
    a13 = Button(frm3, text="M", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("m")).grid(row=1, column=5, padx=10, pady=10)
    a14 = Button(frm3, text="N", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("n")).grid(row=1, column=6, padx=10, pady=10)
    a15 = Button(frm3, text="O", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("o")).grid(row=2, column=0, padx=10, pady=10)
    a16 = Button(frm3, text="P", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("p")).grid(row=2, column=1, padx=10, pady=10)
    a17 = Button(frm3, text="Q", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("q")).grid(row=2, column=2, padx=10, pady=10)
    a18 = Button(frm3, text="R", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("r")).grid(row=2, column=3, padx=10, pady=10)
    a19 = Button(frm3, text="S", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("s")).grid(row=2, column=4, padx=10, pady=10)
    a20 = Button(frm3, text="T", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("t")).grid(row=2, column=5, padx=10, pady=10)
    a21 = Button(frm3, text="U", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("u")).grid(row=2, column=6, padx=10, pady=10)
    a22 = Button(frm3, text="V", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("v")).grid(row=3, column=1, padx=10, pady=10)
    a23 = Button(frm3, text="W", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("w")).grid(row=3, column=2, padx=10, pady=10)
    a24 = Button(frm3, text="X", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("x")).grid(row=3, column=3, padx=10, pady=10)
    a25 = Button(frm3, text="Y", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("y")).grid(row=3, column=4, padx=10, pady=10)
    a26 = Button(frm3, text="Z", width=3, font=("arial",20), bg="#ff914d",  command=lambda: gues("z")).grid(row=3, column=5, padx=10, pady=10)

    output = ''
    if tries == 0 or output == word:
        win_or_lose()
    else:
        letter_append()    

    root.mainloop()

main()