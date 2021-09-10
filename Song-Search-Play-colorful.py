# Some variables used
c = 4 
g = 315

#Defining function to print coloured text
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

#Program loop started
while True:
    print()
    print ("Would you like to find a song (Y/N)?")
    Answer = input ("Answer: ").upper()
    print()
    if Answer == "N":
        import time
        print ("Thank you for using this program" )
        time.sleep(1)
        print ("Closing in...")
        while c > 1:                                 #Loop for countdown
            c = c - 1
            g = g - 70
            colored_num = colored(0, g, 0, c)
            time.sleep(0.5)
            print (colored_num)
            time.sleep (0.5)
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
        while True:                                             #Loop for search only or play
            print ()
            print ("Shall I also play it for you (Y/N)?")
            answer_b = input ("Answer: ").upper()
            print ()
            if answer_b == "N":
                import webbrowser
                webbrowser.open (f'https://www.youtube.com/results?search_query={Song}')
                print ("The song " + Song + " has been searched in your browser.")
                break
            elif answer_b == "Y":
                import pywhatkit as kit
                kit.playonyt (Song)
                print ("The song " + Song + " is playing in your browser.")
                colored_yet = colored (255, 0, 0, "YET")
                print ("There may be an ad first. Sorry I cannot skip it for you..." + colored_yet)
                break
            else:
                print ("Invalid answer.")
    else:
        print ("Invalid Answer")