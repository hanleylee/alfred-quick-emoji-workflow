import json
import os
import sys

FILE_NAME = sys.argv[0]
QUERY_STR = '' if len(sys.argv) == 1 else sys.argv[1]
absolute_path = os.path.dirname(__file__)
relative_path = "config/emoji.json"
full_path = os.path.join(absolute_path, relative_path)
emoji_stream = open(full_path)
EMOJI_LIST: list[any] = json.load(emoji_stream)
ALFRED_PREFERENCES = os.getenv('alfred_preferences') # /Users/Crayons/Dropbox/Alfred/Alfred.alfredpreferences
ALFRED_PREFERENCES_LOCALHASH = os.getenv('alfred_preferences_localhash') # adbd4f66bc3ae8493832af61a41ee609b20d8705
ALFRED_WORKFLOW_UID = os.getenv('alfred_workflow_uid') # user.workflow.B0AC54EC-601C-479A-9428-01F9FD732959
ALFRED_WORKFLOW_NAME = os.getenv('alfred_workflow_name') # Quick Emoji
