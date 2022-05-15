from django.shortcuts import render
from PGIRL.Map.models import Challenge

chall_list = None #drastic measures

def map(request):
    return render(request, 'Map/map.html')

def shop(request):
    return render(request, 'Map/shop.html')

def training(request):
    return render(request, 'Map/training.html')

def challenges(request):
    global chall_list
    #create 3 challenges
    c1 =create_challenge()
    c2 =create_challenge()
    c3 =create_challenge()
    chall_list = [c1,c2,c3]

    cont = {
        'c1':c1,
        'c2':c2,
        'c3':c3
    }

    return render(request, 'Map/challenges.html', context = cont)

#Delete old challenges from db, refresh challenges view
def refresh(request):
    pass

#Pick a pet, open the challenge page, delete the other challenges from db and reset list
def chall(request):
    global chall_list

    #make sure to pass the contect (update the image 'img1': "../../../media/enemies/" + str(),)
    pass

#move for attack or quit, also deal with battle end (delete chall when done). clear chall list
def battle_action(request):
    global chall_list
    pass

def create_challenge():
    # Roll for requirement!
    x = random.randint(0, 1)
    level = 0
    ex = 0
    hp = 0
    if x:
        level = random.randint(1, 3)

    x = random.randint(0, 1)
    if x:
        ex = random.randint(0, 3)

    x = random.randint(0, 1)
    if x:
        hp = random.randint(5, 15)

    # randomize image
    x = random.randint(1, 3)
    img_name = "robot" + str(x) + ".png"

    e_hp = 15
    # change enemy health based on which enemy it is
    if x == 1:
        e_hp = random.randint(11, 18)
    elif x == 3:
        e_hp = random.randint(18, 24)

    c =Challenge.objects.create(required_level=level, required_experience=ex, required_health=hp, image_=img_name,
                             enemy_hp=e_hp)
    return c