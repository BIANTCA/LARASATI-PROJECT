```if not os.path.exists(path):
  return None
with open(path) as json_file:
  return json.load(json_file)```
