from ast import Pass
from glob import glob
from tkinter import *
from tkinter.font import BOLD
from turtle import bgpic

window =Tk()
window.resizable(False, False)
window.title("Wizard Game")
window.config(background='#27302f')
icon= PhotoImage(file='GameIcon.png')
window.iconphoto(True,icon)
AttackImg=PhotoImage(file='defAttackImg.png')
MagicImg=PhotoImage(file='defMagicImage.png')
SpellsImg=PhotoImage(file='SpellsImg.png')

Mhealth=100
MonsterName='monster'
Hhealth=100
PlayerName='Tomer'
Level=1


canvas = Canvas(window, bg="#27302f", height=800, width=800)
canvas.pack()
#functions
WindowCloser=0
def WinWindow():
    global Hhealth
    global Level
    global Uses
    Uses=4
    
    Hhealth=125
    Level=2
    newWindow= Tk()
    newWindow.title("You Won")
    newWindow.config(background='#27302f')

    canvas = Canvas(newWindow, bg="#27302f", height=800, width=1700)
    canvas.pack()

    YouWonText = Label(newWindow,text="You Win"
            ,font=('Arial',100,'bold'),bg='#27302f',
            fg="#63bbeb",
            activeforeground="#00FF00",
            activebackground="black")

    NewChapt=Button(newWindow,text='Move to Next Chapter',
                command=NewBattle,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                relief=RAISED,
                bd=10)
    NewChapt.pack()
    NewChapt.place(x=630, y=500)
    
    YouWonText.pack()
    YouWonText.place(x=530, y=50)

    CH2Stry = Label(newWindow,text="the Wizard Continued is adventure to the castle\n He continued venturing in the woods until suddenly \n 3 Goblins appeard from the bushes to ambush him \n the Wizard had no choice but to fight them"
            ,font=('Arial',25,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
    CH2Stry.pack()
    CH2Stry.place(x=400, y=250)

    PStats = Label(newWindow,text=f"Your stats got upgraded : Hp = {Hhealth}, Spells Left : {Uses},Level:{Level}"
            ,font=('Arial',25,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
   
    PStats.pack()
    PStats.place(x=400, y=600)
    window.destroy()

def WinWindow2():
    global WindowCloser
    global Hhealth
    global Level
    global Uses
    
    Uses=4
    Hhealth=140
    Level=3
    Win2Window= Tk()
    Win2Window.title("You Won The Battle ")
    Win2Window.geometry("1700x800")
    Win2Window.config(background='#27302f')
    
    YouWonText = Label(Win2Window,text="You Won Against the Goblins!"
            ,font=('Arial',75,'bold'),bg='#27302f',
            fg="#7cb02e",
            activeforeground="#00FF00",
            activebackground="black")

    NewChapt=Button(Win2Window,text='Move to Next Chapter',
                command=MinBossBattle,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                relief=RAISED,
                bd=10)
    NewChapt.pack()
    NewChapt.place(x=630, y=500)
    
    
    YouWonText.pack()
    YouWonText.place(x=170, y=50)

    CH2Stry = Label(Win2Window,text="after the wizard defeated the 3 goblins \n he finally arrived to the castle gate \nbut there he encouterd a foe unlike anyone before\n The Dragon Lord Gurdian The Archlongion! \n The wizard decided to fight it! ,becuase he knew If he defeat's him he'll be able to enter the Castle of mordor!"
            ,font=('Arial',20,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
    CH2Stry.pack()
    CH2Stry.place(x=100, y=250)

    PStats = Label(Win2Window,text=f"Your stats got upgraded : Hp = {Hhealth}, Spells Left : {Uses},Level:{Level}"
            ,font=('Arial',25,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
   
    PStats.pack()
    PStats.place(x=400, y=600)

def WinWindow3():
    global WindowCloser
    global Hhealth
    global Level
    global Uses
    global MedidUses
    MedidUses=5
    Uses=5
    Hhealth=175
    Level=6
    Win3Window= Tk()
    Win3Window.title("You Won The Battle ")
    Win3Window.geometry("1700x800")
    Win3Window.config(background='#27302f')
    
    YouWonText = Label(Win3Window,text="You Successfuly Defeated The Gurdian"
            ,font=('Arial',60,'bold'),bg='#27302f',
            fg="#e83541",
            activeforeground="#00FF00",
            activebackground="black")

    NewChapt=Button(Win3Window,text='Get to Last BATTLE',
                command=TheRockBattle,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                relief=RAISED,
                bd=10)
    NewChapt.pack()
    NewChapt.place(x=630, y=500)
    
    
    YouWonText.pack()
    YouWonText.place(x=130, y=50)

    CH2Stry = Label(Win3Window,text="The magican has finally reached the Legendary Staff\nUntil suddenly he heard a loud Roar\nwait who is it there...\nIS THAT THE ROCK??!!"
            ,font=('Arial',30,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
    CH2Stry.pack()
    CH2Stry.place(x=300, y=250)

    PStats = Label(Win3Window,text=f"Your stats got upgraded : Hp = {Hhealth}, Spells Left : {Uses},Level:{Level}"
            ,font=('Arial',25,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
   
    PStats.pack()
    PStats.place(x=320, y=600)
def WinWindowEnd():
    global WindowCloser
    global Hhealth
    global Level
    global Uses
    global MedidUses
    MedidUses=666
    Uses=666
    Hhealth=666
    Level=666
    Win4Window= Tk()
    Win4Window.title("You Won The Battle ")
    Win4Window.geometry("1700x800")
    Win4Window.config(background='#27302f')
    
    YouWonText = Label(Win4Window,text="You Successfuly Defeated The ROCK"
            ,font=('Arial',60,'bold'),bg='#27302f',
            fg="#e83541",
            activeforeground="#00FF00",
            activebackground="black")

    NewChapt=Button(Win4Window,text='Get to Last BATTLE',
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                relief=RAISED,
                bd=10)
    NewChapt.pack()
    NewChapt.place(x=630, y=500)
    
    
    YouWonText.pack()
    YouWonText.place(x=130, y=50)

    CH2Stry = Label(Win4Window,text="Oh Shit I cant believe it, You actually defeated THE ROCK"
            ,font=('Arial',20,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
    CH2Stry.pack()
    CH2Stry.place(x=350, y=220)

    CH3Stry = Label(Win4Window,text="And so... Thats how i got - The Legendary Magic Staff\n"
            ,font=('Arial',20,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
    CH3Stry.pack()
    CH3Stry.place(x=350, y=300)

    PStats = Label(Win4Window,text=f"Your stats got upgraded : Hp = {Hhealth}, Spells Left : {Uses},Level:{Level}"
            ,font=('Arial',25,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
   
    PStats.pack()
    PStats.place(x=320, y=600)

   
#-----------------------CH2 Elements

Goblin1Health=50 
Goblin2Health=60
Goblin3Health=80
def NewBattle():
    Chapter2=Tk()
    Chapter2.title("Chapter 2")
    Chapter2.geometry("800x800")
    Chapter2.config(background='#27302f')
    def PlayerAttack():
        global Uses
        global Hhealth
        global Goblin1Health
        global Goblin2Health
        global Goblin3Health
        Goblin1Health-=25
        Goblin2Health-=20
        Goblin3Health-=20
        Hhealth-=23
        SpellLeft_Text.config(text=f"Spells: {Uses}/4 Left")
        Mnshealth_Text.config(text=f"Goblin 1: {Goblin1Health}/50 HP")
        Mnshealth1_Text.config(text=f"Goblin 2: {Goblin2Health}/60 HP")
        Mnshealth2_Text.config(text=f"Goblin 3: {Goblin3Health}/80 HP")
        PLhealth_Text.config(text=f"You: {Hhealth}/140 HP" )
        if Goblin1Health>0 and Goblin2Health>0 and Goblin3Health>0 and Uses<=0:
            print("you cant use spells anymore")
            SpellLeft_Text.config(text=f"No spells Left")
        if Goblin1Health<=0:
            Mnshealth_Text.config(text=f"Goblin 1: 0/50 HP")
            Hhealth=Hhealth
            print("you finised the game")
        if Goblin2Health<=0:
            Mnshealth2_Text.config(text=f"Goblin 2: 0/60 HP")
            Hhealth=Hhealth
        if Goblin3Health<=0:
            Mnshealth2_Text.config(text=f"Goblin 3: 0/80 HP")
            Hhealth=Hhealth
            WinWindow2()
        
        print(MonsterName,' has :', Hhealth ,' Hp Left!')

    if Hhealth<0:
        LoseWindow()
        print("you finised the game")

        
    def PlayerMagic():
        global Uses
        global Goblin1Health
        global Goblin2Health
        global Goblin3Health
        global Hhealth
        Goblin1Health-=7
        Goblin2Health-=6
        Goblin3Health-=5
        Hhealth-=23
        Uses-=1
        SpellLeft_Text.config(text=f"Spells: {Uses} Left")
        Mnshealth_Text.config(text=f"Goblin 1: {Goblin1Health} HP")
        Mnshealth1_Text.config(text=f"Goblin 2: {Goblin2Health} HP")
        Mnshealth2_Text.config(text=f"Goblin 3: {Goblin3Health} HP")
        PLhealth_Text.config(text=f"You: {Hhealth} HP" )
        if Uses<=0:
            print("you cant use that spell uses Left:",Uses)
            SpellLeft_Text.config(text=f"No spells Left")
            GoblinHealth-=0
            GoblinHealth=GoblinHealth
        
        if Goblin1Health>0 and Goblin2Health>0 and Goblin3Health>0 and Uses<=0:
            print("you cant use spells anymore")
            SpellLeft_Text.config(text=f"No spells Left")
        if Goblin1Health<=0:
            Mnshealth_Text.config(text=f"Goblin 1: 0/50 HP")
            Hhealth=Hhealth
            print("you finised the game")
        if Goblin2Health<=0:
            Mnshealth2_Text.config(text=f"Goblin 2: 0/60 HP")
            Hhealth=Hhealth
        if Goblin3Health<=0:
            Mnshealth2_Text.config(text=f"Goblin 3: 0/80 HP")
            Hhealth=Hhealth
            WinWindow2()
    
      
   

    #buttons
    buttonAttk = Button(Chapter2,text='Attack!',
                command=PlayerAttack,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                bd=10)
    buttonAttk.pack()
    buttonAttk.place(x=50, y=420)

    buttonMagic = Button(Chapter2,text='Magic!',
                command=PlayerMagic,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                bd=10)
    buttonMagic.pack()
    buttonMagic.place(x=540, y=420)

    #labels
    label1 = Label(Chapter2,text="The Witchers Wood"
            ,font=('Arial',40,'bold'),bg='#27302f',
            fg="green",
            activeforeground="#00FF00",
            activebackground="black",)
            
    label1.pack()
    label1.place(x=180, y=20)

    PLhealth_Text = Label(Chapter2,text=f"You: {Hhealth}/125 HP",font=('Arial',28,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
    PLhealth_Text.pack()
    PLhealth_Text.place(x=40, y=100)

    Mnshealth_Text = Label(Chapter2,text=f"Goblin 1: {Goblin1Health}/80 HP",font=('Arial',28,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
            
    Mnshealth_Text.pack()
    Mnshealth_Text.place(x=430, y=100)

    Mnshealth1_Text = Label(Chapter2,text=f"Goblin 2: {Goblin2Health}/84 HP",font=('Arial',28,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
            
    Mnshealth1_Text.pack()
    Mnshealth1_Text.place(x=430, y=150)

    Mnshealth2_Text = Label(Chapter2,text=f"Goblin 3: {Goblin3Health}/88 HP",font=('Arial',28,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
            
    Mnshealth2_Text.pack()
    Mnshealth2_Text.place(x=430, y=200)

    SpellLeft_Text = Label(Chapter2,text=f"Spells: {Uses}/4 Left",font=('Arial',28,'bold'),bg='#27302f',
                fg="white",
            activeforeground="#00FF00",
            activebackground="black",)
            
    SpellLeft_Text.pack()
    SpellLeft_Text.place(x=260, y=600)

    EffectChange_Text = Label(Chapter2,text=f"*Damaging Goblins with Magic\n got reduced to 30% effected by the goblins aura",font=('Arial',20,'bold'),bg='#27302f',
                fg="white",
            activeforeground="#00FF00",
            activebackground="black",)
            
    EffectChange_Text.pack()
    EffectChange_Text.place(x=75, y=700)
BossHP=250
MedidUses=3
def MinBossBattle():
    Chapter2=Tk()
    Chapter2.title("Chapter 3 - Mini Boss")
    Chapter2.geometry("1200x1000")
    Chapter2.config(background='#27302f')
    def PlayerAttack():
        global MedidUses
        global Uses
        global Hhealth
        global BossHP
        BossHP-=22
        Hhealth-=12
        SpellLeft_Text.config(text=f"Spells: {Uses}/4 Left")
        Mnshealth_Text.config(text=f"HP \n{BossHP}/250 HP")
        PLhealth_Text.config(text=f"You: {Hhealth}/140 HP" )
        if Uses<=0:
            print("you cant use that spell uses Left:",Uses)
            SpellLeft_Text.config(text=f"No spells Left")
        if BossHP<250 and BossHP>=220:
            print("Boss Just used Swinging Axe Attack On Player")
        if BossHP<=185 and BossHP>=150:
            print("Boss Just used FireBall Attack On Player")
        if BossHP<130 and BossHP>100:
            print("Boss Just used Swinging Axe Attack On Player")
        if BossHP<=100 and BossHP>=70:
            print("Boss Just used FireBall Attack On Player")
        if BossHP<=50 and BossHP>0:
            print("Boss Just used FireBall Attack On Player")
        if BossHP<=0:
            Mnshealth_Text.config(text=f"HP \n0/250 HP")
            Hhealth=Hhealth
            WinWindow3()
            print("you finised the game")

        if MedidUses<=0:
            MedidateLeft_Text.config(text=f"No Meditations Left")
            Hhealth+=0
        print(BossHP)
        if Hhealth>=140:
            Hhealth=140
            print("Health:",Hhealth)

    if Hhealth<=0:
        LoseWindow()
        print("you finised the game")

        
    def PlayerMagic():
        global Uses
        global BossHP
        global Hhealth
        global MedidUses
        BossHP-=40
        Hhealth-=18
        Uses-=1
        SpellLeft_Text.config(text=f"Spells: {Uses}/4 Left")
        Mnshealth_Text.config(text=f"HP \n{BossHP}/540 HP")
        PLhealth_Text.config(text=f"You: {Hhealth} HP" )
        if Uses<=0:
            print("you cant use that spell uses Left:",Uses)
            SpellLeft_Text.config(text=f"No spells Left")
            BossHP-=0
            Chapter2.destroy()
        if BossHP<250 and BossHP>=220 and Uses<=0:
            print("Boss Just used Swinging Axe Attack On Player")
        if BossHP<=185 and BossHP>=150 and Uses<=0:
            print("Boss Just used FireBall Attack On Player")
        if BossHP<130 and BossHP>100 and Uses<=0:
            print("Boss Just used Swinging Axe Attack On Player")
        if BossHP<=100 and BossHP>=70 and Uses<=0:
            print("Boss Just used FireBall Attack On Player")

        if BossHP<=50 and BossHP>0 and Uses<=0:
            print("Boss Just used FireBall Attack On Player")
            

        if BossHP<=0:
            Mnshealth_Text.config(text=f"HP \n0/250 HP")
            Hhealth=Hhealth
            WinWindow3()
            print("you finised the game")
        if Hhealth>=140:
            Hhealth=140
            print("Health:",Hhealth)
        if MedidUses<=0:
            MedidateLeft_Text.config(text=f"No Meditations Left")
        if Hhealth<0:
            print("you Losed the game")
            LoseWindow()
    
    
    def Medidate():
        global MedidUses
        global Hhealth
        Hhealth+=10
        global Uses
        MedidUses-=1

        if Uses<=0:
            Chapter2.destroy()
            print("you cant use that spell uses Left:",Uses)
            SpellLeft_Text.config(text=f"No spells Left")

        SpellLeft_Text.config(text=f"Spells: {Uses}/4 Left")
        PLhealth_Text.config(text=f"You: {Hhealth}/140 HP" )
        MedidateLeft_Text.config(text=f"Meditations Left: {MedidUses}/3 Left")
        if MedidUses<=0:
            print("you cant use that! Meditation uses Left:",MedidUses)
            MedidateLeft_Text.config(text=f"No Meditations Left")
            Chapter2.destroy()
        if Hhealth>=140:
            Hhealth=140
            print("Health:",Hhealth)
    #buttons
    buttonAttk = Button(Chapter2,text='Attack!',
                command=PlayerAttack,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                bd=10)
    buttonAttk.pack()
    buttonAttk.place(x=300, y=360)

    buttonMagic = Button(Chapter2,text='Magic!',
                command=PlayerMagic,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                bd=10)
    buttonMagic.pack()
    buttonMagic.place(x=700, y=360)

    MedidtateButton = Button(Chapter2,text='Medidate',
                command=Medidate,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                bd=10)
    MedidtateButton.pack()
    MedidtateButton.place(x=480, y=450)

    #labels
    label1 = Label(Chapter2,text="DragonLord Gurdian\nArchlongion"
            ,font=('Arial',35,'bold'),bg='#27302f',
            fg="#ff3037",
            activeforeground="#00FF00",
            activebackground="black",)
            
    label1.pack()
    label1.place(x=340, y=20)

    PLhealth_Text = Label(Chapter2,text=f"You: {Hhealth}/140 HP",font=('Arial',28,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
    PLhealth_Text.pack()
    PLhealth_Text.place(x=440, y=575)

    Mnshealth_Text = Label(Chapter2,text=f"HP \n{BossHP}/250 HP",font=('Arial',28,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
            
    Mnshealth_Text.pack()
    Mnshealth_Text.place(x=480, y=150)


    SpellLeft_Text = Label(Chapter2,text=f"Spells: {Uses}/4 Left",font=('Arial',28,'bold'),bg='#27302f',
                fg="white",
            activeforeground="#00FF00",
            activebackground="black",)
            
    SpellLeft_Text.pack()
    SpellLeft_Text.place(x=450, y=630)


    MedidateLeft_Text = Label(Chapter2,text=f"Meditaions Left: {MedidUses}/3 Left",font=('Arial',28,'bold'),bg='#27302f',
                fg="white",
            activeforeground="#00FF00",
            activebackground="black",)
            
    MedidateLeft_Text.pack()
    MedidateLeft_Text.place(x=380, y=685)

    EffectChange_Text = Label(Chapter2,text=f"*Damaging Dragon with Normal Attacks\n got reduced by 50%",font=('Arial',20,'bold'),bg='#27302f',
                fg="white",
            activeforeground="#00FF00",
            activebackground="black",)
            
    EffectChange_Text.pack()
    EffectChange_Text.place(x=340, y=735)
TheRockHp=400 
def TheRockBattle():
    global Hhealth
    global MedidUses
    MedidUses=5
    Hhealth=175
    Chapter2=Tk()
    Chapter2.title("Chapter 3 - Mini Boss")
    Chapter2.geometry("1200x1000")
    Chapter2.config(background='#27302f')
    def PlayerAttack():
        global MedidUses
        global Uses
        global Hhealth
        global TheRockHp
        MedidUses=5
        Hhealth-=12
        TheRockHp-=32
        print(Hhealth)
        SpellLeft_Text.config(text=f"Spells: {Uses}/5 Left")
        Mnshealth_Text.config(text=f"HP \n{TheRockHp}/400 HP")
        PLhealth_Text.config(text=f"You: {Hhealth}/175 HP" )
        if Uses<=0:
            print("you cant use that spell uses Left:",Uses)
            SpellLeft_Text.config(text=f"No spells Left")
        if TheRockHp<400 and TheRockHp>=370:
            print("Boss Just used Rocking-Barrage On Player")
        if TheRockHp<=350 and TheRockHp>=300:
            print("Boss Just used  Rocking SLAM On Player")
        if TheRockHp<360 and TheRockHp>310:
            print("Boss Just used ITS ABOUT DRIVE ITS ABOUT POWER Attack On Player")
        if TheRockHp<=300 and TheRockHp>=270:
            print("Boss Just used ITS ABOUT DRIVE ITS ABOUT POWER On Player")
        if TheRockHp<=250 and TheRockHp>210:
            print("Boss Just used ITS ABOUT DRIVE ITS ABOUT POWER On Player")
        if TheRockHp<180 and TheRockHp>=145:
            print("Boss Just used Rock.Special_Attack Attack On Player")
        if TheRockHp<=135 and TheRockHp>=100:
            print("Boss Just used Special_Attack On Player")
        if TheRockHp<=80 and TheRockHp>=40:
            print("Boss Just used Rocking-Barrage Attack On Player")
        if TheRockHp<=35 and TheRockHp>=40:
            print("Boss Just used Eye Brow Raise Attack On Player")
        if TheRockHp<=0:
            Mnshealth_Text.config(text=f"HP \n0/400 HP")
            Hhealth=Hhealth
            WinWindowEnd()
            print("you finised the game") 

        if MedidUses<=0:
            MedidateLeft_Text.config(text=f"No Meditations Left")
            Hhealth+=0
        print(BossHP)
        
        if Hhealth>=175:
            Hhealth=175
            print("Health:",Hhealth)
    if Hhealth<=0:
        LoseWindow()
        print("you finised the game")

        
    def PlayerMagic():
        global Uses
        global TheRockHp
        global Hhealth
        global MedidUses
        MedidUses=5
        TheRockHp-=45
        Hhealth-=18
        Uses-=1
        SpellLeft_Text.config(text=f"Spells: {Uses}/5 Left")
        Mnshealth_Text.config(text=f"HP \n{TheRockHp}/400 HP")
        PLhealth_Text.config(text=f"You: {Hhealth}/175 HP" )
        if Uses<=0:
            print("you cant use that spell uses Left:",Uses)
            SpellLeft_Text.config(text=f"No spells Left")
            TheRockHp-=0
            Chapter2.destroy()
        if TheRockHp<400 and TheRockHp>=370:
            print("Boss Just used Rocking-Barrage On Player")
        if TheRockHp<=350 and TheRockHp>=300:
            print("Boss Just used  Rocking SLAM On Player")
        if TheRockHp<360 and TheRockHp>310:
            print("Boss Just used ITS ABOUT DRIVE ITS ABOUT POWER Attack On Player")
        if TheRockHp<=300 and TheRockHp>=270:
            print("Boss Just used ITS ABOUT DRIVE ITS ABOUT POWER On Player")
        if TheRockHp<=250 and TheRockHp>210:
            print("Boss Just used ITS ABOUT DRIVE ITS ABOUT POWER On Player")
        if TheRockHp<180 and TheRockHp>=145:
            print("Boss Just used Rock.Special_Attack Attack On Player")
        if TheRockHp<=135 and TheRockHp>=100:
            print("Boss Just used Special_Attack On Player")
        if TheRockHp<=80 and TheRockHp>=40:
            print("Boss Just used Rocking-Barrage Attack On Player")
        if TheRockHp<=35 and TheRockHp>=40:
            print("Boss Just used Eye Brow Raise Attack On Player")
         

        if TheRockHp<=0:
            Mnshealth_Text.config(text=f"HP \n0/400 HP")
            Hhealth=Hhealth
            WinWindowEnd()
            print("you finised the game")
        if MedidUses<=0:
            MedidateLeft_Text.config(text=f"No Meditations Left")
        if Hhealth>=175:
            Hhealth=175
            print("Health:",Hhealth)
        if Hhealth<0:
            print("you Losed the game")
            LoseWindow()
    
    
    def Medidate():
        global Uses
        global MedidUses
        global Hhealth
        Hhealth+=10
        MedidUses-=1
        if Uses<=0:
            Chapter2.destroy()
            print("you cant use that spell uses Left:",Uses)
            SpellLeft_Text.config(text=f"No spells Left")

        SpellLeft_Text.config(text=f"Spells: {Uses}/5 Left")
        PLhealth_Text.config(text=f"You: {Hhealth}/175 HP" )
        MedidateLeft_Text.config(text=f"Meditations Left: {MedidUses}/5 Left")
        if MedidUses<=0:
            print("you cant use that! Meditation uses Left:",MedidUses)
            MedidateLeft_Text.config(text=f"No Meditations Left")
            Chapter2.destroy()
        if Hhealth>=175:
            Hhealth=175
            print("Health:",Hhealth)
        
    #buttons
    buttonAttk = Button(Chapter2,text='Attack The Rock!',
                command=PlayerAttack,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                bd=10)
    buttonAttk.pack()
    buttonAttk.place(x=170, y=360)

    buttonMagic = Button(Chapter2,text='Magic!',
                command=PlayerMagic,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                bd=10)
    buttonMagic.pack()
    buttonMagic.place(x=700, y=360)

    MedidtateButton = Button(Chapter2,text='Medidate',
                command=Medidate,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                bd=10)
    MedidtateButton.pack()
    MedidtateButton.place(x=480, y=450)

    #labels
    label1 = Label(Chapter2,text="The Rock"
            ,font=('Arial',70,'bold'),bg='#27302f',
            fg="gray",
            activeforeground="#00FF00",
            activebackground="black",)
            
    label1.pack()
    label1.place(x=340, y=20)

    PLhealth_Text = Label(Chapter2,text=f"You: {Hhealth}/175 HP",font=('Arial',28,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
    PLhealth_Text.pack()
    PLhealth_Text.place(x=440, y=575)

    Mnshealth_Text = Label(Chapter2,text=f"HP \n{TheRockHp}/400 HP",font=('Arial',40,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
            
    Mnshealth_Text.pack()
    Mnshealth_Text.place(x=460, y=150)


    SpellLeft_Text = Label(Chapter2,text=f"Spells: {Uses}/5 Left",font=('Arial',28,'bold'),bg='#27302f',
                fg="white",
            activeforeground="#00FF00",
            activebackground="black",)
            
    SpellLeft_Text.pack()
    SpellLeft_Text.place(x=450, y=630)


    MedidateLeft_Text = Label(Chapter2,text=f"Meditaions Left: {MedidUses}/5 Left",font=('Arial',28,'bold'),bg='#27302f',
                fg="white",
            activeforeground="#00FF00",
            activebackground="black",)
            
    MedidateLeft_Text.pack()
    MedidateLeft_Text.place(x=380, y=685)

    EffectChange_Text = Label(Chapter2,text=f"*Damaging Dragon with Normal Attacks\n got reduced by 50%",font=('Arial',20,'bold'),bg='#27302f',
                fg="white",
            activeforeground="#00FF00",
            activebackground="black",)
            
    EffectChange_Text.pack()
    EffectChange_Text.place(x=340, y=735)

def LoseWindow():
    newWindow1= Tk()
    newWindow1.geometry("800x800")
    newWindow1.config(background='#27302f')
    YouWonText = Label(newWindow1,text="You Lose"
            ,font=('Arial',100,'bold'),bg='#27302f',
            fg="red",
            activeforeground="#00FF00",
            activebackground="black",)
            
    YouWonText.pack()
    YouWonText.place(x=100, y=250)
    
    window.destroy()
Uses=3

#-----------------------
#Attack methods
def PAttack():
    global Mhealth
    global Hhealth
    Mhealth-=20
    Hhealth-=14
    SpellLeft_Text.config(text=f"Spells: {Uses} Left")
    Mnshealth_Text.config(text=f"Monster: {Mhealth} HP")
    PLhealth_Text.config(text=f"You: {Hhealth} HP" )
    if Mhealth>0 and Uses<=0:
       print("you cant use spells anymore")
       SpellLeft_Text.config(text=f"No spells Left")
    if Mhealth<=0:
        Mhealth=Mhealth
        Hhealth=Hhealth
        WinWindow()
        print("you finised the game")
    print(MonsterName,' has :', Mhealth ,' Hp Left!')

    if Hhealth<0:
        LoseWindow()
        print("you finised the game")

        
def PMagic():
    global Uses
    global Mhealth
    global Hhealth
    print(Uses)
    Mhealth-=10
    Hhealth-=7
    Uses-=1
    Mnshealth_Text.config(text=f"Monster: {Mhealth} HP" )
    PLhealth_Text.config(text=f"You: {Hhealth} HP" )
    SpellLeft_Text.config(text=f"Spells: {Uses} Left")
    if Uses<=0:
        print("you cant use that spell uses Left:",Uses)
        SpellLeft_Text.config(text=f"No spells Left")
        Mhealth-=0
        Mhealth=Mhealth
        
    if Mhealth>0 and Uses<=0:
       print("you cant use spells anymore")
       SpellLeft_Text.config(text=f"No spells Left")
    if Mhealth<0:
        print("you finised the game")
        WinWindow()
    if Hhealth<0:
        print("you finised the game")
        LoseWindow()
    
      
   

#buttons
buttonAttk = Button(window,text='Attack!',
                command=PAttack,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                image=AttackImg,
                compound='bottom',
                relief=RAISED,
                bd=10)
buttonAttk.pack()
buttonAttk.place(x=50, y=420)

buttonMagic = Button(window,text='Magic!',
                command=PMagic,
                font=("Comic sans",20,BOLD),
                fg="white",
                bg="#1061e3",
                activeforeground="white",
                activebackground="#1061e3",
                state=ACTIVE,
                image=MagicImg,
                compound='bottom',
                relief=RAISED,
                bd=10)
buttonMagic.pack()
buttonMagic.place(x=540, y=420)

#Bools
label1 = Label(window,text="Wizard Adventure"
            ,font=('Arial',40,'bold'),bg='#27302f',
            fg="#63bbeb",
            activeforeground="#00FF00",
            activebackground="black",)
            
label1.pack()
label1.place(x=180, y=20)

PLhealth_Text = Label(window,text=f"You: {Hhealth} HP",font=('Arial',28,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
PLhealth_Text.pack()
PLhealth_Text.place(x=40, y=100)

Mnshealth_Text = Label(window,text=f"Monster: {Mhealth} HP",font=('Arial',28,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black")
            
Mnshealth_Text.pack()
Mnshealth_Text.place(x=430, y=100)

SpellImg = Label(window,bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black",
            image=SpellsImg)
            
SpellImg.pack()
SpellImg.place(x=300, y=540)

SpellLeft_Text = Label(window,text=f"Spells: {Uses} Left",font=('Arial',28,'bold'),bg='#27302f',
            fg="white",
            activeforeground="#00FF00",
            activebackground="black",)
            
SpellLeft_Text.pack()
SpellLeft_Text.place(x=260, y=700)




window.mainloop()
