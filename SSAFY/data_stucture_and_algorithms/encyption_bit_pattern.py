num = list(map(lambda x: int(x, 16), input()))  # 0269FAC9A0
s = ''
for i in num[::-1]:
    for j in range(4):
        s += '1' if i & (1 << j) else '0'
dec = {'01100': '0', '10010': '1', '10111': '2', '00011': '3', '10001': '4', '11011': '5', '10100': '6', '01111': '7',
       '00110': '8', '11101': '9'}
result = []
i = 0
while i < len(s):
    if s[i] == '1':
        result.append(dec[s[i + 1:i + 6]])
        i += 6
    else:
        i += 1
print(",".join(result[::-1]))
