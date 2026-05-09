import csv

with open('miniproject3.csv','r') as file:
    Sort_Record=sorted(file)
    print(Sort_Record)
    reader=csv.reader(file)
    
Choose=str(input("1.ID\n2.Name\n3.Department\nEnter the searching: ").upper())
while Choose not in ("1","2","3","ID","NAME","DEPARTMENT") :
    Choose=str(input("Enter the searching again: ").upper())

Search=str(input("Enter what you want to search: "))
Found=True
with open('miniproject3.csv','r') as csv_file:
    reader=csv.reader(csv_file)
    for i in reader:
        if str(i[0])==Search:
            print("\nFound in ","\nEmployee Number:",i[0],"\nName: ",i[1],"\nDepartment:",i[2],"\n")
            Found=False
        if i[1]==Search:
            print("Found in ","\nEmployee Number:",i[0],"\nName: ",i[1],"\nDepartment:",i[2],"\n")
            Found=False
        if i[2]==Search:
            print("Found in ","\nEmployee Number:",i[0],"\nName: ",i[1],"\nDepartment:",i[2],"\n")
            Found=False
if Found==True:
    print("Your searching is not found in the list.")