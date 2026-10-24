print("        Multiplication Table")
print("    \t1\t2\t3\t4\t5\t6\t7\t8\t9")
print("--------------------------------------------------------------------------")

for i in range(1, 10):
    print(i, "|", end="\t")

    for j in range(1, 10):
        print(i * j, end="\t")

    print()
