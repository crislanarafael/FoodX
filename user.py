# def do_nothing():
# 	pass
# comment taken from account.html
# status is FoodXRole, so either Provider or Seeker
# we need to collect this information from the database of users

def food_choice_provider():
	food_options = []
	food_options.append(comment)
	return food_options

def food_choice_seeker():
	food_options = []
	food_options.append(comment)
	return food_options

def filter_food():
	# take list of food_options selected by user and parse through to determine what food items are being searched for
	for food in food_choice_seeker:
		if food in food_choice_provider:
			return True # or list of matches
		else:
			return "No match found."