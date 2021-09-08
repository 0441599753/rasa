list = list()
tedad = int(input("tedad:"))
zarib = int(input("zarib:"))
while len(list) < tedad:
    text = int(input("adad:"))
    list.append(text)
for number in list:
    print(number * zarib)
