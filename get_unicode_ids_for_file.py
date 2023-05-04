with open("filename.txt") as file:
    for line in file:
        char_ids = []
        for char in line:
            char_ids.append(char)

        print(char_ids)
