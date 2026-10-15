with open("login_logs.txt", "r") as file:
    logs = file.read()

records_count = 0
for record in logs.splitlines():
    records_count += 1


successful_logins = 0
failed_logins = 0

for login in logs.splitlines():
    if "FAILED" in login:
        failed_logins += 1
    elif "SUCCESS" in login :
        successful_logins += 1

username = input("What is your username? ").lower()
username_count = 0
case_logs = logs.lower().splitlines()

for user in case_logs:
    if username in user:
        username_count += 1

longest_record_name = ""
def longest_record(records):
    for record in records.splitlines():
        if len(record) > len(longest_record_name):
            longest_record_name = record
    return longest_record_name

print(f"Login attempts for {username}: {username_count}")
print(f"===== LOGIN AUDIT REPORT =====\nTotal login attempts: {records_count}\nSuccessful logins: {successful_logins}\nFailed logins: {failed_logins}\nThe longest record is: {longest_record(logs)}")
