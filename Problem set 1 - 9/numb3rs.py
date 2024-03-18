import re
import sys
# done

def main():
        print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r'^(?:[0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|255)\.(?:[0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|255)\.(?:[0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|255)\.(?:[0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|255)$'
    
    if re.search(pattern, ip):
        return True
    else:
        return False



if __name__ == "__main__":
    main()
