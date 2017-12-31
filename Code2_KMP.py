""""字符串匹配问题"""
def getNextArray(match):
	if len(match) == 1:
		return [-1]

	nextArr = [-1, 0]
	cn = 0
	while len(nextArr) < len(match):
		if match[len(nextArr)-1] == match[cn]:
			cn += 1
			nextArr.append(cn)
		elif cn > 0:
			cn = nextArr[cn]
		else:
			nextArr.append(0)

	return nextArr


def getIndexOf(st1, match):
	"""KMP"""
	if str1 == None or match == None or len(match) < 1 or len(str1) < len(match):
		return -1

	nextArr = getNextArray(match)

	i1, i2 = 0, 0
	while i1 < len(str1) and i2 < len(match):
		if str1[i1] == match[i2]:
			i1 += 1; i2 += 1
		elif nextArr[i2] == -1:
			i1 += 1
		else:
			i2 = nextArr[i2]

	return (i1 - len(match)) if i2 == len(match) else -1



if __name__ == '__main__':
	str1 = "abcabcababaccc"
	match = "acc"
	print(getIndexOf(str1, match))