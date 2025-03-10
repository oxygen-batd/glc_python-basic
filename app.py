def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print(greet(name))
