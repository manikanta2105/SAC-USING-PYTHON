

filename = input("Enter the Filename: ")

try:
    with open("filename", 'r') as file:
        text = file.read()  # read whole content as a string
        words = re.findall(r'\b\w+\b', text)  # find all words using regex
        unique_words = sorted(set(words))

    print("Unique words in alphabetical order:")
    for word in unique_words:
        print(word)

except FileNotFoundError:
    print("File not found")
