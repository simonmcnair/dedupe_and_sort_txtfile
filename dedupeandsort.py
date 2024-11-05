import sys
import os

def sort_and_deduplicate(file_path):
    # Create the output file path by appending '_output' before the file extension
    base, ext = os.path.splitext(file_path)
    output_path = f"{base}_output{ext}"
    
    # Open the file and read all lines while handling different newline types.
    with open(file_path, 'r', newline=None) as file:
        lines = file.readlines()
    
    # Strip whitespace, remove empty lines, and perform case-insensitive deduplication
    deduped_lines = {}
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:  # Ignore empty lines
            deduped_lines[stripped_line.lower()] = stripped_line  # Key by lowercase, store original
    
    # Sort the deduplicated lines (by the original case)
    unique_sorted_lines = sorted(deduped_lines.values(), key=lambda x: x.lower())
    
    # Write the sorted unique lines back to a new file
    with open(output_path, 'w', newline='\n') as output_file:
        for line in unique_sorted_lines:
            output_file.write(f"{line}\n")
    
    print(f"Sorted and deduplicated file created at: {output_path}")

# Check if the script is being run with an input file argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <input_file>")
    else:
        input_file = sys.argv[1]
        sort_and_deduplicate(input_file)
