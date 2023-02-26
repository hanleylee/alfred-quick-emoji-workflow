from fuzzywuzzy import fuzz
from alfred import AlfredList, AlfredListItem, output_to_alfred, Icon, AlfredListItemMod, AlfredListItemMods
from variables import QUERY_STR, EMOJI_LIST


def generateItem(obj):
    emoji = obj['emoji']
    alias = ', '.join(obj['aliases'])
    tags = ', '.join(obj['tags'])
    icon_name = emoji.encode('unicode-escape').decode('ASCII').replace('\\', '')

    full_desc = f'''
    emoji: {emoji}
    alias: {alias}
    tags: {tags}
    unicode: {icon_name}
    '''

    altMod = AlfredListItemMod(arg=full_desc, subtitle='Copy & Paste Full Info')
    cmdMod = AlfredListItemMod(arg=f'https://emojipedia.org/search/?q={emoji}', subtitle='Open "emojipedia.org" to view detail information')

    return AlfredListItem(
        title=alias,
        subtitle=tags,
        arg=emoji,
        icon=Icon(path=f'icons/{icon_name}.png'),
        mods=AlfredListItemMods(alt=altMod, cmd=cmdMod)
    )


def main():
    for emojiInfo in EMOJI_LIST:
        alias: list[str] = emojiInfo['aliases']
        tags: list[str] = emojiInfo['tags']
        category: str = emojiInfo['category']
        searched_content = ' '.join(alias) + ' '.join(tags) + ' ' + category
        match_score = fuzz.partial_ratio(QUERY_STR, searched_content)
        emojiInfo['match_score'] = match_score

    EMOJI_LIST.sort(reverse=True, key=lambda x: x['match_score'])

    filterd_emoji = EMOJI_LIST[:10]
    listItems = list(map(generateItem, filterd_emoji))

    output_to_alfred(alfredlist=AlfredList(items=listItems))


    # print(emojiInfo['emoji'])
if __name__ == "__main__":
    main()
