from selenium.webdriver.common.by import By

"""以下为服务器域名配置地址"""
# 管理员端地址-测试地址
admin_url = "http://test-ccat.66nao.cn/#/admin/login"
# 管理员端地址-付凯本地
# admin_url = "http://192.168.1.241/#/admin/login"

# 医生端地址-测试地址
doctor_url = "http://test-ccat.66nao.cn/#/doctor/login"
# 医生端地址-付凯本地
# doctor_url = "http://192.168.1.241/#/doctor/login"

# 儿童端地址
child_url = ""

"""以下为 管理员端-登陆页面 配置数据"""
# 获取邮箱
admin_login_get_email = By.XPATH, '//span'
# 密码输入框
admin_login_password_input = By.XPATH, '//input'
# 登录按钮
admin_login_btn = By.XPATH, '//button'
# 获取错误文本信息
admin_login_err = By.XPATH, '//p[@class="login-error"]'
# 忘记密码按钮
admin_login_porget_password_btn = By.XPATH, '//a[text()="忘记密码"]'
# 医生登录按钮
admin_login_doctor_btn = By.XPATH, '//a[text()="医生登录"]'
# 登录log
admin_login_log = By.XPATH, '//h3'

"""以下为 管理员端-登陆-忘记密码①页面 配置数据"""
# 返回登录页面按钮
admin_login_porget_password_login_btn = By.XPATH, '//span[contains(text(),"返回登录页面")]'
# 获取验证码按钮
admin_login_porget_password_get_code = By.XPATH, '//button[contains(text(),"获取验证码")]'
# 验证码输入框[1]
admin_login_porget_password_input_code1 = By.XPATH, '(//div[@class="split-input-container"]/input)[1]'
# 验证码输入框[2]
admin_login_porget_password_input_code2 = By.XPATH, '(//div[@class="split-input-container"]/input)[2]'
# 验证码输入框[3]
admin_login_porget_password_input_code3 = By.XPATH, '(//div[@class="split-input-container"]/input)[3]'
# 验证码输入框[4]
admin_login_porget_password_input_code4 = By.XPATH, '(//div[@class="split-input-container"]/input)[4]'
# 获取验证码提示信息
admin_login_porget_password_get_err = By.XPATH, '(//p[@class="login-error"])[1]'
"""以下为 管理员端-登陆-忘记密码②页面 配置数据"""
# 新密码输入框
admin_login_porget_password_new_input = By.XPATH, '//input[@placeholder="输入新密码"]'
# 设定新密码按钮
admin_login_porget_password_new_btn = By.XPATH, '//button[contains(text(),"设定新密码")]'

"""以下为 管理员端-医生列表页面 配置数据"""
# 登录成功log
admin_doctor_list_log = By.XPATH, '//h3[@class="welcomeTitle"]'
# 创建医生按钮
admin_doctor_list_create_btn = By.XPATH, '//div[contains(text(),"创建医生")]'
# 搜索输入框
admin_doctor_list_search_input = By.XPATH, '//input[@placeholder="搜索医生"]'
# 搜索按钮
admin_doctor_list_search_btn = By.XPATH, '//i[@class="icon-search"]'
# 排序方式one
admin_doctor_list_sort_one = By.XPATH, '//input[@placeholder="创建日期"]'
# 排序方式：按创建日期排序
admin_doctor_list_sort_data = By.XPATH, '//span[contains(text(),"按创建日期排序")]'
# 排序方式：按姓名拼写排序
admin_doctor_list_sort_name = By.XPATH, '//span[contains(text(),"按姓名拼写排序")]'
# 排序方式two
admin_doctor_list_sort_two = By.XPATH, '//input[@placeholder="升序"]'
# 排序方式：升序
admin_doctor_list_sort_asc = By.XPATH, '//span[contains(text(),"升序")]'
# 排序方式：降序
admin_doctor_list_sort_desc = By.XPATH, '//span[contains(text(),"降序")]'

# 医生列表按钮
admin_doctor_list_btn = By.XPATH, '//div[text()="医生"]'
# 账户按钮按钮
admin_doctor_list_account_btn = By.XPATH, '//div[text()="账户"]'

# 医生列表第一个医生的姓名
admin_doctor_list_first_name = By.XPATH, '((//tr[@class="el-table__row"])[1]/td)[1]/div'
# 医生列表第二个医生的姓名
admin_doctor_list_second_name = By.XPATH, '((//tr[@class="el-table__row"])[2]/td)[1]/div'
# 医生列表第三个医生的姓名
admin_doctor_list_third_name = By.XPATH, '((//tr[@class="el-table__row"])[3]/td)[1]/div'

