import re

def main():
    s = input("HTML: ")
   
    src = parse(s)
    print(validate(src))


def parse(s):
    elements = s.split()
    for element in elements:
        if "src" in element:
            src = element
            return src.split("\"")[1]
    return None


def validate(src):
    if re.search(r"^(http){1}s?:?(\/\/)+(www)?\.(youtube)?\.+(com)?\/+(embed)+\/+[a-zA-Z0-9]*$", src):
        unique = src.split("embed")[1]
        return "https://youtu.be" + unique
    else:
        None

if __name__ == "__main__":
    main()