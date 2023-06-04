def user_details(fullname):
    if not fullname: print('These fields is required')
    else: print(f"Your fullname is: {fullname}")




fullname = input("Please enter your fullname: \n")
def show_user_details():
    try:
        user_details(fullname)
    except ValueError: print("Please enter the values: ")
    # except ValueError as error : print("Please enter the values: ", error)

show_user_details()
