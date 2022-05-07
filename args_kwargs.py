def fun(**kwargs):
    return kwargs.get("name")[::-1]


print(fun(name="Rezna"))