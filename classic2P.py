import sys

def classic2P(input_file, output_file):
  lines_to_skip = ["0 1 0 R", "0 1 1 R"]

  try:
    with open(input_file, "r") as in_file, open(output_file, "w") as out_file:
      first_line = in_file.readline().strip()
      out_file.write(first_line + "\n")

      for line in in_file:
        if line.strip() not in lines_to_skip:
          values = line.strip().split()
          out_file.write(f"{values[0]}|")
          out_file.write(f"{values[1]}|1|")

          for value in values[2:]:
            if value == "0":
              out_file.write("1|")
            else:
              out_file.write("0|")

          out_file.write("0|0|0|0|-80085|-80085|-80085|0|0|0|-80085|-80085|-80085\n")
  except FileNotFoundError:
      print(f"Error: Input file '{input_file}' not found.")

if len(sys.argv) < 3:
  print("Usage: python script.py <input_file> <output_file>")
  sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

classic2P(input_file, output_file)
