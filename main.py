import speech_recognition as sr
from googletrans import Translator

def recognize_and_translate(language_code='hi'):  # Default language is Hindi
    print(f"Received language code in recognize_and_translate: {language_code}")
    r = sr.Recognizer()
    translator = Translator()

    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)
        try:
            # Recognize speech using Google Speech Recognition
            speech_text = r.recognize_google(audio)
            print("You said: " + speech_text)
            
            # Translate the recognized speech to the selected language
            translated_text = translator.translate(speech_text, dest=language_code).text
            print("Translated Text: " + translated_text)
            
            return {'speech_text': speech_text, 'translated_text': translated_text}
        except sr.UnknownValueError:
            return {'speech_text': '', 'translated_text': '', 'error': 'Could not understand'}
        except sr.RequestError:
            return {'speech_text': '', 'translated_text': '', 'error': 'Could not request result from Google'}
        except Exception as e:
            return {'speech_text': '', 'translated_text': '', 'error': str(e)}
