import re
def main():
    with open('../input.txt', 'r') as file:
        power = 0
        for line in file:
            values = re.findall(r'\d+ [a-z]+(?:, \d+ [a-z]+)*', line)
            result = []
            for string in values:
                result += string.split(', ')
            max_values = {'red': 0, 'blue': 0, 'green': 0}

            for randomCubes in result:
                number, color = randomCubes.split(' ')
                number = int(number)
                if number > max_values[color]:
                    max_values[color] = number

            # Calculate the power
            power += max_values['red'] * max_values['blue'] * max_values['green']

        print(power)


if __name__ == "__main__":
    main()
