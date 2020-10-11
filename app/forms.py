# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


# 导入 Form 类，接着导入两个我们需要的字段类，TextField 和 BooleanField。
class ordernoForm(FlaskForm):
	orderno = StringField('orderno', validators=[DataRequired()])  # DataRequired 验证器只是简单地检查相应域提交的数据是否是空
	
class idnoForm(FlaskForm):
	idno = StringField('idno', validators=[DataRequired()])

class userinfoForm(FlaskForm):
	userinfo = StringField('userinfo', validators=[DataRequired()])

class updatebindcardForm(FlaskForm):
	card_no = StringField('card_no', validators=[DataRequired()])
	user_id = StringField('userid', validators=[DataRequired()])
	phone = StringField('phone', validators=[DataRequired()])