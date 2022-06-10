"""
Program: numberGuessGUI.py page 269-272
Author: Md Suhel Rana 06/07/2022

GUI-based version of the number guessing game from chapter 2.
"""

from breezypythongui import EasyFrame
import random
# other imports

class GuessingGame(EasyFrame):
	"""Plays a gussing game with the user."""
	# definition of the __init__() method which is our class constructor
	def __init__(self):

		# call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "Guesing Game", width = 240, height = 180)

		# Initialize the instance variables for the class
		self.myNumber = random.randint(1, 100)
		self.count = 0

		# Create and add widgets to the window
		greeting = "Guess a number between 1 and 100."
		self.hintLabel = self.addLabel(text = greeting, row = 0, column = 0, sticky = "NEWS", columnspan = 2)
		self.addLabel(text = "Your guess", row = 1, column = 0)
		self.guessField = self.addIntegerField(value = 0, row = 1, column = 1)	
		self.nextButton = self.addButton(text = "Next", row = 2, column = 0, command = self.nextGuess)
		self.newButton = self.addButton(text = "New Game", row = 2, column = 1, command = self.newGame)

	# The event handling methods for the buttons
	def nextGuess(self):
		"""Processes the users next guess."""
		self.count += 1
		guess = self.guessField.getNumber()
		# Logic to determine the game's outcome
		if guess == self.myNumber:
			self.hintLabel["text"] = "You've guessed it in " + str(self.count) + " attempts!"
			self.newButton["state"] = "disabled"

		elif guess < self.myNumber:
			self.hintLabel["text"] = "Sorry, too small!"

		else:
			self.hintLabel["text"] = "Sorry, too large!"	

	def newGame(self):
		"""Reset the data and GUI to their original states."""
		self.myNumber = random.randint(1, 100)
		self.count = 0
		self.hintLabel["text"] = "Guess a number between 1 and 10."
		self.guessField.setNumber(0)
		self.newButton["state"] = "normal"

# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	GuessingGame().mainloop()

if __name__ == "__main__":	

# global call to the main() method
	main()
