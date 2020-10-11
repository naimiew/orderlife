from flask import render_template, request, Flask
from app import app
import connect_mysql
from .forms import ordernoForm, idnoForm, userinfoForm, updatebindcardForm
import config
import json
import ast

@app.route('/update_repay_apply')
def update_repay_apply():
    update_repay_apply = connect_mysql.connect_mysql_update_repay_apply(request.args.get('third_order_no'))
    return "还款提速已触发",update_repay_apply

@app.route('/update_borrow_state')
def update_borrow_state():
    update_borrow_state = connect_mysql.connect_mysql_update_borrow_state(request.args.get('third_order_no'),request.args.get('borrow_state'))
    state_data = request.args.get('borrow_state')
    return f"修改订单状态{state_data}已触发",update_borrow_state

@app.route('/update_repay_time')
def update_repay_time():
    update_repay_time = connect_mysql.connect_mysql_update_repay_time(request.args.get('update_repay_time_day'),request.args.get('third_order_no'),request.args.get('borrow_repay_id'))
    update_repay_time_day_data = request.args.get('update_repay_time_day')
    return f"应还日减{update_repay_time_day_data}天已触发",update_repay_time

@app.route('/update_mq_record_credit')
def update_mq_record_credit():
    update_mq_record_credit = connect_mysql.connect_mysql_update_mq_record_credit(request.args.get('third_order_no'),request.args.get('mq_record_credit_id'))
    return f"mqc提速已触发",update_mq_record_credit

@app.route('/update_mq_record_fico')
def update_mq_record_fico():
    update_mq_record_fico = connect_mysql.connect_mysql_update_mq_record_fico(request.args.get('third_order_no'),request.args.get('mq_record_fico_id'))
    return f"mqf提速已触发",update_mq_record_fico

@app.route('/update_mq_record_loan')
def update_mq_record_loan():
    update_mq_record_loan = connect_mysql.connect_mysql_update_mq_record_loan(request.args.get('third_order_no'),request.args.get('mq_record_loan_id'))
    return f"mql提速已触发",update_mq_record_loan

@app.route('/update_cl_notify_callback')
def update_cl_notify_callback():
    update_cl_notify_callback = connect_mysql.connect_mysql_cl_notify_callback(request.args.get('third_order_no'),request.args.get('cl_notify_callback_id'))
    return f"notify_callback提速已触发",update_cl_notify_callback

@app.route('/update_cl_notify_callback_re')
def update_cl_notify_callback_re():
    update_cl_notify_callback_re = connect_mysql.connect_mysql_cl_notify_callback_re(request.args.get('third_order_no'),request.args.get('cl_notify_callback_re_id'))
    return f"notify_callback重试已触发",update_cl_notify_callback_re

@app.route('/')
@app.route('/index')
def index():
    if config.TEST_REMOTE_BIND_ADDRESS[0] == config.TEST_HOST:
        if config.TEST_HOST == '47.94.175.76':
            environment = '渠道01'
        elif config.TEST_HOST == '39.106.35.160':
            environment = '渠道02'
        elif config.TEST_HOST == '39.105.213.16':
            environment = '渠道03'
        else:
            environment = '渠道未知'
    else:
        environment = '渠道配置错误'
    saysomethiong = {'way': 'GoodLuck ^_^'}
    return render_template("index.html", environment=environment, titel='Home', say=saysomethiong)


@app.route('/searchidno', methods=['GET', 'POST'])
def searchidno():
    form = idnoForm()
    if config.TEST_REMOTE_BIND_ADDRESS[0] == config.TEST_HOST:
        if config.TEST_HOST == '47.94.175.76':
            environment = '渠道01'
        elif config.TEST_HOST == '39.106.35.160':
            environment = '渠道02'
        elif config.TEST_HOST == '39.105.213.16':
            environment = '渠道03'
        else:
            environment = '渠道未知'
    else:
        environment = '渠道配置错误'
    if form.validate_on_submit():  # 某种数据校验
        # flash('third_order_no"' + form.orderno.data + '"')
        show_id_no_info = connect_mysql.connect_mysql_id_no(form.idno.data)
        return render_template('idnoinfo.html', environment=environment, title='id_no_info', form=form,
                               show_sql_str_can_loan=show_id_no_info[0], showcl=show_id_no_info[1],
                               show_sql_str_id_no=show_id_no_info[2], showini=show_id_no_info[3])
    return render_template('searchidno.html', environment=environment, title='searchidno', form=form)


