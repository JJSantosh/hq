def age(a):
    try:
        a=int(a)
        if a < 0:
            raise ValueError("negative number us not allowed")
        if a % 2==0:
            print("Age is even")
        else:
            print("Age is odd")

    except ValueError as e:
        print("Invalid age")

i=input("Enter age:")
age(i)    