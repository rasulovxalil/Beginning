def HCF(a,b):
    smallnumber = min (a,b)
    highest_common_factor = 1

    for i in range(1,smallnumber+1):
        if a % i == 0 and  b % i == 0:
            highest_common_factor = i

    print(f"{a} and {b} number's highest factor is  {highest_common_factor} ")

HCF(40,72)




