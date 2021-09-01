# salam man rasa ansari hastam va in proje class man ast 
# ke ba set va len neveshte shode ast
list = ('rasa', 'reza', 'hasan', 'parsa', 'mohamad', 'sorosh', 'amirsam')
list2 = ('rasa', 'parsa','amirsam', 'hasan')
set1 = set(list)
set2 = set(list2)
kol = list + list2
b = set(kol)
a = set1 - set2
tedad1 = len(a)
tedad2 = len(b)
menha = b - a
print(f"class fizick1:{menha} tedad:{tedad2} nafar")
print(f"class riazi1:{a} tedad:{tedad1} nafar") 
