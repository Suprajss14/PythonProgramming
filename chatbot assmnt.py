print("Hey! I am Chatboy")
name=input("What's your name ")
print("Hey ",name,"\n In what do you need help")
print("Type 'not reieved conformation mail' for mail ID related quieries")
print("Type 'not able to connect to zoom' for zoom related quieries")
print("Type 'Mahan baba voice is audible but no video' for video related quieries")
print("Type 'Mahan baba voice is breaking' for voice issue related quieries")
print("Type 'zoom link is not activated' for activation related quieries")
problem= input("What help you need:")
if problem == "not recieved confirmation mail":
    print("let us resend it again")
elif problem == "not able to connect to zoom":
    print("try reinstalling the application")
    zoom=input("registered zoom ID")
    if zoom == "NA":
        print("We are happy we could help")
    else:
        print("get into other account")
elif problem == "Mahan baba voice is audible but no video":
    print("ensure that all the permission are enabled")
elif problem == "Mahan Baba voice breaking":
    print("check your internet connection then try again")
elif problem == "Zoom link is not activated":
    print("wait for sometime, we will activate it soon")
else:
    print("my problem is not mentioned above")
