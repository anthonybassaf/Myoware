import random
import tkinter
import serial
import time

###############################################
#MAIN MENU WINDOW

def start():
    global cclass
    cclass="start"
    gameplay()

def menug():
    global menu
    menu=tkinter.Tk()
    menu.title("Fight Game - Menu")
    menu.geometry("500x500")
    menu.configure(background="#7F0404", cursor="dot")
    
    print("Game initialised.\n")


    title=tkinter.Label(menu, text="Fight Game - Menu", font=("Courier", 28, "bold"), pady=20,bg="#7F0404", fg="white")
    startt=tkinter.Button(menu, text="START", command=start, pady=20, width=100)
    mexit=tkinter.Button(menu, text="Exit", command=exit)

    mexit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    title.pack()
    startt.pack()
    menu.mainloop()
###############################################
#GAME WINDOW
def gameplay():
    global menu
    menu.destroy()
    window=tkinter.Tk()
    window.title("Fight Game - Playing")
    window.geometry("640x480")
    window.configure(background="#7F0404", cursor="dot")


    global basehp
    basehp = 150
    global health
    health = 150
    global cclass
    global tdmgp
    global tdmg
    tdmg=0
    tdmgp=0
    global pmodifier
    pmodifier = 1.3

    global ehealth
    ehealth=int(health*1.2)
    global emodifier
    emodifier=1.3
    global ebasehp
    ebasehp=ehealth

    global pwin
    pwin=0

    def pwin():
        global ehealth
        if ehealth<=0:
            ehealthl.configure(text="Health: 0"+"/"+str(ebasehp))
            print("Player has won")
            global pwin
            pwin=1
            winner.configure(text="Player has won")

    def ewin():
        global health
        if health<=0:
            healthl.configure(text="Health: 0"+"/"+str(basehp))
            print("Enemy has won")
            global pwin
            pwin=1
            winner.configure(text="Enemy has won")

    def echance():
        global pwin
        global tdmg
        
        if pwin!=1:
            global health
            missche=random.randint(0,13)
            echance=random.randint(0,13)
            if echance>=5 and echance<10:
                if missche>=11:
                    print("Enemy attack missed!")
                    enemymove.configure(text="Enemy attack missed")
                else:
                    global ehealth
                    dmgdealt=int(random.randint(10,20)*emodifier)
                    health-=dmgdealt
                    print("Damage dealt to Player: "+str(dmgdealt))
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(int(health))+"/"+str(basehp))
                    enemymove.configure(text="Damage dealt to you: " + (str(dmgdealt)))
                    
            elif echance>=10:
                if missche>=10:
                    print("Enemy attack missed!")
                    enemymove.configure(text="Enemy attack missed")
                else:
                    global ehealth
                    dmgdealt=int(random.randint(14,26)*emodifier)
                    health-=dmgdealt
                    print("Damage dealt to Player: "+str(dmgdealt))
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(health)+"/"+str(basehp))
                    enemymove.configure(text="Damage dealt to you: "+(str(dmgdealt)))
            
            elif echance<=4:
                global ehealth
                dmgdealt=int(random.randint(2,7)*emodifier)
                health-=dmgdealt
                print("Damage dealt to Player: "+str(dmgdealt))
                print("Player health is now: "+str(health))
                healthl.configure(text="Health: "+str(int(health))+"/"+str(basehp))
                enemymove.configure(text="Damage dealt to you: "+(str(dmgdealt)))           

    def attack():
        global pwin
        ser = serial.Serial('COM3', 9600, timeout = 1)
        val = []
        if pwin!=1:
            global ehealth
            missch=random.randint(0,13)
            if missch>=11:
                print("\nPlayer attack missed!")
            else:
                global dmgdealtp
                dmgdealtp = 0
                while dmgdealtp == 0:
                    arduinoData = ser.readline().decode('ascii')
                    arduinoData = arduinoData.replace("\r", "")
                    arduinoData = arduinoData.replace("\n", "")
                    print(arduinoData)
                    if arduinoData != '' and int(float(arduinoData)) >= 140 and int(float(arduinoData)) <= 220:
                        val.append(float(arduinoData))
                        dmgdealtp = int(max(val)/10)
                    else:
                        val.clear()
                ehealth-=dmgdealtp
                print(max(val))
                print("\nDamage dealt to Enemy: "+str(dmgdealtp))
                print("Enemy health is now: "+str(ehealth)+"\n")
                ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
                playerddealt.configure(text="Damage dealt to enemy: "+str(dmgdealtp))
            pwin()
            echance()
            ewin()

    



		
    player=tkinter.Label(window, text="Player", font=("Courier", 24, "bold"))
    healthl=tkinter.Label(window, text=("Health: "+str(health)+"/"+str(basehp)), font=("Courier", 18))
    enemy=tkinter.Label(window, text="Enemy", font=("Courier", 24, "bold"))
    ehealthl=tkinter.Label(window, text=("Health: "+str(ehealth)+"/"+str(ebasehp)), font=("Courier", 18))
    attack=tkinter.Button(window, text="Attack", command =attack)
    texit=tkinter.Button(window, text="Exit", command=exit)
    enemymove=tkinter.Label(window,text="", font=("Courier", 14), bg="#7F0404",fg="white")
    playerddealt=tkinter.Label(window,text="", font=("Courier", 14), bg="#7F0404", fg="white")
    winner=tkinter.Label(window, text="", font=("Courier", 14, "bold"), bg="#7F0404", fg="white")

    texit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    player.pack(pady=10, padx=20, fill=tkinter.X)
    healthl.pack()
    attack.pack(pady=5)
    playerddealt.pack()
    enemy.pack(pady=10, padx=20, fill=tkinter.X)
    ehealthl.pack()
    enemymove.pack()
    winner.pack(side=tkinter.BOTTOM)
    window.mainloop()

#Initialises the game
menug()