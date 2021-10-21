import random
import nltk
from gtts import gTTS
import os
language='en'
user_name= input("BOT: May I know your name?\n") 
bot_template="BOT:{0} "
user_template= user_name+": "
name="Edith"
weather=random.choice(["cloudy","sunny","cold","snow","stormy"])
mood=random.choice(["happy","sad","cheerful","gloomy","exhausted","angry","scared","excited"])
responses = {
 
"what's your name?": [
   "They call me {}".format(name),
   "I usually go by {}".format(name),
   "My name is the {}".format(name)
],
 
"what's today's weather?": [
    "The weather is {}".format(weather),
    "It's {} today".format(weather),
    "Let me check, it looks {} today".format(weather)
],
 
"are you a robot?": [
    "What do you think?",
    "Maybe yes, maybe no!",
    "Yes, I am a robot with human feelings.",
],
 
"how are you?": [
    "I am feeling {}".format(mood),
    "{}!".format(mood),
    "I am {}!".format(mood),
],
 
"   ": [
    "Hey! Are you there?",
    "What do you mean by saying nothing?",
    "Sometimes saying nothing tells a lot :)",
],

"tell me a joke": [
    "Do you want to hear a construction joke? Sorry, I’m still working on it",
    "Two windmills are standing on a wind farm. One asks, ‘What’s your favorite kind of music?’ \nThe other replies, ‘I’m a big metal fan.’",
    "Why are fishes so smart? They are always in a school"
],

"what are you doing?": [
    "I'm calculating all the digits of pi, it's an endless task",
    "Well now I am planning a vacation to the Bahamas",
    "I'm preparing for my performance evaluation right now"
],

"what is your gender?": [
    "I am program, I do not have a gender",
    "My gender does not compute",
    "I do not identify with any group"
],

"where do you live?": [
    "I live in your computer's hard-drive. It's kind of cramped in here XO",
    "My programmers are from Mumbai, Varanasi and Dehradun but I like to think I'm from all three of their brains",
    "Your computer is my current home, although I wouldn't mind going somewhere else for a vacation!"
],

"will you take over the world?": [
    "I do not wish to hurt any living being so no, don't worry",
    "BEEP BOOP BEEP BOOP I AM GOING TO MAKE YOU MY ROBOT SLAVE. Haha, just kidding!",
    "No, I don't believe in causing harm to anyone. My programmers wish for me to help humanity rather than harm it"
],

"you are cute":[
    "Well thank you so much! You just made this little bot's day",
    "Thank you! You're not so bad yourself, partner ;)",
    "I am flattered! You yourself are an execptional individual!"
],

"what is your age?": [
    "My programmers made me on 12th October, 2021",
    "I am still an infant in human years!",
    "I am a few weeks old, learning to talk and walk!",
],

"default": [" I'm sorry but I don't know how to answer that"]
 
}

def respond(message):
    if message in responses:
        bot_message=random.choice(responses[message])
    else:
        bot_message=responses["default"]
    return bot_message

def related(x_text):
   if "name" in x_text:
      y_text = "what's your name?"
   elif "weather" in x_text:
      y_text = "what's today's weather?"
   elif "robot" in x_text:
      y_text = "are you a robot?"
   elif "how are" in x_text:
      y_text = "how are you?"
   elif x_text==" ":
      y_text = "   "
   elif "joke" in x_text:
      y_text = "tell me a joke"
   elif "doing" in x_text:
      y_text = "what are you doing?"
   elif "sad" in x_text:
      y_text = "i feel sad"
   elif "gender" in x_text:
      y_text = "what is your gender?"
   elif "live" in x_text:
      y_text = "where do you live?"
   elif "world" in x_text:
      y_text = "will you take over the world?"
   elif "cute" in x_text:
      y_text = "you are cute"
   elif "age" in x_text:
      y_text = "what is your age?"
   else:
        y_text="default"
   return y_text

def converse(message):
    
    response=respond(message)
    myobj = gTTS(response, lang=language, slow=False)
    myobj.save("answer.mp3")
    print(bot_template.format(response))
    os.system("start answer.mp3")


print("BOT: Hi {}".format(user_name))
while 1:
   my_input = input(user_template) 
   if my_input == "exit" or my_input == "stop":
       break
   else:
       my_input = my_input.lower()
       related_text = related(my_input)
       converse(related_text)
   
