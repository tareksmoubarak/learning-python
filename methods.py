def getUserAge():
	return int(input("Enter your age: "))

def calculateAgeInSecond(ageYears):
	return ageYears*365*24*60*60

def run():
	print("Your age in seconds is {}.".format(calculateAgeInSecond(getUserAge())))

run();