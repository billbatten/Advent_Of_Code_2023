import re


def main():
    with open('../input.txt', 'r') as file:
        possibleGames = []
        for line in file:
            isPossible = True
            values = re.findall(r'\d+ [a-z]+(?:, \d+ [a-z]+)*', line)
            result = []
            for string in values:
                result += string.split(', ')

            for randomCubes in result:
                number, color = randomCubes.split(' ')
                if (color == "red" and int(number) > 12) or (color == "green" and int(number) > 13) or (
                        color == "blue" and int(number) > 14):
                    isPossible = False

            if isPossible == True:
                possibleGames.append(line)

        sum = 0
        for games in possibleGames:
            gameNumber = re.match(r'Game (\d+):', games)
            sum += int(gameNumber.group(1))

        print(sum)


if __name__ == "__main__":
    main()
