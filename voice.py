import time

import speech_recognition as sr
import pyttsx3
import speech
import features
# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak
speech.stock_voice()
speech.config_test()
while 1:
    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)


            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            if "weather" in MyText or "temperature" in MyText:
                SpeakText(features.weather('Boise, US', 'celsius'))
            elif 'news' in MyText:
                features.npr()
            elif 'search' in MyText:
                prompt_satisfied = False
                search_num = 0
                while prompt_satisfied != True:
                    SpeakText('What Would You Like To Search For ?' )
                    search_queue = r.listen(source2)
                    search_queue = r.recognize_google(search_queue)
                    search_results = features.search(search_queue,search_num)
                    SpeakText(search_results[0])
                    time.sleep(2)
                    SpeakText(search_results[1])
                    time.sleep(2)
                    SpeakText('Would You Like to hear from a different source? ')
                    check_prompt = r.listen(source2)
                    check_prompt = r.recognize_google(check_prompt)
                    if 'no' in check_prompt:
                        prompt_satisfied = True
                    elif 'yes' in check_prompt:
                        search_queue += 1
            elif "hey darwin" not in MyText:
                print("Did you say ", MyText)
                SpeakText(MyText)
            else:
                SpeakText('Hello My name is darwin I dont do much yet but I hope to be of great use')

    except sr.RequestError as e:
        continue

    except sr.UnknownValueError:
        continue
