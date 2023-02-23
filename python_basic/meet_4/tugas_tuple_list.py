print("======= Modifikasi Pyton List dan Tuple ========")

tuple1 = ('Python', 'Golang', 'Javascript', 'PHP')
tuple2 = ("FastAPI","Gin", "Express JS", "Laravel")
tuple3 = ("MySQL", "PostSQL", "MongoDB", "Oracle")
print(tuple1)
print(tuple2)
print(tuple3)

# print(tuple1, tuple2)
# update nilai tuple
tuplegab = tuple1 + tuple2 + tuple3
# print(tuplegab)

# #mengurutkan tuple
sorted_tupl3 = tuple(sorted(tuplegab))
# print(sorted_tupl3)

# del sorted_tupl3

sorted_tupl3 = (tuple1[0], tuple2[0], tuple3[1])
print(f"Ternyata kita mau pakai teknologi : {sorted_tupl3[0]}, {sorted_tupl3[1]}, {sorted_tupl3[2]} saja ")

data = []
# print(f'list kosong : {data}')

programming_language_unused = []
framework_unused= []
database_unused= []


programming_language_unused = [tuple1[1],tuple1[2],tuple1[3]]
framework_unused= [tuple2[1],tuple2[2],tuple2[3]]
database_unused= [tuple3[1],tuple3[2],tuple3[3]]

# print(f"programming_language_unused : {programming_language_unused}")
# print(f"framework_unused : {framework_unused}")
# print(f"database_unused : {database_unused}")


# list_data = {
#     "tech_stack_used":{
#         "programming_language": "",
#         "framework" : "",
#         "database" : "" 
#     },
#     "tech_stack_unused": {
#         "programming_language": "",
#         "framework": "",
#         "database" : ""
#     }
# }
# print(list_data)

list_data = {
    "tech_stack_used":{
        "programming_language": tuple1[0],
        "framework" : tuple2[0],
        "database" : tuple3[1] 
    },
    "tech_stack_unused": {
        "programming_language": programming_language_unused,
        "framework": framework_unused,
        "database" : database_unused
    }
    
}
data.append(list_data)
print('hasil list terupdate: ', data)

response = {"status": "", "message":"", "data":""}

response.update(
    {
        "status": "00",
        "message" : "Sukses",
        "data": data
    }
)
print(f'balikan response : {response}')

