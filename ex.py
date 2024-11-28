import re
txt = "rain is beautiful"
#Check if the string ends with "ful":
x = re.findall("ful\Z", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
