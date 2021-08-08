"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
"""
def findJudge(n: int, trust):
    if len(trust) == 0 and len(trust) == n-1:
        return n
    elif len(trust) == 0 and len(trust) < n-1:
        return -1
    give,take = [],[]
    for each in trust:
        give.append(each[0])
        take.append(each[1])
    for each in set(take):
        if take.count(each) == n-1 and each not in give:
            return each
    return -1