import os
import platform

global list_of_students #Making list_of_students As Super Global Variable
list_of_students = ["Subhankar Das","Asish Das","Sagar Barman","Gourhari Bej"] #List Of Students already added

def manage_Student(): #Function For The Student Management System
	global bye #Making Bye As Super Global Variable
	bye ="THANK YOU FOR USING StUDENT MANAGEMENT" # Will Print GoodBye Message

	#Printing Welcome Message And options For This Program
	print(""" 
  ------------------------------------------------------
 |======================================================| 
 |======== WELCOME TO STUDENT MANAGEMENT SYSTEM	========|
 |======================================================|
  ------------------------------------------------------

 Enter 1 : To View Student's List 
 Enter 2 : To Add New Student 
 Enter 3 : To Search Student 
 Enter 4 : To Remove Student 
""")

	try: #Using Exceptions For Validation
		user_input = int(input("Please Select An Above Option: ")) #Will Take Input From User
	except ValueError:
		exit("\nHy! That's Not A Number") #Error Message
	else:
		print("\n") #Print New Line

	#Checking Using Option	
	if(user_input == 1): #This Option Will Print List Of Students
		print("LIST OF STUDENTS :")
		print("_________________\n") 
		for students in list_of_students:
			print("=> {}".format(students))

	elif(user_input == 2): #This Option Will Add New Student In The List
		new_student = input("Enter New Student :")
		if(new_student in list_of_students): #This Condition Checking The New Student Is Already In List Ur Not
			print("\nThis Student {} Already In The Database".format(new_student))  #Error Message
		else:	
			list_of_students.append(new_student)
			print("\n=> New Student {} Successfully Add \n".format(new_student))
			for students in list_of_students:
				print("=> {}".format(students))	

	elif(user_input == 3): #This Option Will Search Student From The List
		search_for_student = input("Enter Student Name To Search: ")
		if(search_for_student in list_of_students): #This Condition Searching The Student
			print("\n=> Record Found Of Student {}".format(search_for_student))
		else:
			print("\n=> No Record Found Of Student {}".format(search_for_student)) #Error Message

	elif(user_input == 4): #This Option Will Remove Student From The List
		remove_student = input("Enter Student Name To Remove: ")
		if(remove_student in list_of_students): #This Condition Removing The Student From The List 
			list_of_students.remove(remove_student)
			print("\n=> Student {} Successfully Deleted \n".format(remove_student))
			for students in list_of_students:
				print("=> {}".format(students))
		else:
			print("\n=> No Record Found of This Student {}".format(remove_student)) #Error Message
	 
	elif(user_input < 1 or user_input > 4): #Validating User Option
		print("Please Enter Valid Option")	#Error Message	
						
manage_Student()

def runAgain(): #Making Runable Problem1353
	run_again = input("\nWant To Run Again Y/N: ")
	if(run_again.lower() == 'y'):
		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		manage_Student()
		runAgain()
	else:
		quit(bye) #Print GoodBye Message And Exit The Program

runAgain()		
