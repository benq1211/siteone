from django.contrib.syndication.views import Feed
from .models import Post

class AllPostsRssFeed(Feed):
    #显示在聚合阅读器上的标题
    title = "benq blog"
    #通过聚合阅读器跳转到的url
    link = '192.168.1.112:8000/'

    #显示在聚合阅读器上的描述信息
    description = "benq description"


    #需要显示的内容条目
    def items(self):
        return Post.objects.all()
    #聚合器中显示的内容条目的标题
    def item_title(self, item):
        return '[%s] %s' %(item.category, item.title)

    #聚合器中显示的内容条目
    def item_description(self, item):
        return item.body

