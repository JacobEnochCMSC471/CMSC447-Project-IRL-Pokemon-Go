from django.db import models
import random
from Inventory.models import Item

from Photo_Uploader.models import Photo_Data

class Challenge(models.Model):
    #should have level req, ex req, minimum pet health, type of challenge, png, if its done
    required_level=models.IntegerField(default=1)
    required_experience=models.IntegerField(default=0)
    required_health = models.IntegerField(default=0)
    challenge_type = models.CharField(max_length=10, default="Battle")
    image = models.CharField(max_length=20, default="")
    completed = models.BooleanField(default=False)
    enemy_hp=models.IntegerField(default=15)
    enemy_att = models.IntegerField(default=2)

    def reward_player(pet: Photo_Data):
        reward_stats = random.randint(0, 1)
        reward_item = random.randint(0, 1)

        if reward_stats:
            num_increases = 1
            # Rare chance to get an extra stat increase
            if random.randint(0, 100) == 100:
                num_increases = 2
            
            while num_increases > 0:
                stat_choice = random.randint(1, 4)
                if stat_choice == 1:
                    pet.stat_hp += 1
                elif stat_choice == 2:
                    pet.stat_attack += 1
                elif stat_choice == 3:
                    pet.stat_defense += 1
                else:
                    pet.stat_speed += 1
                
                num_increases -= 1
        
        if reward_item:
            items = {
                "Stick": ["A basic stick", 1, 'media/items/branch.png'],
                "Rock": ["It's a rock", 1, 'media/items/rock.png'],
                "Gubgub Berry": ["Don't eat it", 1, 'media/items/gubgub.png'],
                "Bokki Berry": ["Eat it", 1, 'media/items/bokki.png']
            }

            item_name = random.choice(items)
            item_info = items[item_name]
            Item.objects.create(user_id=pet.user_id, name=item_name, description=item_info[0], quantity=item_info[1], image=item_info[2])
