def fibonacci(n):
    # Cek jika n adalah 0 atau 1, karena fibonacci(0) = 0 dan fibonacci(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Rekursi untuk menghitung fibonacci(n-1) + fibonacci(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Masukkan nilai n:"))
print(f"Fibonacci ke-{n} adalah {fibonacci(n)}")