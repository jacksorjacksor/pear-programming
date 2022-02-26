# Open file:
# test
with open("Meteorite_Landings.csv") as f:

    # List comprehensions:
    #   Reads lines from file
    #   Splits into columns (delim: comma) if the weight value can be a decimal
    super_list = [
        meteor.split(",")
        for meteor in f.readlines()[1:]
        if meteor.split(",")[4].isdecimal()
    ]

    # Sort list based on 5th column (index 4)
    super_list.sort(key=lambda x: float(x[4]), reverse=True)

    # Prints top 20
    for i in range(20):
        print(super_list[i])
