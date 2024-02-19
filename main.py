# Open the file "input_text.txt" in read mode
with open("input_text.txt", "r") as file:
    # Read the contents of the file into the variable 'text'
    text = file.read()
    
    # Remove all occurrences of '*' from the text
    text_without_stars = text.replace("*", "")

# Open a new file "output_text.txt" in write mode
with open("output_text.txt", "w") as file:
    # Write the modified text (without stars) into the file
    file.write(text_without_stars)
