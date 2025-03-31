"""Program providing silly names inspired from the show Psych"""

#import sys
import random

print("Welcome to the Psych 'Sidekick Name Picker.'\n")
print("A name just like Sean would pick for Gus:\n")

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
         "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
         'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 
         'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
         'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso', 
         'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckelberry',
          'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny', 
          'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid', 
          '"Mr. Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 
          'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy', 
          'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'", 
          'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam', 
          'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
            'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'BoogerBottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck', 
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 
        'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater', 
        'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 
        'Johnson', 'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles', 
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 
        'Overturf', 'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 
        'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff', 
        'Sugar-Gold', 'Swackhammer', 'Tippins', 'Weiners', 
        'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')

# while loop keeping the program running til we tell it to stop.
while True:
    firstName = random.choice(first)

    lastName = random.choice(last)

    SILLYNAME = f"{firstName} {lastName}"

    print("\n")
    #without fstring
    #print("{} {}".format(firstName, lastName), file=sys.stderr)
    print(SILLYNAME)
    print("\n")
    try_again = input("Try Again? \n(Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break

input("Press Enter to exit.")
