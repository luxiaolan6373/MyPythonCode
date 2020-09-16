from flask import Flask, request, render_template
from 获取3u8m链接 import BaoYu

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # 读取某一页的
    play_urls = by.get_zipai_urls(urls[0]['url'], 1)
    return render_template('index.html', title_list=title_list, play_urls=play_urls)


@app.route('/play', methods=['GET'])
def play():
    # 获取真实视频链接
    u = request.args.get('url')
    title = request.args.get('title')
    bf_url = by.get_data_url(url + u)
    print(url + u)
    return render_template('play.html', playurl='playurl + bf_url + "/480p/480p.m3u8"', title=title)


if __name__ == '__main__':
    url = "https://www.by46zo69p6lch97g7xp42utrl5p.pw:52789"
    playurl = 'https://z.weilekangnet.com:59666'
    by = BaoYu(url, playurl)
    urls = by.get_web(url)
    title_list = []
    title_list.append({'url': 'zipai', 'title': '自拍'})
    title_list.append({'url': 'wuma', 'title': '无码'})
    title_list.append({'url': 'youma', 'title': '有码'})
    title_list.append({'url': 'oumei', 'title': '欧美'})
    title_list.append({'url': 'dongman', 'title': '动漫'})
    title_list.append({'url': 'qingse', 'title': '情色'})
    title_list.append({'url': 'lieqi', 'title': '獵奇'})

    app.run(port=80)
