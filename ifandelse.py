a =int(input("Enter the redemption amount: "))
if a > 1000:
    print("Issued in par value and redemption in premium")
elif a < 1000:
    print("Issued in par value and redemption in discount")
else:
    print("Issued in par and redemption in par")
