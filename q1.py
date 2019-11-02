#! /usr/bin/python3 
#above line is added to  set the path of python in linux
#to make this file executable type chmod +x q1.py
"""
Mr. Camillus is a politician who is going to compete next parliament election. He done nothing for his voters in his last attempt. His private advisor advises him to distribute some money among his most loyal voters with different financial backgrounds, to businessman to beggar. So, the amount which given to voter must depend on his/her financial background.
His secretary created a list of loyal voters and amount should be given to them and also, they spare money to each Divisional Secretariats. But they have problem that they need to satisfy maximum number of voters using given money to each division. so, they need your help to find an effective money distribution way by maximizing the number of satisfied voters.
There are N voters, numbered 1,2,3,4.....,N. For each i (1<i<N ) , Voter i will be happy if he/she gets exactly amount of money. You have to maximize the number of satisfied voters by optimally distributing the x 
amount of money. Find the maximum number of satisfied voters. (For simplicity of calculations let’s assume that our money unit is x1000 times valuable than current value)

Input Format

The first line contains two integers N (number of voters) and x (amount of money can be spent).

The second line contains N space seperated integers a1,a2,a3 ....,aN  denoting the amount need to give to i th voter


Output Format

Print the maximum possible number of satisfied voters.

Sample Input 0

3 10
20 30 10

Sample Output 0

1

Explanation 0

There are 3 voters and the voter who requesting 10 can only be satisfied.
"""

votersAndAmountSpend = input().split()


def converter(x):
    return int(x)


votersAndAmountSpend = list(map(converter, votersAndAmountSpend))


amountsForEachPerson = input().split()

amountsForEachPerson = list(map(converter, amountsForEachPerson))

amountsForEachPerson.sort()
noOfSatisfied = 0
for i in amountsForEachPerson:
    if(votersAndAmountSpend[1] >= i):
        noOfSatisfied += 1
        votersAndAmountSpend[1] -= i

print(noOfSatisfied)
