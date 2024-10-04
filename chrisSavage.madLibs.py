# Christopher Savage
print("Please provide the following words")
plural_noun = input("Plural Noun:  ")
animal = input("Animal:  ")
adjective = input("Adjective:  ")
verb = input("Verb:  ")
exclamation = input("Exclamation:  ")
verb2 = input("Another Verb:  ")
verb3 = input("One more Verb:  ")
emotion = input("Emotion:  ")
food = input("Food:  ")
print(f"""The other day, I was really in trouble. It all started when I saw a very
{verb.lower()}{animal.lower()} down the hallway. "{exclamation.capitalize()}!" I {verb2.lower()}ed. But all
I could think to do was to {verb2.lower()} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3.lower()}
right in front of my family. Then all together we ate {food.lower()}! 
This turned out to be the {emotion.lower()} day of my life! 
The only day better than this was the one with the {plural_noun.lower()}! """)