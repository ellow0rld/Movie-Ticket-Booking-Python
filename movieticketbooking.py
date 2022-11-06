#SCREEN
def screen():
    print()
    global screen_number
    print("Choose screen number")
    print("(1)SCREEN 1")
    print("(2)SCREEN 2")
    print("(3)SCREEN 3")
    a = int(input("choose your screen: "))
    if a == 1:
        screen_number = a
        print()
        timing(a)
    elif a == 2:
        screen_number = a
        print()
        timing(a)        
    elif a == 3:
        screen_number = a
        print()
        timing(a)
    else:
      print()  
      print("WRONG CHOICE")
      screen()

#TIME
def timing(a):
    global x
    global day
    global date
    global month
    import datetime
    today = datetime.datetime.now()
    date = int(input("Enter date(dd): "))
    month = input("Enter month(mm): ")
    print()
    time1 = {
        "1": "10:00am - 1:00am",
        "2": "1:10pm - 4:10pm",
        "3": "4:20pm - 7:20pm",
        "4": "7:30pm - 10:30pm"
    }
    t1 = {
        "1": "10:00",
        "2": "13:10",
        "3": "16:20",
        "4": "19:30"
    }    
    time2 = {
        "1": "10:15am - 1:15pm",
        "2": "1:25pm - 4:25pm",
        "3": "4:35pm - 7:35pm",
        "4": "7:45pm - 10:45pm"
    }
    t2 = {
        "1": "10:15",
        "2": "13:25",
        "3": "16:35",
        "4": "19:45"
    }
    time3 = {
        "1": "10:30am - 1:30pm",
        "2": "1:40pm - 4:40pm",
        "3": "4:50pm - 7:50pm",
        "4": "8:00pm - 10:45pm"
    }
    t3 = {
        "1": "10:30",
        "2": "13:40",
        "3": "16:50",
        "4": "20:00"
    }

    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time: ")
        x = time1[t]
        day = str(date) +"/"+str(month)+"/"+str(2022) +" "+ t1[t]
        day = datetime.datetime.strptime(day, "%d/%m/%Y %H:%M")
        if today > day:
            print("Sorry, Slot not available")
            print()
            print("Please choose another slot:")
            timing(a)
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time: ")
        x = time2[t]
        day = str(date) +"/"+str(month)+"/"+str(2022) +" "+ t2[t]
        day = datetime.datetime.strptime(day, "%d/%m/%Y %H:%M")
        if today > day:
            print("Sorry, Slot not available")
            print()
            print("Please choose another slot:")
            timing(a)
    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time: ")
        x = time3[t]
        day = str(date) +"/"+str(month)+"/"+str(2022) +" "+ t3[t]
        day = datetime.datetime.strptime(day, "%d/%m/%Y %H:%M")
        if today > day:
            print("Sorry, Slot not available")
            print()
            print("Please choose another slot:")
            timing(a)
 
#THEATRE 
def center():
    global theatre 
    print()
    print("Choose theatre")
    print("(1)Inox Theatre")
    print("(2)Icon Theatre")
    print("(3)Fox Theatre")
    a = int(input("choose your option: "))
    if a == 1:
      theatre = "Inox Theatre"  
      screen() 
    elif a == 2:
      theatre = "Icon Theatre"
      screen() 
    elif a == 3:
      theatre = "Fox Theatre"  
      screen()   
    else:
      print()  
      print("WRONG CHOICE")
      center()
      
#MOVIE- ACTION
def actionT():
    global movie
    print()
    print("Choose movie ")
    print("(1)Master")
    print("(2)Karnan")
    print("(3)Teddy")
    print("(4)Bhoomi")
    a = int(input("choose your option: "))
    if a == 1:
      movie = "Master"  
      center() 
    elif a == 2:
      movie = "Karnan" 
      center() 
    elif a == 3:
      movie = "Teddy" 
      center() 
    elif a == 4:
      movie = "Bhoomi" 
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      actionT()

def actionE():
    global movie
    print()
    print("Choose movie ")
    print("(1)Venom")
    print("(2)Black Widow")
    print("(3)Tenet")
    print("(4)Nobody")
    a = int(input("choose your option: "))
    if a == 1:
      movie = "Venom" 
      center() 
    elif a == 2:
      movie = "Black Widow" 
      center() 
    elif a == 3:
      movie = "Tenet" 
      center() 
    elif a == 4:
      movie = "Nobody" 
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      actionE()

