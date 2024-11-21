def read_and_modify_file(input_filename, output_filename):
    """Reads a file, modifies its content, and writes it to a new file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.
    """

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        # Modify the content (example: add a prefix to each line)
        modified_content = "\n".join(f"Modified: {line}" for line in content.splitlines())

        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"File '{output_filename}' created successfully.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except IOError:
        print(f"Error: Could not read or write file '{input_filename}'.")

# Get the input filename from the user
input_filename = input("Enter the input filename: ")

# Create the output filename (you can customize this)
output_filename = f"modified_{input_filename}"

# Call the function to read, modify, and write the file
read_and_modify_file(input_filename, output_filename)