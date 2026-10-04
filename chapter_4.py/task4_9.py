def temperature_conversionOf(celcius):
    return (9/5) * celcius + 32

print("celcius", "fahrenheit")
for count in range(1, 101):
    print(count, "\t", round(temperature_conversionOf(count), 1))

