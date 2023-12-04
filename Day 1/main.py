def main():
    with open('input.txt', 'r') as file:
        sum = 0
        for line in file:
            numbers = [int(s) for s in line if s.isdigit()]
            if len(numbers) == 1:
                numbers.append(numbers[0])

            result = str(numbers[0]) + str(numbers[-1])
            sum += int(result)

    print(sum)
if __name__ == "__main__":
    main()
