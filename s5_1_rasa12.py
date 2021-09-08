list = dict()
text = int(input("tedad :"))
tartib = 1
while len(list) < text:
    nam = input("nam ra vared konid:")
    shomre = int(input("shomare ra vared konid:"))
    list[tartib] = dict()
    list[tartib]['nam'] = nam
    list[tartib]['shomare telephone'] = shomre
    tartib += 1
text = int(input("shomare tartib :"))
print(list[text])
