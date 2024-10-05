

def wordCounter(content: str):
    words = content.split()
    return words

def countCharacters(content: str):
    counter = {}
    for char in content:
        char = char.lower()
        if char.isalpha() == True:
            counter[char] = counter.get(char, 0) + 1
    return counter
    
    
    

def main():
    file = open("./books/frankenstein.txt", "r")
    content = file.read()
    
    print(f"-- This is a report of the {file.name} book--")
    print()
    print(f"{len(wordCounter(content))} words were found in the document!")
    print()
    print("The number of individual character count are the following:")
    print() 
    counter = countCharacters(content)
    for k,v in counter.items():
        print(f"The '{k}' character was found {v} times")
        
    
    print("--End of report--")
    file.close()
main()