import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
from pygame import mixer
import pyowm
import config
import speech_recognition as sr
from google_places import *
import pyjokes
import requests
import json
# from speech_recognition.__main__ import r, audio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 25)

greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['I_was_created_by_Edward_right_in_his_computer.',
        'Edward', 'Some_guy_whom_i_never_got_to_know.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is you name']
cmd1 = ['open browser', 'open google']
cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
cmd3 = [
    'tell a joke',
    'tell me a joke',
    'say something funny',
    'tell something funny']
cmd4 = ['open youtube', 'i want to watch a video']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = [
    'what is your color',
    'what is your colour',
    'your color',
    'your color?']
colrep = [
    'Right now its rainbow',
    'Right now its transparent',
    'Right now its non chromatic']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = ['thank you']

repfr9 = ['youre welcome', 'glad i could help you']

personalized = get_location()
stores = []
stores_data = {}


"""with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print "Say Something"
    #listens for the user's input
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print "you said: " + text

    #error occurs when google could not understand what was said

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio") """
print("hi ", "Setting location through ip bias, Change location?")
change_location = False
while True:
    speech_type = input('Speech/Text: ')
    if speech_type.lower() != "speech":
        translate = input("Type: ")
    else:
        now = datetime.datetime.now()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Tell me something:")
            engine.say('Say something')
            engine.runAndWait()
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                translate = r.recognize_google(audio)
                print("You said:- " + translate)
            except sr.UnknownValueError:
                print("Could not understand audio")
                engine.say('I didnt get that. Rerun the code')
                engine.runAndWait()
    if translate in greetings:
        random_greeting = random.choice(greetings)
        print(random_greeting)
    elif translate.lower() == "yes":
        change_location = True
        print("Location?")
    elif change_location is True:
        personalized = change_location_query(translate, config.google_api_key)
        change_location = False
    elif translate in question:
        print('I am fine')
    elif translate in var1:
        reply = random.choice(var2)
        print(reply)
    elif translate in cmd9:
        print(random.choice(repfr9))
    elif translate in cmd7:
        print(random.choice(colrep))
        print('It keeps changing every micro second')
    elif translate in cmd8:
        print(random.choice(colrep))
        print('It keeps changing every micro second')
    elif translate in cmd2:
        mixer.init()
        mixer.music.load("song.wav")
        mixer.music.play()
    elif translate in var4:
        engine.say('I am a bot, silly')
        engine.runAndWait()
    elif translate in cmd4:
        webbrowser.open('http://www.youtube.com')
    elif translate in cmd6:
        print('see you later')
        exit()
    elif translate in cmd5:
        import requests, json 

# Enter your API key here 
        api_key = config.weather_api_key

# base_url variable to store url 
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
        city_name = get_location()
        print("current city is:",
            city_name)

# complete_url variable to store 
# complete url address 
        complete_url = base_url + "appid=" + api_key +"&q=" + city_name
# get method of requests module 
# return response object 
        response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
        x = response.json() 

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
        if x["cod"] != "404":
            
        

    # store the value of "main" 
    # key in variable y 
            y = x["main"] 

    # store the value corresponding 
    # to the "temp" key of y 
            current_temperature = y["temp"]  

    # store the value corresponding 
    # to the "pressure" key of y 
            current_pressure = y["pressure"] 

    # store the value corresponding 
    # to the "humidity" key of y 
            current_humidiy = y["humidity"] 

    # store the value of "weather" 
    # key in variable z 
            z = x["weather"] 

    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z 
            weather_description = z[0]["description"] 

    # print following values
             
            print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
                    "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
                    "\n humidity (in percentage) = " +
                    str(current_humidiy) +
                    "\n description = " +
                    str(weather_description)) 

        else: 
            print(" City Not Found ") 

        engine.say(y["pressure"])
        engine.runAndWait()
        engine.say('humidity')
        engine.runAndWait()
        engine.say(current_humidiy)
        engine.runAndWait()
        engine.say('temperature')
        engine.runAndWait()
        engine.say(current_temperature)
        engine.runAndWait()
    elif translate in var3:
        print("Current date and time : ")
        print(now.strftime("The time is %H:%M"))
        engine.say(now.strftime("The time is %H:%M"))
        engine.runAndWait()
    elif translate in cmd1:
        webbrowser.open('http://www.google.com')
    elif translate in cmd3:
        jokrep = pyjokes.get_joke()
        print(jokrep)
        engine.say(jokrep)
        engine.runAndWait()
    elif ("them" in translate.split(" ") or "popular" in translate.split(" ")) and stores:
        sorted_stores_data = sorted(
            stores_data,
            key=lambda x: import requests, json 

# Enter your API key here 
        api_key = config.weather_api_key

# base_url variable to store url 
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
        city_name = get_location()
        print("current city is:",
            city_name)

# complete_url variable to store 
# complete url address 
        complete_url = base_url + "appid=" + api_key +"&q=" + city_name
# get method of requests module 
# return response object 
        response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
        x = response.json() 

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
        if x["cod"] != "404":
            
        

    # store the value of "main" 
    # key in variable y 
            y = x["main"] 

    # store the value corresponding 
    # to the "temp" key of y 
            current_temperature = y["temp"]  

    # store the value corresponding 
    # to the "pressure" key of y 
            current_pressure = y["pressure"] 

    # store the value corresponding 
    # to the "humidity" key of y 
            current_humidiy = y["humidity"] 

    # store the value of "weather" 
    # key in variable z 
            z = x["weather"] 

    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z 
            weather_description = z[0]["description"] 

    # print following values
             
            print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
                    "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
                    "\n humidity (in percentage) = " +
                    str(current_humidiy) +
                    "\n description = " +
                    str(weather_description)) 

        else: 
            print(" City Not Found ") 

        engine.say(y["pressure"])
        engine.runAndWait()
        engine.say('humidity')
        engine.runAndWait()
        engine.say(current_humidiy)
        engine.runAndWait()
        engine.say('temperature')
        engine.runAndWait()
        engine.say(current_temperature)
        engine.runAndWait()x['rating'],
            reverse=True)
        sorted_stores = [x['name'] for x in sorted_stores_data][:5]
        if "order" in translate:
            print("These are the stores: ")
            for store in sorted_stores:
                print(store)
            engine.say(sorted_stores)
            engine.runAndWait()
        if "popular" in translate:
            print("Most popular one is: ", sorted_stores[0])
        if "go" in translate:
            lat = sorted_stores_data[0]['geometry']['location']['lat']
            lng = sorted_stores_data[0]['geometry']['location']['lng']
            url = "http://maps.google.com/maps?q={},{}".format(lat, lng)
            webbrowser.open_new(url)
            engine.say(
                "Showing you directions to the store {}".format(
                    sorted_stores[0]))
            engine.runAndWait()
    elif "stores" in translate.split(" ") or "food" in translate.split(" ") or "restaurant" in translate:
        stores = []
        stores_data = {}
        query = filter_sentence(translate)
        stores, stores_data = nearby_places(
            config.google_api_key, personalized.city, query,
            personalized.latitude, personalized.longitude)
        print("These are the stores: ")
        for store in stores:
            print(store)
        engine.say(stores)
        engine.runAndWait()
        print("Where do you want to go:")
        engine.say("Where do you want to go:")
        engine.runAndWait()
    else:
        engine.say("please wait")
        engine.runAndWait()
        print(wikipedia.summary(translate))
        engine.say(wikipedia.summary(translate))
        engine.runAndWait()
        userInput3 = input("or else search in google")
        webbrowser.open_new('http://www.google.com/search?q=' + userInput3)
