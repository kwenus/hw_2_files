
info_dict = {}
texts = ['1.txt', '2.txt', '3.txt']
for text in texts:
    with open(text) as file:
        info_dict[len(file.readlines())] = text

sorted_keys = sorted(info_dict.keys())

with open('merged_file', 'a') as merged:
    for key in sorted_keys:
        with open(info_dict[key]) as file:
            merged.write(info_dict[key])
            merged.write('\n')
            merged.write(str(key))
            merged.write('\n')
            merged.write(file.read())
            merged.write('\n')





