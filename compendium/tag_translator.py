import json
import collections
import sys
import os

# replace_path = 'replaces.json'
# with open(replace_path) as f:
# 	replace_data = json.load(f)['entries']

def replace_tags_in_string(str, tags):
	swap0 = str
	swap1 = str
	if str and str.strip():
		for entry in tags:
			src_tag = '\"' + entry['id'] + '\"'
			src_tag_lower = '\"' + entry['id'].lower() + '\"'
			trans_tag = '\"' + entry['name'] + '\"'
			swap0 = swap1.replace(src_tag, trans_tag)
			swap1 = swap0.replace(src_tag_lower, trans_tag)
		swap0 = swap1.replace('coins', '닢')
	return swap0

def translate_tags(path, tags):
	with open(path) as f:
		data = json.load(f, object_pairs_hook=collections.OrderedDict)

	for entry in data['entries']:
		if 'tags' in entry:
			entry['tags'] = replace_tags_in_string(entry['tags'], tags)
		if '|' in entry['id']:
			splits = entry['id'].split('|', 1)
			entry['id'] = splits[0]
			entry['name'] = splits[1]
		# for replace_entry in replace_data:
		# 	if entry['name'] == replace_entry['name']:
		# 		entry['description'] = replace_entry['description']
	with open(path, "w") as f:
		json.dump(data, f, ensure_ascii=False, indent=2)

tag_path = 'dungeonworld.tags.json'

with open(tag_path) as f:
	tags = json.load(f)['entries']

for path in os.listdir('./'):
	if path.endswith(".json") and tag_path not in path: #and replace_path not in path:
		translate_tags(path, tags)
