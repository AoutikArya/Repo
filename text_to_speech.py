import pyttsx3

t=pyttsx3.init()
ans=input("enter text to convert :")

t.say(ans)
t.runAndWait()