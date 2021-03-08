while True:
    try:
        num = int(input("input num"))
        divisor = int(input("input divisor"))
        print(num/divisor)
    except Exception as e:
        print(f"{e} has occurred")
