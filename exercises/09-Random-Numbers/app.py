import random

def get_randomInt():
  	# ✅ ↓ CHANGE ONLY THIS ONE LINE BELOW ↓ ✅
	min_num = 1
	max_num = 10
	random_number = random.randint(min_num, max_num)
	return random_number

print(get_randomInt())