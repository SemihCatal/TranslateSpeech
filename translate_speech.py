import speech_recognition as sr
from googletrans import Translator
import languages

translator = Translator()


def speech_to_text(destination_language, source_language):
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language=source_lang)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    print(translator.translate(text, dest=destination_language, src=source_language))


destination_lang = languages.get_langcode('english')
source_lang = languages.get_langcode('turkish')
speech_to_text(destination_lang, source_lang)












