import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]



def main():
    num = random_numbers(10)
    print(f"Náhodná čísla: {num}")


if __name__ == "__main__":
    main()
