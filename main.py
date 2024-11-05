import sys
import os

def sort_and_deduplicate(file_path):
    # Create the output file path by appending '_output' before the file extension
    base, ext = os.path.splitext(file_path)
    output_path = f"{base}_output{ext}"
    
    # Open the file and read all lines while handling different newline types.
    with open(file_path, 'r', newline=None) as file:
        lines = file.readlines()
    
    # Strip whitespace from each line and filter out empty lines
    lines = [line.strip() for line in lines if line.strip()]
    
    # Remove duplicates by converting to a set, then sort the set
    unique_sorted_lines = sorted(set(lines))
    
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
        sort_and_deduplicate
