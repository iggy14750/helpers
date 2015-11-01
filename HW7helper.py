def P(A):
    return (A**3)-(13*A**2)+(50*A)-56

def Q(A, X):
    return (A**3)-(6*A**2)+(5*A)+X-3

def f(P, Q):
    return min(abs(P), abs(Q), 1)

mybin = {0:"000", 1:"001", 2:"010", 3:"011", 4:"100", 5:"101", 6:"110", 7:"111"}

print "A aaa X xxx | P   Q | f"
for A in range(8):
    for X in range(4):
        print A, mybin[A], X, mybin[X], "|", P(A), Q(A, X), "|", f(P(A), Q(A,X)) 
