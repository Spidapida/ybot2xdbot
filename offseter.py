# !!! FOR YBOT MACROS ONLY !!! 

import sys

def offsetter(input_file, celery, output_file):

  with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
      data = line.strip().split()
      if len(data) >= 2:
        try:
          number = int(data[0])
          kekoy = int(celery)
          outfile.write(f"{number + kekoy} {' '.join(data[1:])}\n")
        except ValueError:
          print(f"Error: Invalid data format in line: {line}")

# Example usage is python offseter.py <inputfile> <offsetframes> <outputfile>
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Not enough args")
    if len(sys.argv) < 3:
        print("Error: Not enough args")
    if len(sys.argv) < 4:
        print("Error: Not enough args")
    else:
        input_file = sys.argv[1]
        celery = sys.argv[2]
        output_file = sys.argv[3]
        offsetter(input_file, celery, output_file)
        print(f"Saved to: {output_file}")

# !!! I REPEAT, THIS IS ONLY FOR YBOT MACROS ONLY !!!
