import random
def wordle():
    global name
    print('\n\n\t\t\tWELCOME   TO   KINGDOM   OF   WORDS\n\n')
    ch='3'
    p=0
    while ch!='4':
        print('1.PLAY\n2.HOW TO PLAY\n3.VIEW SCORE\n4.QUIT')
        ch=input('\nWHAT WOULD YOU LIKE TO CHOOSE??')
        if ch=='1':
            w=['JUMP','BARK','GLOW','FROG','HUNT','WAVE','MINT','CLUB','DUST','RISK',
'COIN','MOON','FALL','GIFT','HORN','KING','LAKE','LION','MASK','NOTE',
'PEAK','POND','RACE','ROAD','SHIP','SNOW','SOIL','STAR','TREE','WIND',
'AXLE','BEND','CHAT','DIAL','ECHO','FAIR','GRIP','HIDE','IRON','JOIN',
'KISS','LACE','MULE','NEST','OPEN','PICK','QUIT','ROLL','SAND','TIDE']
            r=random.choice(w)
            for i in range(1,6):
                ch=input('\nENTER YOUR GUESS(a four letter word):')
                g=ch.upper()
                if g==r:
                   print('YOU GUESSED IT RIGHT!!')
                   print('YOU GOT 10 POINTS\n\n')
                   p=p+10
                   break
                else:
                    if len(g)!=4:
                        print('INVALID INPUT....YOU LOST A TRY')
                    else:
                        for j in g:
                            if j in r:
                                print('\n',j,'IS A LETTER IN THE COMPUTER CHOSEN WORD')
            else:
                print('OOPSIES YOU ARE OUT OF TRIES....')
                print('YOU WERE TO GUESS:',r)
                print('BETTER LUCK NEXT TIME')
        elif ch=='2':
            print("THE COMPUTER WILL RANDOMLY CHOOSE A WORD")
            print("YOU NEED TO GUESS THAT WORD WITHIN 5 TRIES")
            print("IF YOU GUESS THE WORD YOU'LL GET 10 POINTS")
            print("YOU WILL BE TOLD EVEN IF YOU GUESS THE WORD PARTIALLY RIGHT\n\n")
        elif ch=="3":
            if p==0:
                print('YOU HAVE 0 POINTS')
                print('COME ON!!!!!.....MAKE SOME PROGRESS')
            else:
                print('YOUR TOTAL SCORE TILL NOW IS:',p,'\n\n')
        elif ch=="4":
            print("THANK YOU\n\n\n\n")
        else:
            print('Invalid input')
    
def rock():
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠈⠓⠚⢸⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⡠⠀⡄⣀⠀⠀⠀⢻⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⠀⠙⠉⠀⠠⡶⣸⠁⠀⣠⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣦⡆⠀⠐⠒⠢⢤⣀⡰⠁⠇⠈⠘⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠠⣄⣉⣙⡉⠓⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    
def paper():
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    
def scissors():
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣶⣶⣦⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢻⣿⣿⡟⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⡿⠛⢉⣉⡉⠛⠻⠿⣧⣤⣉⠋⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⠁⢸⣿⣿⣿⣷⣦⡀⠀⠈⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣧⡈⠻⢿⣿⣿⡿⠇⢠⣶⣦⣄⠀⠀⠀⠈⠉⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣶⣤⣤⣤⣤⣶⣿⣿⡇⠙⠻⢶⣤⣀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠹⣿⣿⣦⣄⡀⠀⠀⠀⠀⠈⠻⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠙⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠈⢿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠈⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿')

def rps():
    global name
    p,c=0,0
    print('\n\n\t\tROCK/PAPER/SCISSORS GAME\n\n')
    print('YOU WILL GET 5 TRIES.......IF YOU SCORE MORE THAN COMPUTER,YOU WIN!!\n\n\n')
    for i in range(5):
        n=input('ENTER YOUR CHOICE: ')
        n=n.upper()
        l=('ROCK','PAPER','SCISSORS')
        r=random.choice(l)
        if n not in l:
            print('INVALID OUTPUT....YOU LOST A TRY:(')
        if n==r:
            if n=='ROCK':
                print('YOU BOTH CHOSE:')
                rock()
                print('ITS A TIE')
            elif n=='PAPER':
                print('YOU BOTH CHOSE:')
                paper()
                print('ITS A TIE')
            elif n=='SCISSORS':
                print('YOU BOTH CHOSE:')
                scissors()
                print('ITS A TIE')
                
        elif n=='ROCK' and r=='SCISSORS':
                print('YOU CHOSE:')
                rock()
                print('COMPUTER CHOSE:')
                scissors()
                print('YOU GOT A POINT!!')
                p=p+1
                print('YOU GOT',p,'POINTS')
        elif n=='ROCK' and r=='PAPER':
                print('YOU CHOSE:')
                rock()
                print('COMPUTER CHOSE:')
                scissors()
                print('YOU LOST:(')
                c=c+1
        elif n=='SCISSORS' and r=='PAPER':
                print('YOU CHOSE:')
                scissors()
                print('COMPUTER CHOSE:')
                paper()
                print('YOU GOT A POINT!!')
                p=p+1
                print('YOU GOT',p,'POINTS')
        elif n=='SCISSORS' and r=='ROCK':
                print('YOU CHOSE:')
                scissors()
                print('COMPUTER CHOSE:')
                rock()
                print('YOU LOST:(')
                c=c+1
        elif n=='PAPER' and r=='ROCK':
                print('YOU CHOSE:')
                paper()
                print('COMPUTER CHOSE:')
                rock()
                print('YOU GOT A POINT!!')
                p=p+1
                print('YOU GOT',p,'POINTS')
        elif n=='PAPER' and r=='SCISSORS':
                paper()
                print('COMPUTER CHOSE:')
                scissors()
                print('YOU LOST:(')
                c=c+1
    if c>p:
        print('COMPUTER SCORED',c,'POINTS')
        print('YOU LOST FROM COMPUTER.....BETTER LUCK NEXT TIME...YOU LOST 5 POINTS FROM YOUR OVERALL SCORE\n\n')
    elif c==p:
        print('YOU AND COMPUTER BOTH SCORED',c,' POINTS.......ITS A TIE\n\n')
    else:
        print('YOU SCORED MORE THAN COMPUTER')
        print('CONGRATS!!!! YOU WON...YOU HAVE GOT ANOTHER POINT IN YOUR OVERALL SCORE\n\n')
print('\t\t\t\t\t\t\t\t\tJTB PLAYS PRESENTS')
print('\t\t\t\t\t\t\t\t\t\t JTB ARENA')
ch=1

while ch!=3:
    print('1.WORDLE\n2.ROCK/PAPER/SCISSORS\n3.EXIT\n\n')
    name = input('ENTER YOUR NAME:')
    ch=int(input('ENTER YOUR CHOICE:'))
    if ch==1:
        wordle()
    elif ch==2:
        rps()
    elif ch==3:
        print('\tTHANK YOU',name,'\n HOPE YOU ENJOYED OUR GAME:)')                
    else:
        print('INVALID INPUT')