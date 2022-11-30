def foo(h):
    if h==0:
        return 1
    elif h == 1:
        return 2
    return foo(h-1) + foo(h-2)

print(foo(5))
print(foo(7))