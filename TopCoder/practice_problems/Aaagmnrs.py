class Aaagmnrs:
    def anagrams(self, phrases):
        anagram = set()
        result = []
        for phrase in phrases:
            temp = []
            for spelling in phrase:
                if spelling != " ":
                    alpha = spelling.lower()
                    if temp:
                        if(temp[-1] < alpha):
                            temp.append(alpha)
                        else:
                            for i in range(len(temp)):
                                if alpha <= temp[i]:
                                    temp.insert(i, alpha)
                                    break
                    else:
                        temp.append(alpha)
            temp = "".join(temp)
            if temp not in anagram:
                result.append(phrase)
                anagram.add(temp)
        return tuple(result)


a = Aaagmnrs()
print(a.anagrams(("Radar ghost jilts Kim", "patched hers first",
                  "DEPTH FIRST SEARCH", "DIJKSTRAS ALGORITHM")))
