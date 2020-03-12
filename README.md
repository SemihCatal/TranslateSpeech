# TranslateSpeech
Translate speech to text using SpeechRecognition and googletrans libraries. 

## NOTE:
- Licensing information for SpeechRecognition can be found within the [SpeechRecognition] README.
- [Googletrans] is licensed under the MIT License.

[SpeechRecognition]: https://github.com/Uberi/speech_recognition
[Googletrans]:  https://github.com/ssut/py-googletrans

## Requirements:
- Python 3.3+ (required)
- PyAudio 0.2.11+ (required only if you need to use microphone input, Microphone)
- Googletrans 2.3.0+ (required)
- SpeechRecognition 3.8.0 (required)


## How to Install:
1. Create a virtualenv
    1. $ virtualenv venv -p python3
    1. $ source venv/bin/activate
2. Install Speech Recognition, PyAudio, and Googletrans
    1. $ pip install SpeechRecognition
    1. $ pip install googletrans
    1. $ pip install pyaudio
3. Run file
    1. $ python translate_speech.py
