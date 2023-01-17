import json
"""personal_data=[
  {"name":"Anna", 
    "age":18, 
    "email":"anna99@gmail.com", 
    "school":"maltas vidusskola",
   "car":
   {
   "year":"2020",
   "color":"sarkans", 
   "marka":"audi",
   "dz_tilp":"2.0"
   }
          },
  {"name":"Oskars", 
    "age":19, 
    "email":"oskars88@gmail.com", 
    "school":"rezeknes vidusskola",
    "car":
   {
   "year":"2021",
   "color":"peleks", 
   "marka":"bmw",
   "dz_tilp":"1.9"
   }
  }
]


with open('readme.txt', 'a') as f:
  for i in range(1,101):
    f.write(f"name {i} surname {i}\n")



file=open("personggggggs.json", "w")
json.dump(personal_data, file, indent=4)



file=open('students.json', 'r')
data=json.load(file)

student=data['Students'][0]

for student in data['Students']:
    print(f"Vārds: {student['Name']} Krāsa:{student['Color']}")


file=open('students.json', 'r')
data=json.load(file)
total_punkti=0
count=0



for student in data['Students']:
    total_punkti+=float(student["Hairstyle"])
    count+=1
videjais=round((total_punkti/count),2)
print(f'videjais hairstyle:{videjais}')
"""



file=open('students.json', 'r')
data=json.load(file)




for student in data['Students']:
    student["email"]=f"{student['Name']}.{student['Surname']}@epasts.com"

file_write=open("studentsnew.json", "w")
json.dump(data, file_write, indent=4)