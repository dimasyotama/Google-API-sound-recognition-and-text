########################
## Dimas Yoga Pratama ##
##  More From Google  ##
##    09-060-2018     ##
########################

from gtts import gTTS
import os
import speech_recognition as sr


class ada():
    def rules(self):
        print("--- Selamat Datang di Pogram Python --- ")
        print("--- 1. tekan 1 untuk ketik teks dan mengucapakannya --- ")
        print("--- 2. untuk mengucapkan dengan mic ---- ")
        print("===-Note kode bahasa=====")
        print("===Khusus untuk nomor 2 harus memakai bahasa inggris")
        print("===Indonesia = id")
        print("===Inggris = en")
    def teks(self):
        angka = str(input("Masukkan angka "))
        if angka == '1':
            teks = str(input("Masukkan kalimat : "))
            bahasa = str(input("Masukkan kode = "))
            nama_file = str(input("Masukkan Nama File : "))
            obj = gTTS(text=teks,lang=bahasa,slow=False)
            obj.save('%s.mp3'%(nama_file))
            os.system('mp321 %s.mp3'%(nama_file))
        elif angka == '2':
            r =sr.Recognizer()
            with sr.Microphone() as source:
                print("Talk with English Languange : ")
                audio = r.listen(source)
                try:
                    print("Result what do you talk :" + r.recognize_google(audio))
                except sr.UnknownValueError:
                    print("Word doesnt recognize!?!?!!?")
                except sr.RequestError as e: 
                    print("Google API not recognizing the word.Please Try Again")
            
        

if __name__=="__main__":
    a = ada()
    a.rules()
    a.teks()
