#Modules Imported
import time
import webbrowser as web
import pywhatkit as kit

#Program loop started
while True:                                           
    print()
    print ("Would you like to find a song (Y/N)?")
    Answer = input ("Answer: ").upper()
    print()
    if Answer == "N":
        print ("Thank you for using this program" )
        time.sleep(1)
        print ("Closing in...")
        i = 4
        while i > 1:                                 #Loop for countdown to exit
            i = i - 1
            time.sleep(0.5)
            print (i)
            time.sleep(0.5)
        break
    elif Answer == "Y":
        Song = input ("Enter song name: ").capitalize()
        while True:                                             #Loop for artist name
            print()
            print ("Do you know the artist for this song (Y/N)?")
            answer_a = input ("Answer: ").upper()
            print ()
            if answer_a == "N":
                break
            elif answer_a == "Y":
                Artist = input ("Enter artist name: ").title()
                Song = Song + " by " + Artist
                break
            else:
                print ("Invalid answer")
        while True:                                              #Loop for search only or play
            print ()
            print ("Shall I also play it for you (Y/N)?")
            answer_b = input ("Answer: ").upper()
            print ()
            if answer_b == "N":
                web.open (f'https://www.youtube.com/results?search_query={Song}')
                print ("The song " + Song + " has been searched in your browser.")
                break
            elif answer_b == "Y":
                kit.playonyt (Song)
                print ("The song " + Song + " is playing in your browser.")
                print ("There may be an ad first. Sorry I cannot skip it for you...yet.")
                break
            else:
                print ("Invalid answer.")
    else:
        print ("Invalid Answer")
