def fib(n):
  def fib_help(a, b, n):
    return fib_help(b, a+b, n-1) if n > 0 else a
  return fib_help(0, 1, n)
# Driver Code

n = int(input())
print(fib(n))