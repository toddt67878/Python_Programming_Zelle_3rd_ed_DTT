def recFib(n):
    # returns nth Fibonacci number
    # Note: this algorithm is exceedingly inefficient!
    print("Computing fib(", n, ")")
    if n < 3:
        return 1
    else:
        print("Leaving fib(", n, ") returning(", n-1, ")")  # is this right?
        return recFib(n-1) + recFib(n-2)
