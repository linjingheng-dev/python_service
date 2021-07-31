import datetime

from django.db import models
from django.utils import timezone

"""
模型是真实数据的简单明确的描述。它包含了储存的数据所必要的字段和行为。
Django 遵循 DRY Principle 。它的目标是你只需要定义数据模型，然后其它的
杂七杂八代码你都不用关心，它们会自动从模型生成。

来介绍一下迁移 - 举个例子，不像 Ruby On Rails，Django 的迁移代码是由你
的模型文件自动生成的，它本质上只是个历史记录，Django 可以用它来进行数据
库的滚动更新，通过这种方式使其能够和当前的模型匹配。
"""


# 定义模型
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 方便使用 Question.objects.all() 输出
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 方便使用 Choice.objects.all() 输出
    def __str__(self):
        return self.choice_text


"""
代码非常直白。每个模型被表示为 django.db.models.Model 类的子类。每个模型有
一些类变量，它们都表示模型里的一个数据库字段。每个字段都是 Field 类的实
例 - 比如，字符字段被表示为 CharField ，日期时间字段被表示为 DateTimeField 。
这将告诉 Django 每个字段要处理的数据类型。
每个 Field 类实例变量的名字（例如 question_text 或 pub_date ）也是字段名，所以
最好使用对机器友好的格式。你将会在 Python 代码里使用它们，而数据库会将它们作为列名。
你可以使用可选的选项来为 Field 定义一个人类可读的名字。这个功能在很多 Django 内部组
成部分中都被使用了，而且作为文档的一部分。如果某个字段没有提供此名称，Django 将会使
用对机器友好的名称，也就是变量名。在上面的例子中，我们只为 Question.pub_date 定义了
对人类友好的名字。对于模型内的其它字段，它们的机器友好名也会被作为人类友好名使用。
定义某些 Field 类实例需要参数。例如 CharField 需要一个 max_length 参数。这个参数的用
处不止于用来定义数据库结构，也用于验证数据，我们稍后将会看到这方面的内容。
Field 也能够接收多个可选参数；在上面的例子中：我们将 votes 的 default 也就是默认值，设
为0。
注意在最后，我们使用 ForeignKey 定义了一个关系。这将告诉 Django，每个 Choice 对象都关
联到一个 Question 对象。Django 支持所有常用的数据库关系：多对一、多对多和一对一。
"""
