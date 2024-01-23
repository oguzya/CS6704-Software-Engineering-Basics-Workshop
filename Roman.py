dictRomanToInt = {
	'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I': 1
}

# this function will convert integer to roman
# the idea is try to use the biggest roman character value
def convertIntToRoman(num):
	ans = ""
	for k,v in dictRomanToInt.items():
		while (num >= v):
			num -= v
			ans += k
	return ans


# this function will convert roman to int
# the idea is using for loop for each character on the roman string then add up to the final answer based on the dictionary
def convertRomanToInt(strRoman):
	ans = 0
	for c in strRoman:
		ans += dictRomanToInt[c]
	return ans


print(convertIntToRoman(56))
print(convertRomanToInt('LVI'))
	
	
