list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = [x + y for x in list1 for y in list2] # x берется от первого списка Y от второго и в начале добавляется по очереди в новый список
print(list3)