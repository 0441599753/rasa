# salam man rasa ansari hastam va in proje BMI ast
# ke ba def va if va elif va return neveshte shode ast
ghad = int(input("ghad khod ra konid:"))
vazn = int(input("vazn khod ra konid:"))
def BMI():
    b =  vazn / (ghad * ghad) * 10000
    return b
c = BMI()
r = round(c,2)
print('''vazne shoma hast: {} vagahad shoma hast :{} va BMI shoma hast :{}'''.format(vazn , ghad ,r))
if r < 16:
    print("dochar kambod vazne shoded")
elif (r >= 16) and  (r <= 18):
    print("kambod vazne")

elif (r >= 18) and (r <= 25):
    print("adi")

elif (r >= 25) and (r <= 30):
    print("ezafe vazn")

elif (r >= 30) and (r <= 35):
    print("ezafe vazne 1")

elif (r >= 35) and (r <= 40):
    print("ezafe vazne 2")

elif (r > 40):
    print("ezafe vazne 3")
