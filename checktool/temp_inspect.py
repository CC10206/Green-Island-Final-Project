import pathlib
p = pathlib.Path(r'c:/Users/user/Desktop/Green-Island-Final-Project/stampColl.html')
text = p.read_text(encoding='utf-8')
idx = text.index('function normalizeDateStr')
segment = text[idx:idx+260]
print(repr(segment))
