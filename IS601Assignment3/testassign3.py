def replace_in_file(filename,target,replacement):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    tempText = text.split()
    workingText = text.split()
    finalText = []
    count = 0
    print(workingText)
    for word in range(len(workingText)):
        if workingText[word] == target:
            finalText.append(replacement)
            count += 1
        else:
            finalText.append(tempText[word])
    print("Original:")
    print(text)
    print("\nReplaced Text:")
    print(" ".join(finalText))
    print("\nNumber of words changed: %d" % (count))

def main():
    # filename = input("Enter the filename: ")
    filename = "test2.txt"
    # target = input("Enter the word to be replaced: ")
    target = "John"
    # replacement = input("Enter the word to replace with: ")
    replacement = "brian"

    replace_in_file(filename, target,replacement)

if __name__ == "__main__":
    main()