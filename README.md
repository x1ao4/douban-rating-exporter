# douban-rating-exporter
使用 douban-rating-exporter 可以导出[豆瓣](https://movie.douban.com/)用户的电影、电视剧、综艺等影视内容的评分数据。只需要提供用户 ID 就可以通过 `requests` 和 `BeautifulSoup` 库从豆瓣网站抓取数据并提取用户公开评价过的影视信息。

## 示例
假设您需要获取您的豆瓣电影评分数据，使用此脚本后，您会得到类似于下面这样的数据：
```
肖申克的救赎: 5
这个杀手不太冷: 4
霸王别姬: 5
阿甘正传: 5
美丽人生: 4
```

## 运行条件
- 安装了 Python 3.0 或更高版本。
- 安装了必要的第三方库：requests 和 BeautifulSoup。

## 使用方法
1. 将仓库克隆或下载到计算机上的一个目录中。
2. 在脚本中设置您的豆瓣 ID，将 `douban_id` 变量的值更改为您的豆瓣 ID。
3. 修改 `start.command (Mac)` 或 `start.bat (Win)` 中的路径，以指向您存放 `douban-rating-exporter.py` 脚本的目录。
4. 双击运行 `start.command` 或 `start.bat` 脚本以执行 `douban-rating-exporter.py` 脚本。
5. 脚本将开始抓取您在豆瓣上公开评价过的所有影片，并将它们的名称和评分写入到同一目录下名为 `movies.txt` 的文件中。
6. 在脚本运行过程中，您可以在控制台中看到当前正在处理的页面序号以及每部影片的名称和评分。
7. 脚本运行完成后，您可以在 `movies.txt` 文件中查看所有电影的评分数据。

## 注意事项
- 由于豆瓣网站有反爬虫机制，建议在脚本运行过程中不要进行其他与豆瓣网站相关的操作，以免被封 IP。
- 如果您有大量的电影评分数据，脚本运行时间可能会较长，请耐心等待。
<br>

# douban-rating-exporter
The douban-rating-exporter allows you to export rating data of movies, TV shows and other video content ratings data from [Douban](https://movie.douban.com/) users. By providing a user ID, it can use the `requests` and `BeautifulSoup` libraries to scrape data from the Douban website and extract publicly rated video information from the user.

## Demo
Suppose you need to get your Douban movie rating data. After using this script, you will get data similar to the following:
```
肖申克的救赎: 5
这个杀手不太冷: 4
霸王别姬: 5
阿甘正传: 5
美丽人生: 4
```

## Requirements
- Python 3.0 or higher is installed.
- The necessary third-party libraries are installed: requests and BeautifulSoup.

## Usage
1. Clone or download the repository to a directory on your computer.
2. Set your Douban ID in the script by changing the value of the `douban_id` variable to your Douban ID.
3. Modify the path in `start.command (Mac)` or `start.bat (Win)` to point to the directory where you store the `douban-rating-exporter.py` script.
4. Double-click `start.command` or `start.bat` to execute the `douban-rating-exporter.py` script.
5. The script will start scraping all publicly rated movies on Douban and write their names and ratings to a file named `movies.txt` in the same directory.
6. During the script’s execution, you can see the page number currently being processed and the name and rating of each movie in the console.
7. After the script has finished running, you can view all movie rating data in the `movies.txt` file.

## Notes
- Due to Douban’s anti-crawling mechanism, it is recommended not to perform other operations related to the Douban website during the script’s execution to avoid being blocked by IP.
- If you have a large amount of movie rating data, the script may take a long time to run. Please be patient.
