names_path = "Mail Merge Project Start/Input/Names/invited_names.txt"
letter_path = "Mail Merge Project Start/Input/Letters/starting_letter.txt"

with open(names_path) as f:
    names = f.readlines()

for name in names:
    name = name.strip()
    with open(letter_path) as f:
        letter = f.read()
    letter = letter.replace("[name]", name)
    with open(
        f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}", "w"
    ) as f:
        f.write(letter)
