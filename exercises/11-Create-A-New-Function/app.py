import random

# ✅↓ Write your code here ↓✅
def generate_random():
    min_num = 0
    max_num = 9
    random_number = random.randint(min_num, max_num)
    return random_number 

print(generate_random)