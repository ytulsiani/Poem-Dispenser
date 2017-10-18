import sys
import json
from pprint import pprint
from enum import Enum
from random import *
class Genre(Enum):
	#change so it reads the genres from the JSON files
	freeverse = "free verse"
	nature = "nature"
	love = "love"
	depression = "depression"
	politics = "politics"

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
	if "random" in inputMessage:
		poem = findRandomPoem()
		text = poem.text
		author = poem.author
		genre = poem.genre
		print('Here is a poem by {}. It is of the genre {}. <br/> {}'.format(author, genre, text))
	else:
		for genre_name, genre in Genre.__members__.items():
			if genre.value in inputMessage:
				poem = findPoemByGenre(genre)
				text = poem.text
				author = poem.author
				genre = poem.genre
				print('Here is a poem by {}. It is of the genre {}. \n {}'.format(author, genre, text))
				return
		print("Your message is not valid. Please ask for a random poem or choose a genre to get your poem. You can choose from free verse, nature, love, depression, and politics")

if __name__ == '__main__':
    main()
