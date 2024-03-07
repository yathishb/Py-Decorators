from main import div

def decorator(func):
    def div_abs(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return div_abs

@decorator
def add(a,b):
    return(a+b)

d = decorator(div)
print(d(a=1,b=6))

print(add(a=1,b=6))