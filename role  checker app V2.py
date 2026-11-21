import random
print ("Welcome to the Random Role Selector!")
roles = ('ai machine learning engineer','devops engineer','site reliability engineer','system administrator','help desk')
chosen_role = random.choice(roles)
print (f'Your randomly selected role is: {chosen_role}')
if chosen_role == 'ai machine learning engineer':
    print ("welcome to your new role!")
    print ("You will be working on cutting-edge AI technologies and developing machine learning models.")
elif chosen_role == 'devops engineer':
    print ("welcome to your new role!")
    print ("You will be responsible for automating and streamlining the software development and deployment process.")
elif chosen_role == 'site reliability engineer':
    print ("welcome to your new role!")
    print ("You will be ensuring the reliability and performance of our systems and services.")
elif chosen_role == 'system administrator':
    print ("welcome to your new role!")
    print ("You will be responsible for managing and maintaining our IT infrastructure.")
elif chosen_role == 'help desk':
    print ("welcome to your new role!")
    print ("You will be providing technical support and assistance to our users.")