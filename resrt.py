import re

filename = input('Insert full file name: \n')

bad_newline_regex = r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n\s'
illegal_chars = '<'

def open_srt():
	with open(filename, 'r') as f:
		f_contents = f.read()
		return f_contents
		
def find_wrong_newline():
	pattern = re.compile(bad_newline_regex)
	matches = pattern.findall(open_srt())
	NumberOfErrors = len(matches)
	sentence = f'Number of newline errors: {NumberOfErrors}\n'
	print(sentence)
	for item in matches:
		print(item)

def contains_illegal_chars():
	if illegal_chars in open_srt():
		print(f'contains: {illegal_chars}')
	else:
		print(f'does not contain: {illegal_chars}')

find_wrong_newline(), contains_illegal_chars()



