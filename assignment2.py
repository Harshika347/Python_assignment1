# 1.) Create a file and write to it
with open('masna.txt', 'w') as f:
    f.write('Hello Dear! I am Harshika.\n')

# 2.) Append more content to the file
with open('masna.txt', 'a') as f:
    f.write('I am from Hyderabad.\n')


# output : 
# Hello Dear! I am Harshika.
# I am from Hyderabad.

import os
print(os.path.abspath('masna.txt'))

# output :
# C:\Users\masna\OneDrive\Desktop\Fed\masna.txt

 # Read and print all lines from the file
with open('masna.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)

# output :
# ['Hello Dear! I am Harshika.\n', 'I am from Hyderabad.\n']


# Read and print just the first line
with open('masna.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line)

# output :
# Hello Dear! I am Harshika.