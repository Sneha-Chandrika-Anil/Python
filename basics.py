first_name = "Sneha"
middle_name = "Chandrika"
last_name = "Anil"
print(first_name+" "+middle_name+" "+last_name)
list,tuples,dictionaries
cricketers = ["Virat","Dhoni","Sachin","Bumrah"]
print(type(cricketers))
runs = [100,35,84,6,[1,4,6]]
print(type(runs))
performance = list(("Excellent","Average","Good"))
print(type(performance))
print(cricketers)
print(runs)
cricketers[-2]="Shami"#change list items
cricketers.pop()#delete list item
print(len(cricketers))
cricketers.append("Sachin")
tuple1 = (1,"anu",3)
print(type(tuple1))
print(tuple1)

list4 = ["Abd","Gayle","Zaheer","Rashid"]
list3 = list(cricketers)
# copy lists
cricketers[-1]="Rohit"
print(list4)
print(cricketers)
print(list3)

d = {"student1":{
    "name": "Sneha",
    "age": 22,
    "marks":{
        "math": 90,
        "science": 85
        }},
    "student2":{
    "name": "Urmila",
    "age": 23,
    "marks":{
        "math": 98,
        "science": 88
        }}
    }
d["student1"]["marks"]["math"]=75 #update values in dictionaries
d["student2"]["place"]="rajastan"
print(d.get("student1").get("marks")) #add keys in dictionary
print(d["student2"])
d.get("student2").pop("age") #to delete a particular inner dictionary key
print(d["student2"])
del d["student1"] #delete keyword
print(d)
d.clear() #clearing dictionaring
print(d)


set1 = {1,5}
set2 = {'a','b','c','d',22,23,24}
print(set1)
print(set2)

