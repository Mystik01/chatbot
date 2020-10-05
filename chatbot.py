import time
from time import sleep
import requests # pip install requests
import sys

"""Optional Imports"""
from tqdm import tqdm # pip install tqdm
from googlesearch import search # pip install google



def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor
spinner = spinning_cursor()

def google():
    query = input("What do you wanna search? ")
    for _ in range(25):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    print("Here are the top 5 results:")
    for i in search(query, tld="co.in", num=5, stop=5):
        print(i)

def weather():
    weathercity = input("What town/city are you in? ")
    weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+weathercity+',uk&units=metric&appid=886705b4c1182eb1c69f28eb8c520e20')
    data = weather.json()

    temp = data['main']['temp_max']
    description = data['weather'][0]['description']
    cityname = data['name']
    weatherprint ="In {}, it is currently {}° with {}."
    for _ in range(25):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    print(weatherprint.format(cityname, temp, description))
    sleep(2.0)

def kill():
    for i in tqdm (range (101),  
    desc="Loading…",  
    ascii=False, ncols=75): 
        time.sleep(0.01)
    sys.exit()
        

"""LOGIN"""

users = {}
 
def newUser():
    createLogin = input("Create a username: ")
 
    if createLogin in users:
        print("\nLogin name already exist!\n")
        newUser()
    else:
        createPassw = input("Create a password: ")
        users[createLogin] = createPassw
        print("\nUser created, now please login!\n")
        sleep(1.0)
        oldUser()
 
def oldUser():
    login = input("Enter existing username: ")
    passw = input("Enter password: ")
 
    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
        sleep(3.0)
        
    else:
        print("\nUser doesn't exist or wrong password! Please retry!")
        sleep(1.0)
        oldUser()
  

"""Program START"""

for i in tqdm (range (101),  
               desc="Loading…",  
               ascii=False, ncols=75): 
    time.sleep(0.01) 
      
print("Complete.") 

print("Welcome To Chatbot 2.0!")
sleep(2.0)
print("To get you started you need to create an account!")
sleep(2.0)


#account
newUser()



print("Well done for logging in!")
name = input("What's you name? ")
print("Cool!\n")
sleep(1.0)

"""QUIZ"""

print("Now I've created quiz for you to play:")
sleep(1.5)
print("When answering, please type the letter number next to the answer.")
sleep(2.5)

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "\nWho is the richest person in 2020?\nA - Bill Gates\nB - Jeff Bezos\nType your answer here: ",
     "\nIn which year did Twitter launch?\nA - 2006\nB - 2000\nC - 2010\nType your answer here: ",
     "\nWhat is the longest river in the UK?\nA - River Thames\nB - River Severn\nC - River Wye\nType your answer here: ",
     "\nThe tallest building in the world, is located in which city?\nA - New York\nB - Paris\nC - Dubai\nD - Tokyo\nType your answer here: ",
     "\nWhich country's flag, has 50 stars?\nA - United Kingdom\nB - Spain\nC - China\nD - USA\nType your answer here: ",
     "\nWhat is the Indian currency called?\nA - Yen\nB - Rupee\nC - Renminbi\nD - Birr\nType your answer here: ",
     "\nIn which year was the popular video game Fortnite released?\nA - 2010\nB - 2016\nC - 2011\nD - 2017\nType your answer here: ",
     "\nName the composer behind the soundtracks of The Lion King, Inception and Pirates of the Caribbean.\nA - John Williams\nB - Danny Elfman\nC - Hans Zimmer\nType your answer here: ",
     "\nIn what year did Channel 5 launch in the UK?\nA - 2000\nB - 1990\nC - 1997\nD - 1999\nType your answer here: ",
     "\nIn tennis, who has won more Women’s Singles Grand Slam titles?\nA - Martina Navratilova\nB - Serena Williams\nType your answer here: ",
     
]

questions = [
     Question(question_prompts[0], "B"),
     Question(question_prompts[1], "A"),
     Question(question_prompts[2], "B"),
     Question(question_prompts[3], "C"),
     Question(question_prompts[4], "D"),
     Question(question_prompts[5], "B"),
     Question(question_prompts[6], "D"),
     Question(question_prompts[7], "C"),
     Question(question_prompts[8], "C"),
     Question(question_prompts[9], "B"),


     
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt).upper()
          if answer == question.answer:
               score += 1
     print(name+ ", you got", score, "out of", len(questions), "! Well Done!")
     sleep(2.0)
     print("Thanks for playing the quiz! If you want to re-try the quiz type !quiz later on")

 
run_quiz(questions)


"""API KEY
886705b4c1182eb1c69f28eb8c520e20

http://api.openweathermap.org/data/2.5/weather?q=alton,uk&units=metric&appid=886705b4c1182eb1c69f28eb8c520e20'
http://api.openweathermap.org/data/2.5/weather?q='+weathercity+'uk&appid=886705b4c1182eb1c69f28eb8c520e20

"""
"""WEATHER"""

print("\nI can also tell you useful things like the weather!")
sleep(1.0)
weather()
print("If you would like to find out the weather again, just type !weather")
"""GOOGLE SEARCH"""

print("\nI can also make Google searches!")
sleep(0.5)
google()
print("\nIf you want to access google again, just type: !google")



while True:
    commands = input("\nIf you want to find the weather in a different place or search somthing else, type one of the commands below:\n")
    if commands == '!weather':
        weather()
    elif commands == '!google':
        google()
    elif commands == '!quiz':
        print("So you'd like to re-try the quiz...")
        sleep(1.5)
        run_quiz(questions)
    else:
        print("IDK")
        kill()



