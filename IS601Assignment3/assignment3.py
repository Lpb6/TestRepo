def replace_in_file(filename,target,replacement):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    replaced_text = text.replace(target,replacement)
    count = replaced_text.count(replacement)
    print("Original:")
    print(text)
    print("\nReplaced Text:")
    print(replaced_text)
    print("\nNumber of words changed: %d" % (count))

def main():
    filename = input("Enter the filename: ")
    target = input("Enter the word to be replaced: ")
    replacement = input("Enter the word to replace with: ")

    replace_in_file(filename, target,replacement)

if __name__ == "__main__":
    main()