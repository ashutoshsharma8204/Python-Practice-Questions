# You have given A string a you have to find a all amazing substring of S and amazing substring is first that start with a vowel.
S = input()
N = len(S)
C = 0
for i in range(0,N):
     if (S[i] in 'aeiouAEIOU'):
         C = C + (N-i)
         
print(C)


# Find the number of occurence of 'bob' in string A. Consisting of lowercase letters.
A = 'abobc'
C = 0
for i in range(len(A)-2):
  if(A[i]=='b' and A[i+1]=='o' and A[i+2]=='b'):
    C = C+1
print(C)


