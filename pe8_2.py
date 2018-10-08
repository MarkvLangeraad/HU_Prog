List = eval(input("Give a list with 10 strings:"))
new_list = []

def count(List):
    for file in List:
        if len(file) == 4:
            new_list.append(file)
    return file
count(List)

print('De nieuw list met alle 4-letter woorden bestaat uit:',new_list)

# copy and paste this: ["nice", "hello", "work", "done", "apple", "tree", "wood", "house", "doo", "plate", "lane", "down"]
