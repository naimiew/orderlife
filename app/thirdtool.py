#-*- coding:utf-8 -*-
import datetime
import json


class DateEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime.datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj, datetime.date):
			return obj.strftime("%Y-%m-%d")
		else:
			return json.JSONEncoder.default(self, obj)



		'''
		<b style="color:Crimson"> 1</b>
			|
			{% if a == '1' %}日{% elif a == '2' %}月
            {% elif a == '3' %}年{% elif a == '3' %}年
            {% else %}未知{% endif %}&emsp;
		
		
		keys = [str(x) for x in numpy.arange(len(show_id_no_info))]
		list_json = dict(zip(keys, show_id_no_info))
		str_json = json.dumps(list_json, indent=2, ensure_ascii=False,cls=thirdtool.DateEncoder)  # json转为string
		'''