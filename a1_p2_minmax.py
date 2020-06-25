#Course: CS261 - Data Structures
# Student Name: Joel Chenoweth
# Assignment:1 min_max
# Description: Min_Max returns the highest and lowest integer from a list of integers


def min_max(list) -> ():
    """
This function is used to compute the maximum and minimum of values passed in as an argument. It gives the largest value and
smallest value respectively.  It doesn't use any built in functions such as max(), min(), or sort
    """
    for i in list:
        mx = list[0]
        mn = list[0]

        for num in list:
            if mx < num:
                mx = num
            else:
                if mn > num:
                    mn = num

        return mn, mx,
    return None, None





# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(min_max([1, 2, 3, 4, 5]))

    # example 2
    print(min_max([8, 7, 6, -5, 4]))

    # example 3
    print(min_max([]))