#https://cs50.harvard.edu/python/2022/psets/7/watch/

import re
import sys

'''
def main():
    result = parse(input("HTML: "))
    if not parse == None:
        print(result)
        sys.exit()
    else:
        sys.exit('None')
'''
def main():
    print(parse(input("HTML: ")))

def parse(s):
    youtube_url_pattern = r'src="(http[s]?://(?:www\.)?youtube\.com/embed/[^"]+)"'
    matches = re.search(youtube_url_pattern, s)
    if matches:
        modify = re.sub(r'be\.com/embed','.be' , matches.group(1))
        if 'www' in modify:
            modify_1 = re.sub(r'www\.','', modify)
            if 'https' not in modify_1:
                modify_2 = re.sub('http','https',modify_1)
                return modify_2
            else:
                return modify_1
        else:
            if 'https' not in modify:
                modify_1 = re.sub('http','https', modify)
                return modify_1
            else:
                return modify
    else:
        return None


if __name__ == "__main__":
    main()
