#MadLib Assignment
# create list with all types of words user should be prompted for
blanks = [
  'occupation', 
  'noun',
  'verb',
  'adjective',
  'noun2',
  'verb2',
  'adjective2',
  'noun3',
  'verb3',
  'noun4',]

# create empty dictionary to hold input words
input_words = {}

# explain what the meaning is for verb, noun and adjective 
print("Hint: a Verb is an action. A noun is a person/place/thing. An adjective describes a person/place/thing.")
print(" ")

# ask user for words for each item in blanks list
for blank in blanks:
  word_choice = input(f'Enter {blank}: ')
  input_words[blank] = word_choice

print("")
print("Here is your creation!")
print("")
# print madlib story with users words
print (f"Today a {input_words['occupation']} named {input_words['noun']} came to our school to talk to us about her job.\nShe said the most important skill you need to know to do her job is to be able to {input_words['verb']} around a(n) {input_words['adjective']} {input_words['noun2']}.\nShe said it was easy for her to learn her job because she loved to {input_words['verb2']} when she was my age--and that helps a lot! \nIf you're considering her profession, I hope you can be near a(n) {input_words['adjective2']} {input_words['noun3']}. That's very important! \nIf you get too distracted in that situation you won't be able to {input_words['verb3']} next to a(n) {input_words['noun4']}!")