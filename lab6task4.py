import json

INPUT_FILE = "input.csv"
	# TODO реализовать конвертер из csv в json
def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
	listdict = []
	with open(filename) as f:
		header = f.readline().replace(new_line, '')
		headers_list = header.split(delimiter)
		for row in f:
			row = row.replace(new_line, '')
			values_list = row.split(delimiter)
			listdict.append(dict(zip(headers_list, values_list)))

	return listdict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
