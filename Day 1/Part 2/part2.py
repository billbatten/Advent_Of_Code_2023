def main():
    with open('../input.txt', 'r') as file:
        sum = 0
        overlapsDict = {'oneight': '18', 'twone': '21', 'threeight': '38', 'fiveeight': '58', 'sevenine': '79',
                        'eightwo': '82', 'nineight': '98'}
        wordsDict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
        for line in file:
            for overlaps in overlapsDict:
                if overlaps in line:
                    line = line.replace(overlaps, overlapsDict[overlaps])

            for words in wordsDict:
                if words in line:
                    line = line.replace(words, wordsDict[words])

            numbers = [int(s) for s in line if s.isdigit()]
            if len(numbers) == 1:
                numbers.append(numbers[0])

            result = str(numbers[0]) + str(numbers[-1])
            sum += int(result)

    print(sum)
if __name__ == "__main__":
    main()
