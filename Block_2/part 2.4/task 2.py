string = input() + " "
i = 0
count = 1
new_string = ""

while string[i] != " ":
    if string[i] == string[i + 1]:
        count += 1
    else:
        new_string += string[i] + str(count)
        count = 1
    i += 1

print(new_string)