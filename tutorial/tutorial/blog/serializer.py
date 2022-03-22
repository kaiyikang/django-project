from wsgiref.validate import validator
from rest_framework import serializers

from blog.models import Article
from blog.models import User

class UserSerializer(serializers.ModelSerializer):
    # 通过作者查文章
    articles = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True,
        view_name="article-detail")

    class Meta:
        model = User
        fields = ('id', 'username', 'articles')
        read_only_fields = ('id','username')


# 定义一个validators，并且在serializer的时候确认进去
# def title_gt_90(value):
#     if len(value) < 20:
#         raise serializers.ValidationError('the length of title should be longer than 90')

# def must_have_django(value):
#     if 'django' not in value.lower():
#             raise serializers.ValidationError("Article is not about Django")

class ArticleSerializer(serializers.ModelSerializer):
    # author 不可见，同时自动补全
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # 为了author显示的是作者，而不是id
    # author = serializers.ReadOnlyField(source="author.username")
    
    # 为了显示更多的信息, 别忘记了read_only = true
    author = UserSerializer(read_only =True)
    
    # get_xxxxx_display 可以将 xxxx 的 具体内容暴露出来
    # 为了对status能够修改，增加一个只读的 full_status
    full_status = serializers.ReadOnlyField(source="get_status_display") 
    
    # 将任何数据添加到对象的序列化列表中，通常是model中不存在的fields
    cn_status = serializers.SerializerMethodField()

    # title = serializers.CharField(validators = [must_have_django, title_gt_90])


    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id','create_date','author')
        # depth = 1

    def get_cn_status(self,obj):
        """
        对应 cn_status field
        """
        if obj.status == 'p': return "已发表"
        elif obj.status == 'd': return "草稿"
        else: return ''
