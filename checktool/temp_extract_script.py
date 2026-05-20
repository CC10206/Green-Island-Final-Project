import pathlib
path = pathlib.Path(r'c:/Users/user/Desktop/Green-Island-Final-Project/stampColl.html')
text = path.read_text(encoding='utf-8')
start = text.index('<script>') + len('<script>')
end = text.rindex('</script>')
script = text[start:end]
with open('temp_script.js','w', encoding='utf-8') as f:
    f.write(script)
print('wrote temp_script.js', len(script), 'chars')