def actionH():
    global movie
    print()
    print("Choose movie ")
    print("(1)URI")
    print("(2)Radhe")
    print("(3)The Power")
    print("(4)Krrish 3")
    a = int(input("choose your option: "))
    if a == 1:
      movie = "URI" 
      center() 
    elif a == 2:
      movie = "Radhe" 
      center() 
    elif a == 3:
      movie = "The Power" 
      center() 
    elif a == 4:
      movie = "Krrish 3" 
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      actionH()

#MOVIE- FAMILY
def familyT():
    global movie
    print()
    print("Choose movie ")
    print("(1)Kaadan")
    print("(2)Thaen")
    print("(3)Doctor")
    print("(4)Annaatthe")
    a = int(input("choose your option: "))
    if a == 1:
      movie = "Kaadan"  
      center() 
    elif a == 2:
      movie = "Thaen" 
      center() 
    elif a == 3:
      movie = "Doctor" 
      center() 
    elif a == 4:
      movie = "Annaatthe"  
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      familyT()

def familyE():
    global movie
    print()
    print("Choose movie ")
    print("(1)Shrek")
    print("(2)Onward")
    print("(3)Bolt")
    print("(4)Despicable Me")
    a = int(input("choose your option: "))
    if a == 1:
      movie = "Shrek"
      center() 
    elif a == 2:
      movie = "Onward" 
      center() 
    elif a == 3:
      movie = "Bolt"  
      center() 
    elif a == 4:
      movie = "Despicable Me" 
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      familyE()

def familyH():
    global movie
    print()
    print("Choose movie ")
    print("(1)English Vinglish")
    print("(2)The Lunchbox")
    print("(3)Like Stars on Earth")
    print("(4)Do Dooni Chaar")
    a = int(input("choose your option: "))
    if a == 1:
      movie = "English Vinglish "
      center() 
    elif a == 2:
      movie = "The Lunchbox" 
      center() 
    elif a == 3:
      movie = "Like Stars on Earth" 
      center() 
    elif a == 4:
      movie = "Do Dooni Chaar" 
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      familyH()

#MOVIE- HORROR
def horrorT():
    global movie
    print()
    print("Choose movie ")
    print("(1)Maya")
    print("(2)Aranmanai")
    print("(3)Demonte Colony")
    print("(4)Zero")
    a = int(input("choose your option: "))
    if a == 1:
      movie = "Maya" 
      center() 
    elif a == 2:
      movie = "Aranmanai" 
      center() 
    elif a == 3:
      movie = "Demonte Colony" 
      center() 
    elif a == 4:
      movie = "Zero" 
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      horrorT()

def horrorE():
    global movie
    print()
    print("Choose movie ")
    print("(1)A Quiet Place")
    print("(2)The Conjuring")
    print("(3)The Nun")
    print("(4)Sinister")
    a = int(input("choose your option: "))
    if a == 1:
      movie = "A Quiet Place" 
      center() 
    elif a == 2:
      movie = "The Conjuring" 
      center() 
    elif a == 3:
      movie = "The Nun" 
      center() 
    elif a == 4:
      movie = "Sinister" 
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      horrorE()

def horrorH():
    global movie
    print()
    print("Choose movie ")
    print("(1)Haunted Hills")
    print("(2)Ghost Stories")
    print("(3)Bulbbul")
    print("(4)Ghost")
    a = int(input("choose your option: "))
    if a == 1:
      movie = "Haunted Hills" 
      center() 
    elif a == 2:
      movie =  "Ghost Stories"
      center() 
    elif a == 3:
      movie = "Bulbbul" 
      center() 
    elif a == 4:
      movie =  "Ghost"
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      horrorH()

#MOVIE- SCIFI
def scifiT():
    global movie
    print()
    print("Choose movie ")
    print("(1)24")
    print("(2)Tik:Tik:Tik")
    print("(3)Indru Netru Naalai")
    print("(4)Enthiran")
    a = int(input("choose your option: "))
    if a == 1:
      movie =  "24"
      center() 
    elif a == 2:
      movie = "Tik:Tik:Tik" 
      center() 
    elif a == 3:
      movie = "Indru Netru Naalai" 
      center() 
    elif a == 4:
      movie = "Enthiran" 
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      scifiT()

def scifiE():
    global movie
    print()
    print("Choose movie ")
    print("(1)Inception")
    print("(2)Interstellar")
    print("(3)Annihilation")
    print("(4)Gravity")
    a = int(input("choose your option: "))
    if a == 1:
      movie = "Inception" 
      center() 
    elif a == 2:
      movie = "Interstellar" 
      center() 
    elif a == 3:
      movie = "Annihilation" 
      center() 
    elif a == 4:
      movie = "Gravity" 
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      scifiE()

