def userId():
	return int(input("Enter id: "))

def userGrade():
	return int(input("Enter your grade: "))

def userResult(userGrade):
	if userGrade<60 :
		result="D"
	elif userGrade>=60 and userGrade<=70:
		result="C"
	elif userGrade>70 and userGrade<=80:
		result="B"
	elif userGrade>80 and userGrade<=90:
		result="A"
	elif userGrade>90 and userGrade<=100:
		result="A+"
	else:
		result="D"

	return result

def run():
	print("Student with id = {} has a {} grade.".format(userId(),userResult(userGrade())))

run()