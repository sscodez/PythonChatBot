input_file = 'output_file.txt'  # Replace with your input file name
output_file = 'output6_file.txt'  # Replace with the desired output file name

try:
    with open(input_file, 'r', encoding='utf-8') as file:
        text_content = file.read()

        # Replacing '\n' characters with actual line breaks
        cleaned_content = text_content.replace('\n', '\n')

    # Writing cleaned content with line breaks to a new file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(cleaned_content)
        print(f"Cleaned data saved to '{output_file}'")
        
except FileNotFoundError:
    print(f"File '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")