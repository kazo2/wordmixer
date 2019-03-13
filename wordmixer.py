from random import randint
import subprocess


def clipboardcopy(txt):
	cmd = 'echo ' + txt.strip() + '|clip'
	return subprocess.check_call(cmd, shell=True)


def main():
	words = input()
	words = words.replace("(", "( ").replace(")", ") ")
	wordslist = words.split(' ')

	def randomizer(words, string):
		for i in range(len(words)):
			try:
				prevj = j
			except:
				pass
			j = words[randint(0, len(words) - 1)]
			if i:
				try:
					if j.isupper():
						string += f" {j}"
					elif prevj.endswith((".", "?", "!")):
						string += f" {j.title()}"

					elif prevj in ["(", ")"] and j.isupper():
						string += j
					elif prevj in ["(", ")"]:
						string += j.lower()

					else:
						string += f" {j.lower()}"
				except:
					if j.isupper():
						string += f" {j}"
					else:
						string += f" {j.lower()}"
			else:
				if j != j.upper():
					string += j.title()
				else:
					string += j
			del (words[words.index(j)])
		if len(words) > 1 and string.lower() == str(words.lower()):
			randomizer(words, "")
		print(string)
		clipboardcopy(string)
	randomizer(wordslist, "")
	main()


if __name__ == "__main__":
	main()
