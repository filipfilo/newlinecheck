import re

bad_newline_regex = r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n\s'
illegal_chars = '<'

def open_srt():
    """opens and returns content of input file"""
    with open(filename, 'r', encoding="utf8") as f:
        f_contents = f.read()
        return f_contents

def find_wrong_newline():
    """looks for regex from line 5 and prints results"""
    global filename
    filename = input('Insert full file name: ')
    pattern = re.compile(bad_newline_regex)
    matches = pattern.findall(open_srt())
    print(f'Number of newline errors: {len(matches)}\n')
    for item in matches:
        print(item)

def contains_illegal_chars():
    if illegal_chars in open_srt():
        print(f'contains: {illegal_chars}')
    else:
        print(f'does not contain: {illegal_chars}')

def main():
    find_wrong_newline(), contains_illegal_chars()
    again = input('\nType "y" to run again\nPress "Enter" to exit\n')
    if again=='y':
        main()
    else:
        pass

if __name__ == '__main__':
    main()
