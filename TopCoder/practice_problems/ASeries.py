class ASeries:
    def longest(self, values):
        result = count = 2
        values = sorted(list(values))
        temp = values[0]
        diff = values[1] - values[0]
        for i in range(2, len(values)):
            if values[i] - temp == diff:
                temp = values[i]
                count += 1
                if count > result:
                    result = count
            else:
                diff = values[i] - temp
                temp = values[i]
                count = 2
        return result


AS = ASeries()
print(AS.longest([3, 8, 4, 5, 6, 2, 2]))

# trying, 연속된 순서 말고도, 순서를 고려해야된다.
