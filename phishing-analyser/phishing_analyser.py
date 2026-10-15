with open("messages.txt", "r") as file:
    analyser = file.read()

number_of_messages = 0 
for message in analyser.splitlines():
    number_of_messages += 1 

print(f" There are {number_of_messages} messages in the file")

word_searcher = input("Search for any word of your choosing: ").lower()
case_analyser = analyser.lower().splitlines()
message_counter = 0

for message in case_analyser:
    if word_searcher in message:
        message_counter += 1

print(f"this word {word_searcher} appears in a total of {message_counter} messages")        

warning_words = ["urgent", "password", "verify", "prize"]
warning_words_counter = 0 
for message in case_analyser:
    for word in warning_words:
        if word in message:
            warning_words_counter += 1
            break

print(f"Suspicious messages found: {warning_words_counter}")

if warning_words_counter > 0:
    print("This message is suspicious")
else: 
    print("No suspicious message found")

def count_messages(text):
    counting_messages_in_funtion = 0
    for line in text:
        counting_messages_in_funtion += 1 
    return counting_messages_in_funtion

print(count_messages(case_analyser))

def longest_message(messages):
    longest_message_count = ""
    for message in messages:
        if len(longest_message_count) < len(message):
            longest_message_count = message
    return longest_message_count
print("This is the longest message:", longest_message(analyser.splitlines())

