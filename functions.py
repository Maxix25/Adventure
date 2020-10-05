import sys
import time
# Delay Print
def printf(sentence: str):
    # Print one character at a time
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        # time.sleep(0.05)
    print()