# 医生列表第一个医生的详情
admin_doctor_list_first_detail = By.XPATH, '((//tr[@class="el-table__row"])[1]/td)[5]/div/img'
# 医生列表第二个医生的详情
admin_doctor_list_second_detail = By.XPATH, '((//tr[@class="el-table__row"])[2]/td)[5]/div/img'
# 医生列表第三个医生的详情
admin_doctor_list_third_detail = By.XPATH, '((//tr[@class="el-table__row"])[3]/td)[5]/div/img'

"""以下为 管理员端-医生列表-创建医生页面 配置数据"""
# 医生姓名输入框
admin_create_doctor_name_input = By.XPATH, '//input[@placeholder="输入医生姓名"]'
# 医生身份证号输入框
admin_create_doctor_num_input = By.XPATH, '//input[@placeholder="输入医生身份证号"]'
# 获取错误文本信息
admin_create_doctor_get_err = By.XPATH, '//p[@class="error-center"]'
# 创建按钮
admin_create_doctor_btn = By.XPATH, '//button[@class="admincreate-button Universal"]'
# 关闭按钮
admin_create_doctor_close_btn = By.XPATH, '//img[@class="postionImage"]'

"""以下为 管理员端-医生详情页面 配置数据"""
# 医生详情-账号未激活
admin_doctor_detail_status = By.XPATH, '//h6/following-sibling::span'
# 医生详情-账号冻结中
admin_doctor_detail_frozen_status = By.XPATH, '(//h6/following-sibling::span)[2]'
# 医生详情-医生姓名
admin_doctor_detail_name = By.XPATH, '(//p[@class="name-right"])[1]'
# 医生详情-姓名修改按钮
admin_doctor_detail_name_change = By.XPATH, '(//p[@class="name-right"])[1]/button'
# 修改姓名弹窗-姓名输入框
admin_doctor_detail_pop_name_input = By.XPATH, '//input[@placeholder="输入姓名"]'
# 修改姓名弹窗-修改按钮
admin_doctor_detail_pop_name_change = By.XPATH, '(//button[@class="mainbutton"])[1]'
# 医生详情-性别
admin_doctor_detail_sex = By.XPATH, '(//p[@class="name-right"])[2]'
# 医生详情-医生身份证号
admin_doctor_detail_num = By.XPATH, '(//p[@class="name-right"])[3]'
# 医生详情-未激活-手机号
admin_doctor_detail_no_phone = By.XPATH, '(//p[@class="name-right"])[4]/span[1]'
# 医生详情-已激活-手机号
admin_doctor_detail_yes_phone = By.XPATH, '(//p[@class="name-right"])[4]/span[2]'
# 医生详情-手机号修改按钮
admin_doctor_detail_phone_change = By.XPATH, '(//p[@class="name-right"])[4]/button'

# 修改手机号弹窗-手机号输入框
admin_doctor_detail_pop_phone_input = By.XPATH, '//input[@placeholder="输入手机号"]'
# 修改手机号弹窗-修改按钮
admin_doctor_detail_pop_phone_change = By.XPATH, '(//div[@class="bottom-center"])[2]/button'
# 修改手机号弹窗-获取错误文本信息
admin_doctor_detail_pop_get_err = By.XPATH, '(//div[@class="bottom-center"])[2]/preceding-sibling::p'
# 修改手机号弹窗-关闭按钮
admin_doctor_detail_pop_phone_close = By.XPATH, '(//img)[3]'

# 医生详情-单位
admin_doctor_detail_unit = By.XPATH, '(//p[@class="name-right"])[5]'

# 医生详情-创建时间
admin_doctor_detail_create_time = By.XPATH, '(//p[@class="name-right"])[6]'

# 医生详情-备注
admin_doctor_detail_remark = By.XPATH, '(//p[@class="name-right"])[7]/span'
# 医生详情-备注修改按钮
admin_doctor_detail_remark_change = By.XPATH, '(//p[@class="name-right"])[7]/button'

# 修改备注弹窗-备注输入框
admin_doctor_detail_pop_remark_input = By.XPATH, '//textarea'
# 修改备注弹窗-修改按钮
admin_doctor_detail_pop_remark_change = By.XPATH, '(//div[@class="bottom-center"])[3]/button'

# 冻结医生按钮
admin_doctor_detail_frozen_btn = By.XPATH, '//button[contains(text(),"冻结医生")]'
# 冻结医生窗口-冻结
admin_doctor_detail_pop_frozen_btn = By.XPATH, '(//button[contains(text(),"冻结")])[3]'
# 解除冻结按钮
admin_doctor_detail_unfreeze_btn = By.XPATH, '//button[contains(text(),"解除冻结")]'
# 解除冻结窗口-解冻
admin_doctor_detail_pop_unfreeze_btn = By.XPATH, '//button[contains(text(),"解冻")]'

