import requests as requests
import re
import base64

from variables import EMOJI_LIST

def main():
    data = requests.get('https://unicode.org/emoji/charts/full-emoji-list.html').text
    """For different versions, you can set version = 0 for , """
    html_search_string = r"<img alt='{}' class='imga' src='data:image/png;base64,([^']+)'>"  # '
    for obj in EMOJI_LIST:
        emoji = obj['emoji']
        icon_names = emoji.encode('unicode-escape').decode('ASCII').replace('\\', '')
        matchlist = re.findall(html_search_string.format(emoji), data)
        print(matchlist)
        if matchlist != []:
            b64 = base64.b64decode(matchlist[0])
            with open(f'../icons/{icon_names}.png', "wb") as f:
                f.write(b64)

    # print(b64)

if __name__ == "__main__":
    main()
