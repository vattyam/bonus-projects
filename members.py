new_member = input("Add a new member: ")
file = open(r'C:\Users\vatty\Downloads\members.txt', 'r')
members = file.readlines()
file.close()
members.append(new_member + "\n")
file = open(r'C:\Users\vatty\Downloads\members.txt', 'w')
file.writelines(members)
file.close()