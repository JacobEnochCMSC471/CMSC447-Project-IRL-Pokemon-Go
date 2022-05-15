from django.shortcuts import render, redirect
from PGIRL.Map.models import Challenge

chall_list = None #drastic measures
pet_health =None
pet_strength = None

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
    Challenge.objects.all().delete()
    return redirect('challenges')

#Pick a pet, open the challenge page, delete the other challenges from db and reset list
def chall(request):
    # check if they have a pet.. if not then kick them out!
    items = list(Photo_Data.objects.filter(verified_status=True))

    # only pick a random pet IF there's an image hehe
    if len(items) == 0:
        print("No pets to complete challenges.. returning to map.")
        return render(request, 'Map/map.html')

    global chall_list
    global pet_health
    global  pet_strength


    #If we haven't already...
    if len(chall_list) != 1:
        pet_health = items[0].stat_hp
        pet_strength = items[0].stat_attack
        #identify which challenge..
        if request.POST.get("ch1"):
            chall_list = [chall_list[0]]
        elif request.POST.get("ch2"):
            chall_list = [chall_list[2]]
        else:
            chall_list = [chall_list[3]]


    #make sure to pass the contect (update the image 'img1': "../../../media/enemies/" + str(),)
    cont = {
        'image': "../../../media/" + str(items[0].image),
        'enemy_img': "../../../media/" + str(chall_list[0].image_),
        'pet_hp': pet_health,
        'en_hp': chall_list[0].enemy_hp
    }

    return render(request, 'Map/battle.html', context=cont)

#move for attack or quit, also deal with battle end (delete chall when done). clear chall list
def battle_action(request):
    global chall_list
    global pet_health
    global pet_strength

    #check for win/lose, clear DB
    if pet_health <0:
        print("Pet lost :(")
        Challenge.objects.all().delete()
        return render(request, 'Map/lose_screen.html')

    if chall_list[0].enemy_hp <0:
        print("pet win!!")
        Challenge.objects.all().delete()
        return render(request, 'Map/win_screen.html')

    #decrement healths
    pet_health -=chall_list[0].enemy_att
    chall_list[0].enemy_hp -= pet_strength

    return redirect('chall')

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