def check_if_valid(num):
    try:
        float(num)
        print("it is a number")
        return True
    except ValueError:
        print("not a number")
        return False

check_if_valid("5")
check_if_valid("5.5")
check_if_valid("five")
check_if_valid("5five")
check_if_valid("five5")
check_if_valid("5,000")