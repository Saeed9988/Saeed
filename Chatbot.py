print("🤖 Hallo! Ich bin ein einfacher Chatbot Entwickelt von Saeed Hussain. Lass uns ein bisschen reden!")

name = input("Wie heisst du ? Ich heisse : ")
print (f"Schön dich kennenzulernen,  {name}  😊")

stimmung = input("Wie geht es dir heute? (gut / müde / normal): ")

if stimmung == "gut":
    print("Super! Bleib so positiv 💪")
elif stimmung == "müde":
    print("Oh nein 😔 Ruh dich etwas aus und trink etwas Warmes ☕")
else:
    print("Ich hoffe, dein Tag wird besser! 🌞")

hobby = input("Was ist dein Lieblingshobby? ")
print (f"Toll! Ich mag auch {hobby} , obwohl ich nur ein Roboter bin 😄")

print("Es war schön, mit dir zu sprechen! Bis bald, " + name + " 👋")   