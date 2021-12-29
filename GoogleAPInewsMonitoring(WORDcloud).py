import requests
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

print('Введите начальную дату поиска статей, не раньше, чем:', end=' ')
print((datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
print('Формат ввода: ГГГГ-ММ-ДД')
x = input()
if abs((datetime.strptime(x, '%Y-%m-%d') - datetime.now())) >= timedelta(days=31):
    print('Введена слишком ранняя начальная дата для поиска')
    raise SystemExit
y = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

stopWords = set(stopwords.words('english'))
data = {}
while x != y:
    inquiry = requests.get('https://newsapi.org/v2/everything?q=russia&pageSize=100&page=1&from=' + x + '"&to=' + x + '&apiKey=3798bdf6a3a64d158c7e848d12c8df39')
    jsonText = json.loads(inquiry.text)

    text = ""

    try:
        for item in jsonText['articles']:
            text += str(item['content']).lower()
    except LookupError:
        print('The free Google News API has expired. Try it in 12 hours.')
        raise SystemExit

    Tokens = word_tokenize(text)
    filteredText = [word for word in Tokens if word not in stopWords and word.isalpha() and word != 'chars']

    for word in filteredText:
        data[word] = data.get(word, 0) + 1

    x = (datetime.strptime(x, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')

TOP50 = dict(sorted(data.items(), key=lambda f: -f[1])[:50])

a, b = np.ogrid[:300, :300]
mask = (a - 150) ** 2 + (b - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)
wc = WordCloud(max_words=50, background_color="white", mask=mask).generate_from_frequencies(TOP50)

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
