import re

def main():
    print(count(input("Text: ")))


def count(s):
    string = s.lower()
    pattern = re.findall(r"\bum\b", string)
    return len(pattern)


if __name__ == "__main__":
    main()