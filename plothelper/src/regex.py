import re
s = "#3 @ 5,5: 2x2"
a,b,c,d = re.search(r"#\d+ @ (\d+),(\d+): (\d+)x(\d+)", s).groups()
print(a,b,c,d)