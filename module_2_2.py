first = input("введите число 123: ")
second = input("введите число 456: ")
third =  input("введите число 789: ")
if first == second and second == third and third == first:
    print(0)
elif first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)