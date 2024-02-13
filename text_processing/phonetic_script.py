
import pandas as pd
import sqlite3

# Enter the input file path
file_path = 'phonetic_input.txt'

# Read the TSV file into a DataFrame with names ['words', 'frequency']
# Ignore the first 5 lines of the file with skiprows=5
df = pd.read_csv(file_path, skiprows=5, sep='\t', header=None, names=['words', 'frequency'])

# Filter words with 3 to 6 characters and frequency greater than or equal to 100
filtered_df = df[(df['words'].str.len() >= 3) & (df['words'].str.len() <= 6) & (df['frequency'] >= 100)]

# Transform words to lowercase and remove special characters and numbers
filtered_df['bangla_word'] = filtered_df['words'].str.lower().replace('[^a-zA-Z]', '', regex=True)

# Remove rows where bangla_word have less than 2 characters
filtered_df = filtered_df[filtered_df['bangla_word'].str.len() >= 2]

# Convert the 'frequency' column to integer
filtered_df['frequency'] = filtered_df['frequency'].astype(int)

# Save the bangla words to a text file
output_file_path = 'phonetic_wordlist.txt'
filtered_df['bangla_word'].to_csv(output_file_path, index=False, header=False)

# Save the output words and frequency to the database
sq = sqlite3.connect('phonetic_wordlist.db')
filtered_df[['bangla_word', 'frequency']].to_sql('words', sq, if_exists='replace', index=False)

# Disconnect from the db to ensure there are no memory leaks
sq.close()

# Display the filtered DataFrame
print(filtered_df[['bangla_word', 'frequency']])
