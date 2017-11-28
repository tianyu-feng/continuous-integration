largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done": break
    try:
        fnum = float(num)

    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = fnum
    if smallest is None:
        smallest = fnum
    if largest < fnum:
        largest = fnum
    if smallest > fnum:
        smallest = fnum



print("Maximum", largest)
print("Minimum", smallest)