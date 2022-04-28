
file_path = "resources/input.csv"
f = open(file_path, mode="r", encoding="utf-8")

# line = f.read()
# print(line)

# lines = f.readlines()
# print(lines)

while (line := f.readline()):
  print(line.rstrip("\n"))

f.close()

with open(file_path, mode="r", encoding="utf-8") as f:
  lines = f.readlines()
  print(lines)
