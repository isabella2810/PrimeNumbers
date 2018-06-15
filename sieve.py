# return a list ret that contains all prime numbers <= N
def sieve_algorithm(N):
  myList = [True] * (N+1);

  for i in range(2,N+1):
    if myList[i]==True:
      j=2;
      while j*i<=N:
        myList[j*i] = False
        j+=1

  ret = []
  for i in range(2,N+1):
    if(myList[i]):
      ret.append(i)

  return ret

print(sieve_algorithm(11))
