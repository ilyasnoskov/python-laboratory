def func(text, input_type, valid_cond):
    input_type = input_type.__name__
    while True:
        try:
            if input_type == "int":
                user_input = int(input(text))
            elif input_type == "float":
                user_input = float(input(text))
            else:
                user_input = input(text)
        except:
            print("Введіть значення типу int або float")
            continue
        if valid_cond is not None and valid_cond(user_input) is not True:
            print("Введіть допустиме значення.")
        else:
            return user_input
    return
