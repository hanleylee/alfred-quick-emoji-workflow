import json
from pydantic import BaseModel
import sys


class Icon(BaseModel):
    path: str = ''

class AlfredListItemMod(BaseModel):
    valid: bool = True
    arg: str = ''
    subtitle: str = ''

class AlfredListItemMods(BaseModel):
    alt: AlfredListItemMod = AlfredListItemMod()
    cmd: AlfredListItemMod = AlfredListItemMod()
    ctrl: AlfredListItemMod = AlfredListItemMod()

class AlfredListItem(BaseModel):
    title: str
    subtitle: str
    arg: str = ''
    autocomplete: str = ''
    icon: Icon = Icon()
    mods: AlfredListItemMods = AlfredListItemMods()


class AlfredList(BaseModel):
    items: list[AlfredListItem]


def output_to_alfred(alfredlist: AlfredList):
    alfred_json = json.dumps(alfredlist.dict(), indent=2)
    sys.stdout.write(alfred_json)
