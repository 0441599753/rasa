# salam rasa ansari hasta va in proje joste jo ketab ast
# ke ba while va if va else va int input va input va list neveshte shode ast
listbook = list()
tedad = int(input("tedad:"))
while len(listbook) < tedad:
    book = input("ketab:")
    listbook.append(book)
search = input("search book:")
if search in listbook:
    print("mojod ast")
else:
    print("iaft nashos!")
