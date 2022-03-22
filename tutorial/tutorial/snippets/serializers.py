
from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User



# ====================version 2 =========================
# 基于模型直接展开的Serializer
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']


# ==================== version 1 ========================
# # 取出数据库中的数据，并将它序列化
# class SnippetSerializer(serializers.Serializer):
#     # 初始化 serializers 容器，为了之后的赋值做准备
#     # 前面定义数据类型，括号中定义通用规则
#     id = serializers.IntegerField(read_only=True)

#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)

#     # 这个 style 可以是 base_template 和 input_type
#     code = serializers.CharField(style={'base_template': 'textarea.html'})

#     linenos = serializers.BooleanField(required=False)

#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')

#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         创建 并且 返回 新的instance
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         更新并返回已经存在的 Snippet 实例
#         """
#         instance.title = validated_data.get('title',instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

    