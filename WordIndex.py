#WordIndex.py
#Name: Talia Astorino
#Date: 03/01/2026
#Purpose: Create a word to line to number index from a text file.

def main():
  try:
    words = {} #create an empty dictionary

    with open("fish.txt", 'r') as textFile:
      lineNumber = 0

    for line in textFile:
      lineNumber += 1
      lineWords = line.split()

      for word in lineWords:
        word = word.lower().strip(".,!?")

        if word in words:
          if lineNumber not in words[word]:
            words[word].append(lineNumber)
        else:
          words[word] = [lineNumber]

    for word in sorted(words):
      print(word, ":", words[word])

  except FileNotFoundError:
    print("File not found.")


if __name__ == '__main__':
  main()
