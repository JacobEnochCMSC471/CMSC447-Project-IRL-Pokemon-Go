from django.db import models
import random
from PGIRL.Inventory.models import Item

from PGIRL.Photo_Uploader.models import Photo_Data

class Challenge(models.Model):
    required_level=models.IntegerField()
    required_experience=models.IntegerField()

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
                "Stick": ["A basic stick", 1, 'media/test_uploads/big_oof.PNG'],
                "Rock": ["It's a rock", 1, 'media/test_uploads/big_oof.PNG'],
                "Berry1": ["Don't eat it", 1, 'media/test_uploads/big_oof.PNG'],
                "Berry2": ["Eat it", 1, 'media/test_uploads/big_oof.PNG']
            }

            item_name = random.choice(items)
            item_info = items[item_name]
            Item.objects.create(user_id=pet.user_id, name=item_name, description=item_info[0], quantity=item_info[1], image=item_info[2])
