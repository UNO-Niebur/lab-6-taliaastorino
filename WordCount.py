#WordCount.py
#Name: Talia Astorino
#Date: 03/01/2026
#Purpose: Calculate the total number of lines, words, and characters in a text file.

def main():
  try:
    textFile = open("gettysberg.txt", 'r')

    lineCount = 0
    wordCount = 0
    charCount = 0
    
    for line in textFile:
      lineCount += 1
      wordCount += len(line.split())
      charCount += len(line)

    textFile.close()

    print("Lines:", lineCount)
    print("Words:", wordCount)
    print("Characters:", charCount)

  except FileNotFoundError:
    print("File not found.")
  
if __name__ == '__main__':
  main()
