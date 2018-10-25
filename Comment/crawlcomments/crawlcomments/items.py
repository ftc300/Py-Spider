# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field



# class CommentItem(scrapy.Item):
#     content = scrapy.Field()
#     time = scrapy.Field()
#     platform = scrapy.Field()
#     star = scrapy.Field()

class JDCommentItem(Item):
    user_name = Field()  # 评论用户的名字
    user_ID = Field()  # 评论用户的ID
    userProvince = Field()  # 评论用户来自的地区
    content = Field()  # 评论内容
    good_ID = Field()  # 评论的商品ID
    good_name = Field()  # 评论的商品名字
    date = Field()  # 评论时间
    replyCount = Field()  # 回复数
    score = Field()  # 评分
    status = Field()  # 状态
    title = Field()
    userLevelId = Field()
    productColor = Field()  # 商品颜色
    productSize = Field()  # 商品大小
    userLevelName = Field()  # 银牌会员，钻石会员等
    userClientShow = Field()  # 来自什么 比如来自京东客户端
    isMobile = Field()  # 是否来自手机
    days = Field()  # 天数
    commentTags = Field()  # 标签
class XMCommentItem(Item):
    comment_id = Field()
    user_id = Field()
    user_name  = Field()
    user_avatar = Field()
    comment_content = Field()
    comment_grade = Field()
    add_time = Field()
    add_timestamp = Field()
    up_num = Field()
    down_num = Field()
    reply_content = Field()
    reply_up_num = Field()
    reply_time = Field()
    comment_labels = Field()
    comment_title = Field()
    user_reply_num = Field()
    is_top = Field()
    up_rate = Field()
    average_grade = Field()
    total_grade = Field()
    spec_value = Field()
    site_id = Field()
    comment_images = Field()
    comment_videos = Field()
    marks = Field()
    tags = Field()