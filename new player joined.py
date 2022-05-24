file = open("transcript1.txt","r")
transcript1 = []

for line in file:
    transcript1.append(line.strip())
    
file.close()

file = open("transcript2.txt","r")
transcript2 = []

for line in file:
    transcript2.append(line.strip())
    
file.close()

print()
print(transcript1[0])
print(transcript1[1])
print()
print(transcript2[0])
print()
print(transcript2[1])