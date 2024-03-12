import sys
xd = 0

def twoplayer(filename):
    """Checks if macro is 2 player or not"""

    with open(filename, "r") as file:
        third_values = set()
        for line in file:
            values = line.split()
            if len(values) >= 3:
                third_values.add(values[2])

        if len(third_values) >= 2:
            xd = 0 # difference
        else:
            xd = 1 # all similar

def ybot2xdbot(filename, output_file):
  """main function"""

  try:
    with open(filename, "r") as in_file, open(output_file, "w") as out_file:
      first_line = in_file.readline().strip()
      out_file.write(first_line + "\n")

      for line in in_file:
        if line.strip():
          values = line.strip().split()
          out_file.write(f"{values[0]}|")
          out_file.write(f"{values[1]}|")
          
          platform = "1" if len(values) < 4 else ("2" if values[3] == "L" else "3")
          
          out_file.write(f"{platform}")
          
          if xd == 1:
            out_file.write("|1")
          else:
            if values[2] == "0":
              out_file.write("|1")
            else:
              out_file.write("|0")

          out_file.write("|0|0|0|0|-80085|-80085|-80085|0|0|0|-80085|-80085|-80085\n")
  except FileNotFoundError:
      print(f"Error: Input file '{filename}' not found.")

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Error: No input name, please specify one, along with an output filename.")
  elif len(sys.argv) < 3:
    print("Error: Please provide an output filename as an argument.")
  else:
    filename = sys.argv[1]
    output_file = sys.argv[2]
    twoplayer(filename)
    ybot2xdbot(filename, output_file)
    print(f"Saved macro to: {output_file}")
