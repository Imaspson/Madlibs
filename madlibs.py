#string concatenation or how to put strings togheter
#we want to create a string that says "subscribe to ______"
#youtuber = "Samuel" #some string variable

#a few ways to do this:
#print("subscribe to " + youtuber) #not so good
#print("subscribe to {}".format(youtuber)) #ok
#print(f"subscribe to {youtuber}") #the most staightforward

adj = str(input("Adjective: "))
verb1 = str(input("First verb: "))
verb2 = str(input("Second verb: "))
famous_person = str(input("Famous person: "))

madlib = f"Computer programming is so {adj}! It makes me so excited \
all the time because I love to {verb1}. Stay hydrated and {verb2} \
like you are {famous_person}!"
