list_states = ["Alabama", "Alaska", "Arizona", "Arkansas"]
list2_guessed = ["Alabama", "Alaska"]

data_dict = {
    "states not guessed": []
}

for state in list_states:
    if state not in list2_guessed:
        data_dict["states not guessed"].append(state)

print(data_dict)