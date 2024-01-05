import re

my_search = re.search(r"[A-z]", "hassnaelwhdi")
print(my_search)

my_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|ent)", "hassna234@gmail.com")
print(my_email.group())