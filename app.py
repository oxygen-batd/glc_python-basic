import sys

def add_numbers(a, b):
    return a + b

def main():
    if len(sys.argv) != 3:
        print("Usage: python app.py <num1> <num2>")
        sys.exit(1)
    
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("Vui lòng nhập hai số nguyên hợp lệ.")
        sys.exit(1)
    
    total = add_numbers(num1, num2)
    print(f"Tổng của {num1} và {num2} là: {total}")

if __name__ == "__main__":
    main()
