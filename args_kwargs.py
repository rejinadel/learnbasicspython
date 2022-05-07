def fun(**kwargs):
    """_summary_we created keyword arguments and it was passed in name 
    and the reverse of the name was returned

    Returns:
        str: The name of the kwargs was returned in reverse
    """
    return kwargs.get("name")[::-1]

#print the function
print(fun(name="Rezna"))