import speech_recognition as sr




sound = "websound_1.wav"



r = sr.Recognizer()
with sr.AudioFile(sound) as source:
    # r.adjust_for_ambient_noise(source)
    print("\nConverting Audio To Text ..... ")
    audio = r.listen(source)
# try:
    # text = r.recognize_google(audio)
    # print("Converted Audio Is : " + text)
# except Exception as e:
    # print("Error {} : ".format(e))
    
    

text =  r.recognize_google(audio,language = 'vi-VN')
print(text)