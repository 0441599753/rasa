import robot_help_python as r
k = []
r.make_random_number_for_list(k,10,1,20)
print(k)
for i in k:
    print(i*2)
    r.wait(1)
