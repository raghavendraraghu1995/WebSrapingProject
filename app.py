text_variable='i learn everything with my own interest'
count=0
word_list=text_variable.split(" ")
for every_word in word_list:
    if("learn"==every_word):
        count=count+1


print(count)