# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

#variable to hold story of Dracula and assign it to the result of the readBook function
dracula = readBook()

# Most popular word in Dracula
# Dictionary for word frequency and define "KEY" as the word
word_freq = {}
key = ""

# Find the word that shows up the most often regardless of case of letter popular Word
# appearances is the "Value" of he key in the word_freq library
appearances = 0

# Loop through the dracula string and add each word to the word_freq dictionary
for word in dracula.split():
 if word in word_freq:
   word_freq[word] += 1
   
# Loop through the word_freq dictionary and find the word that shows up the most often
# regardless of case of letter popular Word
 else:
   word_freq[word] = 1
for word in word_freq:

# if the word_freq dictionary value is greater than the appearances variable, then the
# word_freq dictionary key becomes the key variable and the word_freq dictionary value
# becomes the appearances variable
  if(word_freq[word] > appearances):
    appearances = word_freq[word]
    key = word

print(f" {key} appears {appearances} times throughout the entire story about Dracula")
print()

# How many unique four-letter words are in the book
# Create dictionary for unique four-letter words and define "KEY" as the word
fourLetterWords = {}
key = ""

# Count the number of unique four-letter words in the dracula string
appearances = 0

# Determine if has four letters, then add to dictionary if not already in dictionary
for word in dracula.split():
  if len(word) == 4:
    if word in fourLetterWords:
      fourLetterWords[word] += 1
    else:
      fourLetterWords[word] = 1
# Loop through the fourLetterWords dictionary and find the word that shows up the most often      
for word in fourLetterWords:
  if(fourLetterWords[word] > appearances):
    appearances = fourLetterWords[word]  
    key = word
    
print(f" Four letter words appear {appearances} times throughout the entire story about Dracula")
print()

# Every word that shows up more than 500 times and how many times it shows up throughout the book
# Create dictionary for word frequency and define "KEY" as the word
word_popular = {}
key = ""
appearances = 0
# Loop through the dracula string and add each word to the word_popular dictionary
for word in dracula.split():
  if word in word_popular:
    word_popular[word] += 1
  else:
    word_popular[word] = 1
    
# regardless of case of letter popular Word
#print statement before loop so it only prints once
print(f" I noticed that these words show up ten or more times: ")
print()

## Loop through the word_popular dictionary and find the word that shows up the more than 500 times
for word in word_popular:
  if(word_popular[word] > 500):
    appearances = word_popular[word]
    key = word
          
    print(f"{key} {appearances}")
    


