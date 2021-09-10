#Modules Imported
import pywhatkit as kit
import time

#Program loop started
while True:
    print()
    print ("Would you like to find and play a song (Yes/No)?")
    Answer = input ("Answer: ").upper()
    print()
    if Answer == "NO":
        print ("Thank You for using my app" )
        time.sleep(1)
        print ("Closing in...")
        i = 4
        while i > 1:                                                #Loop for countdown to exit
            i = i - 1
            time.sleep(0.5)
            print (i)
            time.sleep(0.5)
        break
    elif Answer == "YES":
        Song = input ("Enter song name: ").capitalize()
        while True:                                               #Loop for artist name
            print()
            print ("Do you know the artist for this song (Yes/No)?")
            answer_a = input ("Answer: ").upper()
            print ()
            if answer_a == "YES":
                Artist = input ("Enter artist name: ").capitalize()
                so_ar = Song + " by " + Artist
                kit.playonyt (so_ar)
                print ()
                print ("The song '" + Song + "'" + " by " + Artist + " is playing in your browser.")
                break
            elif answer_a == "NO":
                kit.playonyt (Song)
                print ()
                print ("The song '" + Song  + "' is playing in your browser.")
                break
            else:
                print ("Invalid Answer")
    else:
        print ("Invalid answer.")
