# salam man rasa ansari hastam va in proje tabedil vahed ast
# ke ba def va if va elif va return neveshte shode ast 
def vahed(tool , arz, dastoor , metr1 = 100 , metr2 = 1000):
    masahat  = tool * arz
    if dastoor == 'cm':
        cm = masahat / metr1
        return cm
    elif dastoor == 'mm':
        mm = masahat / metr2
        return mm
r = vahed(2,3,'cm')
print("masahat be metr:{}".format(r))
