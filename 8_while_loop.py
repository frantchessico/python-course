def user_details(fullname):
    if not fullname: print('These fields is required')
    else: print(f"Your fullname is: {fullname}")




fullname = ""

while fullname !="Francisco Inoque":
    fullname = input("Please enter your fullname: \n")

def show_user_details():
    try:
        user_details(fullname)
    except ValueError : print("Please enter the values")

show_user_details()