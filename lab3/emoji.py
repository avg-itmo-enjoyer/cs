import re

def count_emoji(emoji, text):
    return len(re.findall(emoji, text))

if __name__ == "__main__":
    emoji = "\[\<\/"
    text = "[</"
    print(count_emoji(emoji, text))
    
