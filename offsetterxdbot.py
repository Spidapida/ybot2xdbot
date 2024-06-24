import sys

def offsetter(input_file, celery, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if line.isdigit():
                outfile.write(f"{int(line)}\n")
            else:
                data = line.split('|')
                if len(data) >= 1:
                    try:
                        number = int(data[0])
                        offset = int(celery)
                        new_number = number + offset
                        outfile.write(f"{new_number}|" + '|'.join(data[1:]) + '\n')
                    except ValueError:
                        print(f"Error: Invalid data format in line: {line}")

# Usage is python offseter.py <inputfile> <offsetframes> <outputfile>
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error: Not enough args")
    else:
        input_file = sys.argv[1]
        celery = sys.argv[2]
        output_file = sys.argv[3]
        offsetter(input_file, celery, output_file)
        print(f"Saved to: {output_file}")
