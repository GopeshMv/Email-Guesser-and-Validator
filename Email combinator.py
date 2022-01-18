import csv
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email):
    if(re.fullmatch(regex, email)):
        return True
    return False
    # def isValid(email):
    #    if(re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email) != None):
    #        return True
    #    return False


def guesser(firstName, lastName, domain):
    guesses = []
    guesses.append(f"{firstName}{lastName}@{domain}")
    guesses.append(f"{firstName}.{lastName}@{domain}")
    guesses.append(f"{firstName}_{lastName}@{domain}")
    guesses.append(f"{firstName[0]}{lastName}@{domain}")
    guesses.append(f"{firstName[0]}.{lastName}@{domain}")
    guesses.append(f"{firstName[0]}_{lastName}@{domain}")
    guesses.append(f"{firstName}{lastName[0]}@{domain}")
    guesses.append(f"{firstName}.{lastName[0]}@{domain}")
    guesses.append(f"{firstName}_{lastName[0]}@{domain}")
    guesses.append(f"{lastName}{firstName}@{domain}")
    guesses.append(f"{lastName}.{firstName}@{domain}")
    guesses.append(f"{lastName}_{firstName}@{domain}")
    guesses.append(f"{lastName}{firstName[0]}@{domain}")
    guesses.append(f"{lastName}.{firstName[0]}@{domain}")
    guesses.append(f"{lastName}_{firstName[0]}@{domain}")
    guesses.append(f"{firstName}@{domain}")
    guesses.append(f"{lastName}@{domain}")
    guesses.append(f"{firstName[0]}@{domain}")
    guesses.append(f"{lastName[0]}@{domain}")
    guesses.append(f"{firstName[0]}{lastName[0]}@{domain}")
    guesses.append(f"{firstName[0]}.{lastName[0]}@{domain}")
    guesses.append(f"{firstName[0]}_{lastName[0]}@{domain}")
    guesses.append(f"{lastName[0]}{firstName[0]}@{domain}")
    guesses.append(f"{lastName[0]}.{firstName[0]}@{domain}")
    guesses.append(f"{lastName[0]}_{firstName[0]}@{domain}")
    return guesses


text = open("Guesses.txt", "w")


with open('Input.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        # print(f'\t{row[0]} is the first Name.{row[1]} is the second name.{row[2]} is the domain.')
        z = guesser(row[0], row[1], row[2])
        for element in z:
            email = str(element)

            if(check(email) == True):
                text.write(f'{row[0]} combination is : ')
                text.write(element + "\n")
                text.write("\n")
            else:
                continue

text.close()
