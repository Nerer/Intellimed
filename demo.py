import csv

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


code_csv_file = 'ICD-10-CSV/codes.csv'
desc_to_cat = {}
cat_to_lower = {}
with open(code_csv_file) as f:
	codereader = csv.reader(f, delimiter = ',')
	for eachLine in codereader:
		desc_to_cat[eachLine[5]] = eachLine[0]
		if eachLine[0] not in cat_to_lower:
			cat_to_lower[eachLine[0]] = {}
			cat_to_lower[eachLine[0]][eachLine[3]] = eachLine[1]
		else:
			cat_to_lower[eachLine[0]][eachLine[3]] = eachLine[1]



while True:
	print('Please input a disease name:')
	d = input()
	if d == 'None':
		break
	matched_desc = []
	for key in desc_to_cat.keys():
		if d in key:
			matched_desc.append(key)
	print('Please enter the number cooresponding to the category descriptions below')
	idx = 0
	for key in matched_desc:
		idx += 1
		print(idx, key)

	d = input()
	if not RepresentsInt(d) or int(d) <= 0 or int(d) > len(matched_desc):
		print('Invalid input. Try again')
	d = int(d) - 1

	cat = desc_to_cat[matched_desc[d]]
	lower_codes = cat_to_lower[cat]
	full_descs = []
	for key in lower_codes.keys():
		full_descs.append(key)
	
	print('Please enter the number cooresponding to detailed description choice')
	idx = 0
	for key in full_descs:
		idx += 1
		print(idx, key)
	
	d = input()

	if not RepresentsInt(d) or int(d) <= 0 or int(d) > len(lower_codes):
		print('Invalid input. Try again')
	d = int(d) - 1

	print('According to you description, the corresponding icd-10 code is:', cat + lower_codes[full_descs[d]])



