def pi(eps=1.0e-5):
    s=0
    d=1
    sgn=1
    while True:
        a=4/d
        s=s+sgn*a
        if a<eps:
            return s
        sgn=-sgn
        d=d+2
print(f"Классическое число π: {pi()}")