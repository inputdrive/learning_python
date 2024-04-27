def username_generator(first_name, last_name):
    user_name = first_name[:3] + last_name[:4]
    return user_name
   
def password_generator(user_name):
    password = ""
    for i in range(len(user_name)):
        password += user_name[i-1]
    return password
#end of review_i.py