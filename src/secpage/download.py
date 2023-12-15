"""实现功能：下载专区"""

from datetime import datetime
import os
import re
import config
import requests


def get_mp4_url(video_id):
    """根据视频ID或者URL获取"""
    with open(config.VIDEO_FILE_PATH, mode='r', encoding='utf-8') as file_object:
        for lien in file_object:
            row_list = lien.split(',')
            vid = row_list[0]
            url = row_list[1]
            if video_id == vid:
                return url


def download_file(video_id, video_url):
    """下载视频"""
    current_datatime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_path = os.path.join(config.BASE_PATH, 'files', "{}-{}.mp4".format(video_id, current_datatime))
    res = requests.get(url=video_url)

    print("正在下载中...")

    # 视频总大小（字节）
    file_size = int(res.headers['Content-Length'])
    download_size = 0
    with open(file_path, mode='wb') as file_object:
        # 分块读取下载的视频文件（最多一次读128字节），并逐一写入到文件中。 len(chunk)表示实际读取到每块的视频文件大小。
        for chunk in res.iter_content(128):
            download_size += len(chunk)
            file_object.write(chunk)
            file_object.flush()
            percent = "\r{}%".format(int(round(download_size / file_size, 2) * 100))
            print(percent, end="")
        file_object.close()
    print("\n下载完成")
    res.close()


def execute():
    print("下载专区")
    while True:
        video_id = input("请输入要下载的视频ID (Q/q退出): ")
        if video_id.upper() == 'Q':
            break
        match_group = re.match("\d{7}", video_id.strip())
        if not match_group:
            print("ID不存在,请重新输入:")
            continue
        video_url = get_mp4_url(video_id)
        if not video_url:
            print("视频不存在,请重新输入:")
            continue
        download_file(video_id, video_url)
