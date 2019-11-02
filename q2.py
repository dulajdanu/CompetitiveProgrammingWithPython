#! /usr/bin/python3 

"""
Kasun and Nuwan are best friends. Kasun is good at archery. One day they went to a carnival held in their area. There are so many things to have fun, but both these friends were interested in one game. That is some kind of archery game. This time Kasun let Nuwan to play and win the price. So Nuwan started to play that game as Kasun was guiding. The game is like this.

There are two steps in this game. The first step is to shoot to a wheel that represents x numbers. According to that number ( n ) which he shot in first target wheel and he was given n number of arrows to shoot to cylindrical targets given there as the second step of that game.

ex - : if he shoots that wheel and gets shot to number 8, he will be given 8 arrows to shoot to cylindrical targets of different size diameter.

Though Nuwan is not good in archery, he could shoot successfully only few targets at every time that they were playing. Kasun saw there was a pattern in Nuwan's shooting skill. He shoots successfully only the targets of the largest diameter.

cylindric targets have the following parameter(s): ar: an array of integers representing diameters of the cylindric targets

Input Format

The first line contains a single integer, n denoting the number of where Nuwan shot in that wheel of the target in the first step in that game. The second line contains n space-separated integers, where each integer i describes the diameters of cylindrical targets i.

Output Format

Return the number of targets that can be shot on a new line.

Sample Input 0

10
18 90 90 13 90 75 90 8 90 43

Sample Output 0

5


"""

numberofArrows = int(input())

diameterList = input().split()


def converter(x):
    return int(x)

diameterList = list(map(converter,diameterList))

maxDiameter = max(diameterList)

times = diameterList.count(maxDiameter)

print(times)
