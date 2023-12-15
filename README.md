## 项目：梨视频（短视频）资讯平台
#### 需求：
- 新闻专区（每页显示10条），提示用户输入页码，根据页码显示指定页面的数据。
    - 提示用户输入页码，根据页码显示指定页面的数据。
    - 当用户输入的页码不存在时，默认显示第1页
- 搜索专区
    - 用户输入关键字，根据关键词筛选出所有匹配成功的短视频资讯。
    - 支持的搜索两种搜索格式：
        - `id=1715025`，筛选出id等于1715025的视频（video.csv的第一列）。
        - `key=文本`，模糊搜索，筛选包含关键字的所有新闻（video.csv的第二列）。
- 下载专区
    - 用户输入视频id，根据id找到对应的mp4视频下载地址，然后下载视频到项目的files目录。
        - 视频的文件名为：`视频id-年-月-日-时-分-秒.mp4`
     
  
## 代码框架

![image](https://github.com/cuiziwenn/python/assets/69893963/23717297-4efe-41db-87a8-4a49a9416459)
