def main():
    bookPath = "books/frankenstein.txt"
    text = getText(bookPath)
    wordCount = getWordCount(text)
    charCount = getCharCountDict(text)
    sortedList = charCountDictToSortedList(charCount)

    # print header
    print(f"--- Begin report of {bookPath} ---")
    print(f"{wordCount} words found in the docutment")
    print()

    # print body
    for dict in sortedList:
        char = dict["char"]
        count = dict["num"]
        if char.isalpha():
            print(f"The {char} character was found {count} times")
    print("--- End report ---")


def getText(path):
    with open(path) as f:
        return f.read()

def getWordCount(text):
    return len(text.split())

def getCharCountDict(text):
    text = text.lower()
    countDict = dict()
    for char in text:
        if char not in countDict:
            countDict[char] = 1
        else:
            countDict[char] += 1
    return countDict

def charCountDictToSortedList(charDict):
    sortedList = []
    for char in charDict:
        sortedList.append({"char" : char, "num" : charDict[char]})
    sortedList.sort(reverse=True, key=sort_on)
    return sortedList


def sort_on(dict):
    return dict["num"]
main()