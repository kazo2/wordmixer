from random import randint
import subprocess


def clipboardcopy(txt):
	"""Copies text to the keyboard"""
	cmd = 'echo ' + txt.strip() + '|clip'
	return subprocess.check_call(cmd, shell=True)


def main():
	words = input()
	# Add spaces to parentheses so they are counted as words too and thus randomized
	words = words.replace("(", "( ").replace(")", ") ")
	wordslist = words.split(' ')

	def randomizer(words, string):
		"""Randomizes words"""
		for i in range(len(words)):
			try:
				prevj = j  # The previous word
			except:
				pass
			j = words[randint(0, len(words) - 1)]
			if i:
				try:
					# Setting up grammar rules and such
					if j.isupper():
						# If the string is all uppercase we leave it as such
						string += f" {j}" 
					elif prevj.endswith((".", "?", "!")):
						# If the previous word ended with an end of statement
						# symbol then we will capitalize the first letter
						# of this word
						string += f" {j.title()}"

					elif prevj == "(" and j.isupper():
						# If the word is uppercase and there were parentheses
						# we leave it uppercase and don't add a space
						string += j
					elif prevj == "(":
						# If there were parentheses we do not add a space
						# to avoid doing ( this )
						string += j.lower()

					else:
						# Just a normal word in a sentence.
						string += f" {j.lower()}"
				except:
					if j.isupper():
						# If the word is uppercase we keep it that way
						string += f" {j}"
					else:
						# A normal word
						string += f" {j.lower()}"
			else:
				if j.isupper():
					# If its uppercase we do not capitalize it.
					string += j
				else:
					# First word will be capitalized.
					string += j.title()
			# Delete it to narrow down the words we've already pulled
			del (words[words.index(j)])
		print(string)  # Prints the string in console
		clipboardcopy(string)  # and copies it to the clipboard
	randomizer(wordslist, "")  # Runs the randomizer
	main()  # Loops the program once the input has been randomized.


if __name__ == "__main__":
	main()