@app.route('/searchtono', methods=['GET', 'POST'])
def searchtono():
    form = ordernoForm()
    if config.TEST_REMOTE_BIND_ADDRESS[0] == config.TEST_HOST:
        if config.TEST_HOST == '47.94.175.76':
            environment = '渠道01'
        elif config.TEST_HOST == '39.106.35.160':
            environment = '渠道02'
        elif config.TEST_HOST == '39.105.213.16':
            environment = '渠道03'
        else:
            environment = '渠道未知'
    else:
        environment = '渠道配置错误'
    if form.validate_on_submit():  # 某种数据校验
        # flash('third_order_no"' + form.orderno.data + '"')
        show_third_order_info = connect_mysql.connect_mysql_third_order_no(form.orderno.data)
        print(show_third_order_info)
        return render_template('orderlife.html', environment=environment, title='orderlife', form=form,
                               show_sql_str_third_order = show_third_order_info[0],
                               showtoi=show_third_order_info[1],
                               show_sql_str_borrow=show_third_order_info[2],
                               showbow=show_third_order_info[3],
                               show_sql_str_borrow_extended_info=show_third_order_info[4],
                               showbei=show_third_order_info[5],
                               show_sql_str_borrow_repay=show_third_order_info[6],
                               showbr=show_third_order_info[7],
                               show_sql_str_borrow_repay_detail=show_third_order_info[8],
                               showbrd=show_third_order_info[9],
                               show_sql_str_pay_apply=show_third_order_info[10],
                               showpa=show_third_order_info[11],
                               show_sql_str_fund_in_order_info=show_third_order_info[12],
                               showfioi=show_third_order_info[13],
                               show_sql_str_policy_apply_qa=show_third_order_info[14],
                               showpaq=show_third_order_info[15],
                               show_sql_str_mq_record_credit=show_third_order_info[16],
                               showmqc=show_third_order_info[17],
                               show_sql_str_mq_record_fico=show_third_order_info[18],
                               showmqf=show_third_order_info[19],
                               show_sql_str_mq_record_loan=show_third_order_info[20],
                               showmql=show_third_order_info[21],
                               show_sql_str_notify_callback=show_third_order_info[22],
                               showcallback=show_third_order_info[23],
                               show_sql_str_req_record_credit_sign=show_third_order_info[24],
                               showrrcs=show_third_order_info[25],
                               show_sql_str_product=show_third_order_info[26],
                               showp=show_third_order_info[27],
                               show_sql_str_product_fee=show_third_order_info[28],
                               showpf=show_third_order_info[29],
                               show_sql_str_product_interest_rate=show_third_order_info[30],
                               showpir=show_third_order_info[31],
                               show_sql_str_repay_apply=show_third_order_info[32],
                               showra=show_third_order_info[33])
    return render_template('searchtono.html', environment=environment, title='searchtono', form=form)


@app.route('/userinfo', methods=['GET', 'POST'])
def userinfo():
    form = userinfoForm()
    if config.TEST_REMOTE_BIND_ADDRESS[0] == config.TEST_HOST:
        if config.TEST_HOST == '47.94.175.76':
            environment = '渠道01'
        elif config.TEST_HOST == '39.106.35.160':
            environment = '渠道02'
        elif config.TEST_HOST == '39.105.213.16':
            environment = '渠道03'
        else:
            environment = '渠道未知'
    else:
        environment = '渠道配置错误'
    show_user_info = connect_mysql.connect_mysql_user_info(form.userinfo.data)
    tonolen = len(show_user_info[3])
    updlen = len(show_user_info[5])
    '''
    #查看获数据明细
    for show_user_info_list_size in show_user_info:
        for show_user_info_list_dict in show_user_info_list_size:
                print('获取到数据大小为' + str(show_user_info_list_dict))
    '''
    return render_template('userinfo.html', environment=environment, title='userinfo', form=form,tonolen=tonolen,updlen=updlen,
                           show_sql_str_user_id=show_user_info[0],
                           showuio=show_user_info[1],
                           show_sql_str_third_order_info=show_user_info[2],
                           showtono=show_user_info[3],
                           show_sql_str_user_push_data=show_user_info[4],
                           showupd=show_user_info[5],
                           show_sql_str_credit_account_data=show_user_info[6],
                           showcad=show_user_info[7],
                           show_sql_str_credit_account_info=show_user_info[8],
                           showcai=show_user_info[9],
                           show_sql_str_credit_account_change_detail=show_user_info[10],
                           showcacd=show_user_info[11],
                           show_sql_str_bank_card_list=show_user_info[12],
                           showbcl=show_user_info[13],
                           show_sql_depository_register_info=show_user_info[14],
                           showdri=show_user_info[15],
                           show_sql_str_jdcredit_req_log=show_user_info[16],
                           showjrl=show_user_info[17])


@app.route('/updatebindcard', methods=['GET', 'POST'])
def updatebindcard():
    form = updatebindcardForm()
    if config.TEST_REMOTE_BIND_ADDRESS[0] == config.TEST_HOST:
        if config.TEST_HOST == '47.94.175.76':
            environment = '渠道01'
        elif config.TEST_HOST == '39.106.35.160':
            environment = '渠道02'
        elif config.TEST_HOST == '39.105.213.16':
            environment = '渠道03'
        else:
            environment = '渠道未知'
    else:
        environment = '渠道配置错误'
    show_card_info = connect_mysql.connect_mysql_update_bindcard(form.card_no.data,form.user_id.data,form.phone.data)
    return render_template('updatebindcard.html', environment=environment, title='updatebindcard',showbcl=show_card_info)


# 注册json格式化，自定义的过滤器
@app.template_filter("jsonformat")
def jsonformat(jsondata):
    # eval （不支持true,null等）  str转换为list  为了安全 用ast.literal_eval
    if (isinstance(jsondata, str)):
        json_format_data = json.dumps(ast.literal_eval(jsondata), ensure_ascii=False, sort_keys=True, indent=4)
        return json_format_data
    # 这个只是知识点  实际上  这样不对 str转换为list可以直接用list(str)来转换，同时可以使用split函数将str转换为list
    elif (isinstance(jsondata, list)):
        json_format_data = json.dumps(jsondata, ensure_ascii=False, sort_keys=True, indent=4)
        return json_format_data
    else:
        return type(jsondata)


if __name__ == '__main__':
    app.run()
