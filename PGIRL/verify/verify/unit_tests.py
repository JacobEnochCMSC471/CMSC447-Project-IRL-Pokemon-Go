"""
We had to change our method of implementation towards the end of the iteration. The belief is that our
photos will be held in a queue system, and once they have recieve 3 verifications it will exit the queue.
It is then determined if that photo passes or not.

Owen has models of pets, photos, and items on his branch. I mimic these tests based of that.
"""

#Each pet will be treated as a dictionary for now. "get_user_id" will be a number (to be replaced with the function)
#and there will be a slot for how many yes/no's a picture got.

#In the end, the values of the dictionary will be variables in the pet module. The queue of modules would be passed to
#this step when a user uploads their pet.

pet_test = {"Pet1": {"get_user_id": "1", "yes":2,"no":1,"total":3},
            "Pet2": {"get_user_id": "2", "yes":3,"no":1,"total":4},
            "Pet3": {"get_user_id": "52", "yes":1,"no":5,"total":6},
            "Pet4": {"get_user_id": "5", "yes":1,"no":1,"total":2}}

#Send values to the PGIRL system.
#Output should read : yes yes no unfinished

#To-do: Learn how to do multiprocessing and connect data from one to the other