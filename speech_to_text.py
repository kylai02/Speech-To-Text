import speech_recognition as sr


recog = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    recog.adjust_for_ambient_noise(source)
    print('Start listening...')
    while True:
        audio = recog.listen(source)
        message = recog.recognize_google_cloud(
            audio_data=audio,
            credentials_json='key.json',
            language='en'
        )

        print(message)