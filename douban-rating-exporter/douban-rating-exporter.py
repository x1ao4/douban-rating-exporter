import re
import requests
import time
from bs4 import BeautifulSoup

# 设置用户的豆瓣 ID
douban_id = 'your_douban_id'

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 初始化变量
start = 0
page_num = 1
movies = []
unrated_movies = []

# 打开文件并准备写入数据
with open('movies.txt', 'w', encoding='utf-8') as f:
    # 循环遍历所有页面
    while True:
        # 获取网页内容
        url = f'https://movie.douban.com/people/{douban_id}/collect?start={start}&sort=time&rating=all&filter=all&mode=list'
        res = requests.get(url, headers=headers)

        # 解析网页内容
        soup = BeautifulSoup(res.text, 'html.parser')

        # 提取影片名称和评分数据
        page_movies = soup.find_all('div', class_='item-show')
        if not page_movies:
            break

        # 打印页数序号
        print(f'正在导出第 {page_num} 页\n')

        # 等待 2 秒
        time.sleep(2)

        has_rating = False

        for movie in page_movies:
            title_text = movie.find('div', class_='title').text.strip()
            title_parts = re.split(r'(?<=\s)/', title_text)
            title = title_parts[0].strip()
            title = re.sub(r'\s+', ' ', title)
            title = title.replace(' [可播放]', '')
            rating_element = movie.find('div', class_='date').find('span')
            if rating_element:
                has_rating = True
                rating = rating_element['class'][0][-3]
                movies.append((title, rating))
                print(f'{title}: {rating}')
                f.write(f'{title}: {rating}\n')
                f.flush()
            else:
                unrated_movies.append(title)

        if has_rating:
            print()

        # 更新 start 值以获取下一页内容
        start += 30

        # 更新页数序号
        page_num += 1

# 统计影片数量
movie_count = len(movies)
unrated_movie_count = len(unrated_movies)

# 打印统计信息
print(f'共有 {unrated_movie_count} 部影片没有评分，它们是: \n')
for title in unrated_movies:
    print(title)

print(f'\n共处理 {movie_count + unrated_movie_count} 部影片')
print(f'共导出 {movie_count} 部影片的评分')
