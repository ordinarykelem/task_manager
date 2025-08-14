# Open the file emails.text in READ mode
# Read and split the data using \n to get a list
# Loop over the list of emails and print a generated username for each of them i.e username is all characters before the @


with open("emails.txt", "r") as file:
    # Read the content and split by newline to get a list
    emails = file.read().split("\n")

# Loop through the list of emails
for email in emails:
    # Extract the username (part before the @ symbol)
    username = email.split("@")[0]
    print(username)
