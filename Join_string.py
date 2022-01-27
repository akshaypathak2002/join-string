def split_and_join(line):
    # this will separate the string and make list of it when there is a space
    line = line.split(" ")
    # It will again join the string and in place of space it separated by -
    return "-".join(line)


if __name__ == "__main__":
    line = input()  # To take input
    # Simply printing the result of the split_and_join function
    print(split_and_join(line))
