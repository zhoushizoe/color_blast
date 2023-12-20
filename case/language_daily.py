from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.ios import iosPoco
from base.base_cb import BaseElement

# 暂时关闭截图
ST.SAVE_IMAGE = False
# 设置全局的截图精度为90
ST.SNAPSHOT_QUALITY = 90


class DailyLanguage(BaseElement):
    # if not cli_setup():
    #     auto_setup(__file__, logdir=True, devices=[
    #         "ios:///http://127.0.0.1:8300", ])
    setting_button = Template(r"setting_button.png", record_pos=(0.414, -0.918), resolution=(1284, 2778))
    replay_button = Template(r"replay_button.png", record_pos=(-0.11, 0.428), resolution=(1284, 2778))

    language = "西班牙语"
    name = rf"{language}/{language}"

    def file_path(self):
        path = f"/Users/amber/PycharmProjects/color_blast/case/log/{self.name}"
        if os.path.exists(path):
            return self
        else:
            os.makedirs(path)
        return self

    def open_app(self):
        package_path = r"/Users/amber/Downloads/ColorBlast113.ipa"
        app_name = "Color Blast"
        package_name = "ios.color.blast.inner"
        self.file_path()
        uninstall(package_name)
        sleep(3)
        install(package_path)
        poco = iosPoco()
        poco(app_name).click()
        sleep(3)
        touch([652, 1723])
        sleep(1)
        touch([399, 1567])
        sleep(1)
        touch([643, 1576])
        sleep(5)

    def get_daily_challenge(self):
        filename = "未解锁每日挑战的首页截图"
        self.open_app()
        setting_button = Template(r"setting_button.png", record_pos=(0.414, -0.918), resolution=(1284, 2778))
        replay_button = Template(r"replay_button.png", record_pos=(-0.11, 0.428), resolution=(1284, 2778))
        touch([683, 1656])
        sleep(6)
        swipe([652, 2180], [648, 1607])
        sleep(2)
        swipe([639, 2194], [710, 1399])
        sleep(2)
        swipe([643, 2189], [1034, 2087])
        sleep(20)
        for i in range(7):
            sleep(1)
            touch(setting_button)
            sleep(1)
            touch(replay_button)
            sleep(3)
        touch(setting_button)
        sleep(1)
        touch([359, 1927])
        sleep(2)
        self.get_snapshot(filename, self.name)
        return self

    def get_unlock_daily(self):
        filename = "已经解锁的每日挑战游戏首页"
        self.get_daily_challenge()
        self.sleep_time()
        self.image_click([710, 2300])
        for i in range(4):
            sleep(1)
            touch(self.setting_button)
            sleep(1)
            touch(self.replay_button)
            sleep(3)
        touch(self.setting_button)
        sleep(1)
        touch([359, 1927])
        sleep(2)
        self.get_snapshot(filename, self.name)
        return self

    def daliy_calendar(self):
        self.get_unlock_daily()
        filename1 = "日历页面"
        filename2 = "挑战页面"
        filename3 = "clear模式开局"
        filename4 = "clear模式游戏页面"
        self.sleep_time()
        self.image_click([954, 1696])
        self.sleep_time()
        self.get_snapshot(filename1, self.name)
        self.image_click([630, 2367])
        self.get_snapshot(filename2, self.name)
        self.image_click([932, 1088])
        self.sleep_time(0.5)
        self.get_snapshot(filename3, self.name)
        self.sleep_time()
        self.get_snapshot(filename4, self.name)
        self.sleep_time(10)
        return self

    def clear_fail(self):
        self.daliy_calendar()
        filename1 = "失败横幅"
        filename2 = "clear模式失败弹窗"
        self.image_click([914, 284])
        self.sleep_time(0.5)
        self.get_snapshot(filename1, self.name)
        self.sleep_time()
        self.get_snapshot(filename2, self.name)

    def clear_win(self):
        self.clear_fail()
        filename = "clear模式胜利弹窗"
        filename2 = "you win 横幅"
        # self.clear_fail()
        self.image_click([728, 1669])
        self.sleep_time()
        for i in range(2):
            self.image_click([1050, 266])
            self.sleep_time(4)
        self.image_click([1050, 266])
        self.sleep_time(1)
        self.get_snapshot(filename2, self.name)
        self.sleep_time()
        self.get_snapshot(filename, self.name)
        return self

    def collect_fail(self):
        self.clear_win()
        self.sleep_time()
        filename1 = "收藏模式失败横幅"
        filename2 = "收藏模式失败弹窗"
        filename3 = "收藏模式开局横幅"
        self.image_click([705, 1707])
        self.sleep_time(0.5)
        self.get_snapshot(filename3, self.name)
        self.sleep_time()
        self.image_click([917, 288])
        self.sleep_time(1)
        self.get_snapshot(filename1, self.name)
        self.sleep_time()
        self.get_snapshot(filename2, self.name)

    def collect_win(self):
        self.collect_fail()
        filename = "collect模式胜利弹窗"
        filename2 = "恭喜弹窗"
        self.image_click([789, 1680])
        self.sleep_time()
        for i in range(2):
            self.image_click([1050, 266])
            self.sleep_time(4)
        self.image_click([1179, 208])
        self.sleep_time()
        self.image_click([390, 1933])
        self.sleep_time()
        self.get_snapshot(filename2, self.name)
        self.image_click([625, 1711])
        self.sleep_time(4)
        self.image_click([687, 2385])
        self.sleep_time(4)
        self.image_click([926, 1352])
        self.sleep_time(4)
        self.image_click([1050, 266])
        self.sleep_time(1)
        self.sleep_time(4)
        self.get_snapshot(filename, self.name)
        return self

    def score_fail(self):
        self.collect_win()
        filename = "分数页面横幅"
        filename2 = "分数页面失败弹窗"
        self.image_click([762, 1707])
        self.sleep_time(0.5)
        self.get_snapshot(filename, self.name)
        self.sleep_time()
        self.image_click([900, 292])
        self.sleep_time()
        self.get_snapshot(filename2, self.name)
        return self

    def score_win(self):
        self.score_fail()
        filename = "分数模式胜利页面"
        filename2 = "完成当日挑战日历页面"
        self.image_click([798, 1662])
        self.sleep_time(4)
        self.image_click([1073, 283])
        self.sleep_time(4)
        self.get_snapshot(filename, self.name)
        self.sleep_time()
        self.image_click([656, 1720])
        self.sleep_time(3)
        self.image_click([465, 1902])
        self.sleep_time()
        self.get_snapshot(filename2, self.name)
        return self

    def collect_page(self):
        self.score_win()
        filename = "收藏页面"
        self.image_click([1175, 203])
        self.image_click([199, 288])
        self.get_snapshot(filename, self.name)
        self.sleep_time()
        self.image_click([93, 203])
        return self

    def month(self):
        self.collect_page()
        self.image_click([128, 203])
        self.sleep_time()
        self.image_click([39, 186])

    def get_month(self, filename1, filename2):
        self.image_click([620, 292], times=30)
        self.get_snapshot(filename1, self.name)
        self.image_click([935, 1636])
        self.sleep_time(2)
        self.get_snapshot(filename2, self.name)
        self.image_click([88, 199])
        self.sleep_time()
        return self

    def get_month_plue(self):
        filename1 = "一月份"
        filename11 = "一月份1"
        filename2 = "二月份"
        filename21= "二月份1"
        filename3 = "三月份"
        filename31 = "三月份1"
        filename4 = "四月份"
        filename41 = "四月份1"
        filename5 = "五月份"
        filename51 = "五月份1"
        filename6 = "六月份"
        filename61 = "六月份1"
        filename7 = "七月份"
        filename77 = "七月份1"
        filename8 = "八月份"
        filename88 = "八月份1"
        filename9 = "九月份"
        filename99 = "九月份1"
        filename10 = "十月份"
        filename100 = "十月份1"
        filename111 = "十一月份"
        filename1111 = "十一月份1"
        self.month()
        self.get_month(filename1, filename11)
        self.get_month(filename2, filename21)
        self.get_month(filename3, filename31)
        self.get_month(filename4, filename41)
        self.get_month(filename5, filename51)
        self.get_month(filename6, filename61)
        self.get_month(filename7, filename77)
        self.get_month(filename8, filename88)
        self.get_month(filename9, filename99)
        self.get_month(filename10, filename100)
        self.get_month(filename111, filename1111)


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
        DailyLanguage().get_month_plue()
