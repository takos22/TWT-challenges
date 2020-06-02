def yearToCentury(year):
    """Gets the century of a year.

    Parameters:
        year (int): year to convert into century.

    Returns:
        int: century of the year.
    """

    century = 1 + ((year - 1) // 100)
    return century


print(yearToCentury(355))  # 4
print(yearToCentury(5698))  # 57
print(yearToCentury(700))  # 7
