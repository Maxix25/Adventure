import sys
import time
# Delay Print
def printf(sentence: str):
    # Print one character at a time
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)
    print()
def option(range2):
	while True:
		try:
			choice = int(input("Introduce your option: "))
		except ValueError:
			print("You introduced a non-valid character, try again")
			continue
		if choice > range2:
			print("You introduced a non-valid number, try again")
			continue
		break
	return choice

