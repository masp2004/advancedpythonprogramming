import concurrent.futures
import random
import time

def count_a():
    for i in range(1, 101):
        print(f"CountA: {i}")
        # Verzoegerung: sinnlose Zufallszahlen erzeugen
        for _ in range(100000):
            random.randint(1, 100)
        

def count_b():
    for i in range(100, 0, -1):
        print(f"CountB: {i}")
        # Verzoegerung: sinnlose Zufallszahlen erzeugen
        for _ in range(100000):
            random.randint(1, 100)
        

def main():
    print("Starte das Zählen")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(count_a), executor.submit(count_b)]
        concurrent.futures.wait(futures)

    print("Zählen beendet.")

if __name__ == "__main__":
    main()
