def primes():
  i = 2
  yield i
  i +=1
  while True:
     x = True
     for j in range(2, int(i**0.5)+1):
         if i % j == 0:
             x = False
             break
     if(x):
        yield i
     i += 1