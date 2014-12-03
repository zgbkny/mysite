# coding=utf-8
from django.db import models

# Create your models here.

#用户类型（管理员、经销商等）
class UserType(models.Model):
	name = models.CharField(max_length = 50)

#用户（活动，票的数量）
class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

#主办方
class Organizer(models.Model):
	name = models.CharField(max_length = 200)

#活动类型
class ActivityType(models.Model):
	name = models.CharField(max_length = 200)


#票类型 与活动对应
class TicketType(models.Model):
	name = models.CharField(max_length = 20)
	fee = models.IntegerField()

#票 单个的一张票
class Ticket(models.Model):
	ticketType = models.ForeignKey(TicketType)
	code = models.CharField(max_length = 50) 					



#活动
class Activity(models.Model): 
#	name = models.CharField(max_length = 200)
	#organizer = models.ForeignKey(Organizer) 		#主办方是不是只有一个
	#activityType = models.ForeignKey(ActivityType)  #活动类型

	startTime = models.DateTimeField()              #活动的开始时间
	stopTime = models.DateTimeField()				#活动的结束时间
	startSellTime = models.DateTimeField()          #票的停止售票时间
	stopSellTime = models.DateTimeField()            #票的停止销售时间
#	location = models.CharField(max_length = 1000)
#	logo = models.CharField(max_length = 200)
#	details = models.TextField()
	#ticket = models.ForeignKey(TicketType)


#管理员对每个经销商关于某个活动的设置，经销商取数据时需要验证
class ActivitySetting(models.Model):
	activity = models.ForeignKey(Activity)
	user = models.ForeignKey(User)