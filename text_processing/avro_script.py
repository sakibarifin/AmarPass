
input_file_path = 'avro_input.txt'
output_file_path = 'avro_wordlist.txt'

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:

    # Loop over each line of the file
    for line in input_file:
        # Ignore lines starting with '/'
        if not line.startswith('/'):
            # Split the line into words
            words = line.split()

            # Check if there's at least one word in the line
            if len(words) > 0:
                # Extract the first word in lowercase
                first_word = words[0].strip().lower()

                # Check if the first word consists only of alphabetical characters
                if first_word.isalpha():
                    # Save the first word to the output file
                    output_file.write(first_word + '\n')
