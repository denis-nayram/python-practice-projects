with open("text_notes.txt", "r") as file:
    test = file.read()
    print(test)
line_count = 0
clean_test = test
for mark in ".,!?":
    clean_test = clean_test.replace(mark, "")
for line in test.splitlines():
    line_count += 1
print(line_count)
words = clean_test.lower().split()
print(words)
def count_words(text):
    return len(text.split())
print(count_words(clean_test))
new_word = input("Input any word of your choosing: ").lower()
print("The word you entered appears", words.count(new_word), "times")

def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest) :
            longest = word
    return longest
original_words = clean_test.split()
print("The longest word is", longest_word(original_words)) 