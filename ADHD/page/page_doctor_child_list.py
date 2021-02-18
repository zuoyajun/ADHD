import page
from base.base import Base


class PageDoctorChildList(Base):
    # 获取系统log
    def page_doctor_child_list_get_log(self):
        return self.base_get_text(page.doctor_child_list_log)
