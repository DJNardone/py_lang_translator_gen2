import csv

def intro():
  print(f'Welcome to the Spanish & French translator. \nPlease enter an English word and press "Enter".')
  print('\nType "done" at any time to exit')

def exit():
  print(f'\nThanks for using the translator app.  Have a Nice Day!')

translations = {}
done = False

with open("translations.csv", "r") as words:
  reader = csv.DictReader(words, delimiter=",")
  for line in reader:
    english = line["English"].lower()
    spanish = line["Spanish"].lower()
    french = line["French"].lower()
    translations[english] = [spanish,french]
    
intro()

while not done:
  word = input("\nPlease enter an English word to Translate. ")
  word = word.lower()
  
  if word == "done":
    done = True
    exit()
  elif word in translations:
    print(f'\nSPANISH: {translations[word][0]}')
    print(f'\nFRENCH: {translations[word][1]}')
  else:
    print("\nError, word is not in Dictionary.")