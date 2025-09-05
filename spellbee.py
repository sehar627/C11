import speech_recognition as sr
import pyttsx3
import random
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def talk(text):
    engine.say(text)
    engine.runAndWait()  
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            #listener.adjust_for_ambient_noise(source, duration=0.5)
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
    except:
        return ""

def run_spellbee_game():
    words = ["example", "python", "programming", "challenge", "assistant", "computer", "holiday", "elephant"]
    score = 0
    
    talk("Hello! Let's play the Spell Bee Game. I will say a word and you have to spell it. Say stop anytime to quit.")
    time.sleep(1)

    while True:
        word = random.choice(words)
        talk(f"Spell the word {word}")
        time.sleep(0.5)  

        user_answer = take_command()

        if not user_answer:
            talk("I didn't catch that. Please try spelling the word again.")
            continue

        if "stop" in user_answer:
            talk(f"Game over! Your final score is {score}")
            break

        if user_answer.replace(" ", "") == word:
            score += 1
            talk(f"Correct! Your score is {score}")
        else:
            talk(f"Incorrect. The correct spelling is {word}. Your score is {score}")

        time.sleep(0.5)

run_spellbee_game()
