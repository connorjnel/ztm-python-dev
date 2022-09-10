while True:
    try:
        age = int(input("What is your age\n"))
        10/age
        raise ValueError("Hey cut it out")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
        break
    else:
        print("thank you")
    finally:
        print("okay, im finally done")
    print("can you hear me?")
