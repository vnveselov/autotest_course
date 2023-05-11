first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'
id_1 = second_string.find(first_string[0])
id_2 = second_string.find(first_string[1])
id_3 = second_string.find(first_string[2])
min_id = min (id_1, id_2, id_3)
max_id = max (id_1, id_2, id_3)
print (second_string[min_id : max_id + 1])