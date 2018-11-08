""" Perfectionist """
def main():
    """" input """
    num = int(input())
    if 0 < num <= 100:
        if num % 5 == 0:
            print("Perfect")
        else:
            print("Not Perfect")
    elif num > 100:
        if num % 10 == 0:
            if num % 25 == 0:
                print("Perfect")
            else:
                print("Not Perfect")
        else:
            print("Not Perfect")
    else:
        print("Not Perfect")

main()
