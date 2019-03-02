from pip._vendor.distlib.compat import raw_input


def main():
    input_name = raw_input("Hi, friend! What's your name?\n")
    if input_name == "Alice" or input_name == "Bob":
        print("Hello there " + input_name)
    else:
        print("Sorry, this is only for Alice and Bob")


if __name__ == '__main__':
    main()
