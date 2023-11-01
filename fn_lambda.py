q = lambda a:a+10
print(q(5))

w = lambda x,y,z,r:x+y*z+r
print(w(1,10,10,1))

def sample(a):
    return lambda x:x+a
q = sample(2)
print(q(3))