"""
This script contains my knowledge on Conditions and different datatypes
"""

print("This firm has multiple roles ")
print("Want find out the Role you're Interested in ? ")

print("Type Your Desired Role in "
      "Capitalized Value {eg;Devops} no space Below.")

Roles = ['Devops', 'Software Engineer', 'Network Engineer', 'Data Analysis',
         'Accountant', 'Marketing Admin', 'Solution Architect', ]
Requirements = ('python', '.net', 'matlab', 'java', 'c++', 'mysql')
Recruiter = {'name': 'dave', 'department': 'marketing', 'contact info': 74612324}
Recruiter2 = {'name': 'tom', 'department': 'tech', 'contact info': 55461232344}

usr_role = input("Enter your desired Role :")

# Check in database do we have this job role
if usr_role in Roles :
    print(f'We have {usr_role} opening in our firm.')
elif (usr_role in Requirements):
    print(f"We are in need for {usr_role} skill.")
elif (usr_role in Recruiter.values() or usr_role in Recruiter2.values()):
    print(f"Your Recruiter ")
else:
    print("no roles available")
    print("check the spilling you have entered or is it in capitalize with no spaces")
