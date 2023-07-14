def print_kwargs(*args, **kwargs):
    print(kwargs["a"])
    print(kwargs["c"])


def print_args(*args):
    for arg in args:
        print("hello ", arg)



if __name__ == "__main__":
    print_kwargs(a="b", c="d")
    print(1, 2, 3)
