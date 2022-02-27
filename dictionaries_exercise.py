text = open('book_of_John.txt','r')
read_text = text.read()

words_dict = dict()

words = ['Father','God','Christ','Spirit','life','man']

for i in words:
    count = read_text.count(i)
    words_dict[i] = count



text.close()


for key,value in words_dict.items():
    print(key,':',value)