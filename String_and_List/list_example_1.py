# -*- coding: utf-8 -*-


# len()
# list.append()
# list.extend()

# list.pop()
# list.insert(i)

list_1 = ["a","b","c"]
list_2 = [3,2,1]
list_1.append(list_2)

print("append result:")
print(list_1)
print("length:" + str(len(list_1)) + "\n")
# -----------------------------------------

list_1 = ["a","b","c"]
list_2 = [3,2,1]
list_1.extend(list_2)
print("extend result:")
print(list_1)
print("length:" + str(len(list_1)) + "\n")
# -----------------------------------------

print("Pop:")
list_1 = ["a","b","c"]
print(list_1.pop())
print(list_1)
# -----------------------------------------

print("\nRemove:")
list_1 = ["a","b","c"]
list_1.remove("b")
print(list_1)
# -----------------------------------------

list_1 = [1,"b",3,"d"]
list_1.insert(2,100)    # 
print("\ninsert result:")
print(list_1)