"""以下为 管理员端-账户页面 配置数据"""
# 获取邮箱文本
admin_account_get_email = By.XPATH, '(//p[@class="name-right"])[3]'
# 邮箱-修改按钮
admin_account_email_change = By.XPATH, '(//p[@class="name-right"])[3]/button'
# 获取邮箱验证码按钮
admin_account_pop_get_code = By.XPATH, '//button[contains(text(),"获取邮箱验证码")]'
# 验证码输入框[1]
admin_account_pop_code_input1 = By.XPATH, '(//div[@class="split-input-container"]/input)[1]'
# 验证码输入框[2]
admin_account_pop_code_input2 = By.XPATH, '(//div[@class="split-input-container"]/input)[2]'
# 验证码输入框[3]
admin_account_pop_code_input3 = By.XPATH, '(//div[@class="split-input-container"]/input)[3]'
# 验证码输入框[4]
admin_account_pop_code_input4 = By.XPATH, '(//div[@class="split-input-container"]/input)[4]'
# 错误提示信息
admin_account_pop_get_err = By.XPATH, '//div[@class="split-input-error"]'
# 关闭弹窗
admin_account_pop_close = By.XPATH, '(//img)[1]'

# 修改邮箱-新邮箱输入框
admin_account_pop_new_email_input = By.XPATH, '//input[@placeholder="请输入新邮箱"]'

# 密码-修改按钮
admin_account_password_change = By.XPATH, '(//p[@class="name-right"])[4]/button'
# 修改密码-关闭弹窗
admin_account_pop_change_password_close = By.XPATH, '(//img)[2]'
# 退出登录按钮
admin_account_login_out_btn = By.XPATH, '//button[contains(text(),"退出登录")]'
# 退出按钮
admin_account_pop_out_btn = By.XPATH, '(//button[contains(text(),"退出")])[2]'

"""以下为 医生端-登陆页面 配置数据"""
# 系统log
doctor_login_log = By.XPATH, '//h3'
# 手机号输入框
doctor_login_phone_input = By.XPATH, '//input[@placeholder="请输入手机号"]'
# 密码输入框
doctor_login_password_input = By.XPATH, '//input[@placeholder="请输入密码"]'
# 登录按钮
doctor_login_btn = By.XPATH, '//button[contains(text(),"登录")]'
# 获取错误提示信息
doctor_login_err = By.XPATH, '//p[@class="login-error"]'
# 忘记密码按钮
doctor_login_porget_password_btn = By.XPATH, '//a[contains(text(),"忘记密码")]'
# 去激活账号按钮
doctor_activate_account_btn = By.XPATH, '//a[contains(text(),"去激活账号")]'
# 管理员登录按钮
doctor_login_admin_btn = By.XPATH, '//a[text()="管理员登录"]'

"""以下为 激活账号-①页面 配置数据"""
# 姓名输入框
doctor_activate_name = By.XPATH, '//input[@placeholder="请输入姓名"]'
# 身份证号输入框
doctor_activate_num = By.XPATH, '//input[@placeholder="请输入身份证号"]'
# 下一步按钮
doctor_activate_next_step = By.XPATH, '//button[contains(text(),"下一步")]'
# 获取账号提示信息
doctor_activate_get_account_err = By.XPATH, '(//p[contains(text(),"提示")]/following-sibling::p)'
# 返回登录页面按钮
doctor_activate_return_login = By.XPATH, '//span[contains(text(),"返回登录页面")]'

"""以下为 激活账号-②页面 配置数据"""
# 手机号输入框
doctor_activate_phone = By.XPATH, '//input[@placeholder="请输入常用手机号"]'
# 获取验证码按钮
doctor_activate_get_code_btn = By.XPATH, '//button[contains(text(),"获取验证码")]'
# 验证码输入框
doctor_activate_code_input = By.XPATH, '(//input[@class="border-input"])[1]'
# 获取验证码提示信息
doctor_account_get_code_err = By.XPATH, '//p[@style="clear: both;"]/following-sibling::p'


"""以下为 激活账号-③页面 配置数据"""
# 新密码输入框
doctor_activate_new_password_input = By.XPATH, '//input[@placeholder="输入新密码"]'
# 设定新密码按钮
doctor_activate_new_password_btn = By.XPATH, '//button[contains(text(),"设定新密码")]'

"""以下为 忘记密码-①页面 配置数据"""
# 手机号输入框
doctor_login_porget_password_phone_input = By.XPATH, ''
# 获取验证码按钮
doctor_login_porget_password_get_code_btn = By.XPATH, ''
# 验证码输入框
doctor_login_porget_password_code_input = By.XPATH, ''
# 返回登录按钮
doctor_login_porget_password_return_btn = By.XPATH, ''

"""以下为 忘记密码-①页面 配置数据"""
# 新密码输入框
doctor_login_porget_password_new_password_input = By.XPATH, ''
# 设定新密码按钮
doctor_login_porget_password_new_password_btn = By.XPATH, ''

"""以下为 医生端-儿童列表页面 配置数据"""
# 医生端-登录成功log
doctor_child_list_log = By.XPATH, '//h3[@class="welcomeTitle"]'


