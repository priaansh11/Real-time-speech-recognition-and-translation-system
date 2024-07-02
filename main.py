import speech_recognition as sr
from googletrans import Translator

# Initialize recognizer and translator
r = sr.Recognizer()
translator = Translator()

def recognize_and_translate():
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)
        try:
            # Recognize speech using Google Speech Recognition
            speech_text = r.recognize_google(audio)
            print("You said: " + speech_text)
            
            # Translate the recognized speech to Hindi
            translated_text = translator.translate(speech_text, dest='hi').text
            print("Translated Text: " + translated_text)
            return speech_text, translated_text
        except sr.UnknownValueError:
            print("Could not understand")
            return None, None
        except sr.RequestError:
            print("Could not request result from Google")
            return None, None
        except Exception as e:
            print("Error occurred: " + str(e))
            return None, None
