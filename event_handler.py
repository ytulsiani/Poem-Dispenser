import sys
import json
import textwrap
from pprint import pprint
from enum import Enum
from random import *
class Genre(Enum):
	#change so it reads the genres from the JSON files
	freeverse = "free verse"
	nature = "nature"
	love = "love"
	limerick = "limerick"
	haiku = "haiku"

class Poem:
	text = ""
	author = ""
	genre = ""
	def __init__(self, text, author, genre):
		self.text = text
		self.author = author
		self.genre = genre

	def make_poem(text, author, genre):
		poem = Poem(text, author, genre)
		return poem


def findRandomPoem():
	p = findPoemByGenre(choice(list(Genre)))
	return p
def findPoemByGenre(genre):
	json_data=open('Poems.json').read()
	data = json.loads(json_data)
	poem = data[genre.value][str(randint(0, 5))]
	text = poem['text']
	author = poem['author']
	#needs to get poem from json file
	p = Poem(text, author, genre.value)
	return p


def main():
	inputMessage = sys.argv[1]
	inputMessage = inputMessage.lower()
	if ("hi" in inputMessage or "hello" in inputMessage):
		print("Hi, I'm PoBot. Ask me for a random poem to get started. Or, if you'd like a poem related to one of the following topics, let me know: haiku, free verse, limerick, love, or nature.")
	elif "random" in inputMessage:
		poem = findRandomPoem()
		text = poem.text
		author = poem.author
		genre = poem.genre
		print('Here is a poem by {}. It is of the genre {}. \n'.format(author, genre))
		print(text)
	else:
		for genre_name, genre in Genre.__members__.items():
			if genre.value in inputMessage:
				poem = findPoemByGenre(genre)
				text = poem.text
				author = poem.author
				genre = poem.genre
				print('Here is a poem by {}. It is of the genre {}. \n'.format(author, genre))
				print(text)
				return
		print("Your message is not valid. Please ask for a random poem or choose a genre to get your poem. You can choose from free verse, nature, love, limerick, and haiku")

if __name__ == '__main__':
    main()
