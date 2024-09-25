with open("day8\\Input\\Names\\invited_names.txt", "r") as name_list:
    names = name_list.readlines()
    
with open("day8\\Input\\Letters\\starting_letter.txt", "r") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        with open(f"day8\\Input\\Letters\\{stripped_name}.txt", "w") as new_letter_file:
            new_letter = letter_content.replace('[name]', stripped_name)
            new_letter_file.write(new_letter)
        
    