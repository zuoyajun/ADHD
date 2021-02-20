from time import sleep
import page
from base.base import Base
from tool.get_logger import GetLogger

log = GetLogger.get_logger()


class PageAdminDoctorDetail(Base):

    # 获取医生详情-医生状态
    def page_admin_doctor_detail_get_status(self):
        return self.base_get_text(page.admin_doctor_detail_status)

    # 获取医生详情-医生姓名
    def page_admin_doctor_detail_get_name(self):
        get_doctor_detail_name = self.base_get_text(page.admin_doctor_detail_name)[:-3]
        log.info("获取的医生姓名为：{}".format(get_doctor_detail_name))
        return get_doctor_detail_name

    # 获取医生详情-医生性别
    def page_admin_doctor_detail_grt_sex(self):
        return self.base_get_text(page.admin_doctor_detail_sex)

    # 获取医生详情-医生身份证号
    def page_admin_doctor_detail_get_num(self):
        return self.base_get_text(page.admin_doctor_detail_num)

    # 获取医生详情-未激活-手机号
    def page_admin_doctor_detail_get_no_phone(self):
        return self.base_get_text(page.admin_doctor_detail_no_phone)

    # 获取医生详情-已激活-手机号
    def page_admin_doctor_detail_get_yes_phone(self):
        return self.base_get_text(page.admin_doctor_detail_yes_phone)

    # 获取医生详情-单位
    def page_admin_doctor_detail_get_unit(self):
        return self.base_get_text(page.admin_doctor_detail_unit)

    # 获取医生详情-创建时间
    def page_admin_doctor_detail_get_create_time(self):
        return self.base_get_text(page.admin_doctor_detail_create_time)

    # 获取医生详情-备注
    def page_admin_doctor_detail_get_remark(self):
        return self.base_get_text(page.admin_doctor_detail_remark)

    # 点击医生详情-姓名-修改按钮
    def page_admin_doctor_detail_name_change(self):
        self.base_click(page.admin_doctor_detail_name_change)

    # 点击医生详情-手机号-修改按钮
    def page_admin_doctor_detail_phone_change(self):
        self.base_click(page.admin_doctor_detail_phone_change)

    # 点击医生详情-备注-修改按钮
    def page_admin_doctor_detail_remark_change(self):
        self.base_click(page.admin_doctor_detail_remark_change)

    # 修改姓名弹窗-输入医生姓名
    def page_admin_doctor_detail_pop_name_input(self, change_name):
        self.base_send_input(page.admin_doctor_detail_pop_name_input, change_name)

    # 修改姓名弹窗-点击修改按钮
    def page_admin_doctor_detail_pop_name_change(self):
        self.base_click(page.admin_doctor_detail_pop_name_change)

    # 修改手机号弹窗-输入手机号
    def page_admin_doctor_detail_pop_phone_input(self, change_phone):
        self.base_input(page.admin_doctor_detail_pop_phone_input, change_phone)

    # 修改手机号弹窗-点击修改按钮
    def page_admin_doctor_detail_pop_phone_change(self):
        self.base_click(page.admin_doctor_detail_pop_phone_change)

    # 修改手机号弹窗-获取错误文本信息
    def page_admin_doctor_detail_pop_get_err(self):
        return self.base_get_text(page.admin_doctor_detail_pop_get_err)

    # 修改手机号-关闭弹窗
    def page_admin_doctor_detail_pop_phone_close(self):
        self.base_click(page.admin_doctor_detail_pop_phone_close)

    # 修改备注弹窗-输入备注
    def page_admin_doctor_detail_pop_remark_input(self, change_remark):
        self.base_send_input(page.admin_doctor_detail_pop_remark_input, change_remark)

    # 修改备注弹窗-点击修改按钮
    def page_admin_doctor_detail_pop_remark_change(self):
        self.base_click(page.admin_doctor_detail_pop_remark_change)

    # 获取冻结医生按钮文本
    def page_admin_doctor_detail_frozen_get_text(self):
        return self.base_get_text(page.admin_doctor_detail_frozen_btn)

    # 点击冻结医生按钮
    def page_admin_doctor_detail_frozen_click(self):
        self.base_click(page.admin_doctor_detail_frozen_btn)

    # 冻结医生窗口-点击冻结按钮
    def page_admin_doctor_detail_pop_frozen_click(self):
        self.base_click(page.admin_doctor_detail_pop_frozen_btn)

    # 获取冻结状态
    def page_admin_doctor_detail_frozen_status_get_text(self):
        return self.base_get_text(page.admin_doctor_detail_frozen_status)

    # 点击解除冻结按钮
    def page_admin_doctor_detail_unfreeze_click(self):
        self.base_click(page.admin_doctor_detail_unfreeze_btn)

    # 解除冻结窗口-点击解冻按钮
    def page_admin_doctor_detail_pop_unfreeze_click(self):
        self.base_click(page.admin_doctor_detail_pop_unfreeze_btn)

    # 组合方法—修改姓名
    def page_admin_doctor_detail_change_name(self, change_name):
        self.page_admin_doctor_detail_name_change()
        sleep(1)
        self.page_admin_doctor_detail_pop_name_input(change_name)
        sleep(1)
        self.page_admin_doctor_detail_pop_name_change()
        sleep(1)

    # 组合方法—修改手机号
    def page_admin_doctor_detail_change_phone(self, change_phone):
        self.page_admin_doctor_detail_phone_change()
        sleep(1)
        self.page_admin_doctor_detail_pop_phone_input(change_phone)
        sleep(1)
        self.page_admin_doctor_detail_pop_phone_change()
        sleep(1)

    # 组合方法—修改备注
    def page_admin_doctor_detail_change_remark(self, change_remark):
        self.page_admin_doctor_detail_remark_change()
        sleep(1)
        self.page_admin_doctor_detail_pop_remark_input(change_remark)
        sleep(1)
        self.page_admin_doctor_detail_pop_remark_change()
        sleep(1)
