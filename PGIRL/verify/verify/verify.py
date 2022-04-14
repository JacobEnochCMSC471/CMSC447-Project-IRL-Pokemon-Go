#Assume photos are passed in as a dictionary
#from multiprocessing import Queue
#from __ import __ //whatever i might need from the other person's

"""
This is where I'd get the dictionary/queue passed in (i believe it might be a queue, but for quick testing 
purposes I'm using a dictionary)
"""
verified = [] #completed pets, verified
delete = [] #completed pets, need removal


#For now, placing the testing stuffs in here
pet_test = {"Pet1": {"get_user_id": "1", "yes":2,"no":1,"total":3},
            "Pet2": {"get_user_id": "2", "yes":3,"no":1,"total":4},
            "Pet3": {"get_user_id": "52", "yes":1,"no":5,"total":6},
            "Pet4": {"get_user_id": "5", "yes":1,"no":1,"total":2}}
repeat_list = dict(pet_test) #ill probably change this later, given the queue could get very big

#Go through each pet, determine if it has been appropriately verified.
for i in range(len(pet_test)):
    pet = pet_test[i]
    if pet["total"] < 3: #idk y this is saying error lol silly
        print(pet, "still needs PGIRL")
    else:
        if pet["yes"] - pet["no"] < 0:
            verified.append(pet)
            repeat_list.pop(pet)
        else:
            delete.append(pet)
            repeat_list.pop(pet)


#Test: print out what's in each
print("Here's each pet that passed PGIRL")
for pet1 in verified:
    print(pet1)

print("Here's each pet that failled PGIRL")
for pet1 in delete:
    print(pet1)

print("Here are the pets that still need to be verified")
for pet1 in repeat_list:
    print(pet1)

    # >:(