def rounding(number):
    nearest_number = round(number)
    nearest_tenths = round(number, 1)
    nearest_hundredths = round(number, 2)
    nearest_thousands = round(number, 3)
    return nearest_number, nearest_tenths, nearest_hundredths, nearest_thousands
print(rounding(13.56449))




