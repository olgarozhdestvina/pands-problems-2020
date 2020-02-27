# Olga Rozhdestvina

with open('myfile.txt', 'w') as f:
    print(f.tell())
    f.write("\n Hello from the first line!")
    print(f.tell())