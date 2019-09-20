'''
Dictionary:
           1.class of dictionary : dict
           2.a={key:value,key:value}
             eg. student={"Name":"Shrikant","Roll":10}
             We also use key value pair in MongoDB,JSON.
           3.Indexing is not supported in Dictionary but it is mutable.
           4.We can add,delete,modify in dictionary using key.

set is mutable as by a.add() fuction we can add any value
'''

a={"Name":"Saurabh","Roll":20}
print(type(a))
print(a)
print(a["Name"])
a["Name"]="name"   #to change any value
a["Age"]=20   #to add any value
a.update({"city":"talegoan"})  #we can also add by update fuction
print(a.keys())
print(a.values())
print(a.items())

