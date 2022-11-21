with open("C:\PythonPractises\Phython_Challenge\data\countries-data.py", errors="ignore") as f:
    file = f.readlines()

languages = []
for i, item in enumerate(file):
    if 'languages' in item:
        #print(str(i) + str(item))
        j = 1
        while ']' not in file[i+j]:
            languages.append(file[i+j])
            j += 1

languages = [lang.rstrip('",\n').lstrip('            "') for lang in languages]
print(languages)
print(len(languages))

distinct_language = set(languages)
language_dict = {lang : languages.count(lang) for lang in distinct_language}
sorted_language = dict(sorted(language_dict.items(), key=lambda item: item[1], reverse=True))
ten_most_spoken_languages = dict(list(sorted_language.items())[:10])
print(ten_most_spoken_languages)







"""
""""""
for country in countries:
    if 'land' in country:
        print(country)"""
