# salam man rasa ansari hastam va in proje dictionary ast
# ke ba def va dictionary neveshte shode ast
esm = input("esm khod ra vared konid:")
famili = input("famili khod ra vared konid:")
sen  = int(input("sen khod ra vared konid:"))
vaziat = input("vaziat tahol khod ra vared konid:")
def e():
    text = {'esm': esm , 'famili' : famili  , 'sen' : sen , 'vaziat tahol' : vaziat}
    print(text.get('esm' , 'balad nistam'))
e()    
