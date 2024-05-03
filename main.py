import dis

print("Hello world")


def f(x):
    return 1 < x ** 2 < 100

dis.dis(f)