def scifiH():
    global movie
    print()
    print("Choose movie ")
    print("(1)Cargo")
    print("(2)Mission Mangal")
    print("(3)Chand Par Chadayee")
    a = int(input("choose your option: "))
    if a == 1:
      movie =  "Cargo"
      center() 
    elif a == 2:
      movie =  "Mission Mangal"
      center() 
    elif a == 3:
      movie =  "Chand Par Chadayee"
      center()   
    else:
      print()  
      print("WRONG CHOICE")
      scifiH()

#GENRE 
def genreT():
    print()
    print("Choose genre ")
    print("(1)Action")
    print("(2)Family")
    print("(3)Horror")
    print("(4)Scifi")
    a = int(input("choose your option: "))
    if a == 1:
      actionT() 
    elif a == 2:
      familyT() 
    elif a == 3:
      horrorT() 
    elif a == 4:
      scifiT()   
    else:
      print()  
      print("WRONG CHOICE")
      genreT()

def genreE():
    print()
    print("Choose genre ")
    print("(1)Action")
    print("(2)Family")
    print("(3)Horror")
    print("(4)Scifi")
    a = int(input("choose your option: "))
    if a == 1:
      actionE() 
    elif a == 2:
      familyE() 
    elif a == 3:
      horrorE() 
    elif a == 4:
      scifiE()   
    else:
      print()  
      print("WRONG CHOICE")
      genreE()

def genreH():
    print()
    print("Choose genre ")
    print("(1)Action")
    print("(2)Family")
    print("(3)Horror")
    print("(4)Scifi")
    a = int(input("choose your option: "))
    if a == 1:
      actionH() 
    elif a == 2:
      familyH() 
    elif a == 3:
      horrorH() 
    elif a == 4:
      scifiH()   
    else:
      print()  
      print("WRONG CHOICE")
      genreH()
      
#LANGUAGE
def type():
    print()
    print("Choose language ")
    print("(1)Tamil")
    print("(2)English")
    print("(3)Hindi")
    a = int(input("choose your option: "))
    if a == 1:
      genreT() 
    elif a == 2:
      genreE() 
    elif a == 3:
      genreH()    
    else:
      print()  
      print("WRONG CHOICE")
      type()

#CITY      
def city():
    global city
    print()
    print("where do you want to watch movie?")
    print("(1)Chennai")
    print("(2)Mumbai")
    print("(3)Bangalore")
    a = int(input("choose your option: "))
    if a == 1:
      city = "Chennai"  
      type()
    elif a == 2:
      city = "Mumbai"
      type()
    elif a == 3:
      city = "Bangalore"
      type()
    else:
      print()  
      print("WRONG CHOICE")
      city()

#PAYMENT
import random
def c():
    cn = input("Enter card number: ")
    if len(str(cn))>12 or len(str(cn))<12:
        print("Please enter 12 digits")
        c()

def cv():
    cvv = input("Enter cvv number: ")
    if len(str(cvv))>3 or len(str(cvv))<3:
        print("Please enter 3 digits")
        cv()
    
def pay():
    print()
    global seats
    seats = int(input("How many seats? "))
    cost = 300 * seats
    print()
    print("Total Cost = Rs.",cost)
    print("Choose mode of payment")
    print("(1)Cash")
    print("(2)Card")
    a = int(input("Choose your option: "))
    if a == 1:
        print("Please pay Rs.",cost,"at the theatre")
    if a == 2:
        c()
        cv()
        r = random.choice([1234,4567,7809,2874])
        print("OTP: ",r)
        print("Transaction Successful")            
        
            

    
        
    
        
print("                                           ----------------------------------------------------") 
print("                                                       Welcome To Movie Ticket Booking ")
print("                                           ----------------------------------------------------")
city()
pay()

#TICKET
print()
print()
print()
for i in range (0,seats):
    print("                       ","---------------------------------------------------------------------------------")
    print("                       ","Ticket no. :",i+1,"                    ",theatre,"                     ")
    print("                       ","---------------------------------------------------------------------------------")
    print("                       ","Movie:",movie)
    print("                       ","Screen:", screen_number)
    print("                       ","Date and Time:",day)
    print()
    print ("                       ","---------------------------------------------------------------------------------")
    print ("                       ","                                  ENJOY WATCHING!!                                ")
    print ("                       ","---------------------------------------------------------------------------------")
    print()
    print()

#STORING TICKETS
import csv 
fields = ['S.No','Movie name','No. of tickets','Screen no.','Date','Month','Time']
filename = "tickets.csv"
rows = ["1",movie,seats,screen_number,date,month,x]
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerow(rows)
