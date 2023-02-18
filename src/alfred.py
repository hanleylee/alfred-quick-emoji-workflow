import json
from pydantic import BaseModel
import sys


class Icon(BaseModel):
    path: str = ''


class AlfredListItem(BaseModel):
    title: str
    subtitle: str
    arg: str = ''
    autocomplete: str = ''
    icon: Icon = Icon()


class AlfredList(BaseModel):
    items: list[AlfredListItem]


def output_to_alfred(alfredlist: AlfredList):
    alfred_json = json.dumps(alfredlist.dict(), indent=2)
    sys.stdout.write(alfred_json)
