from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.ios import iosPoco
from base.base_cb import BaseElement

# 暂时关闭截图
ST.SAVE_IMAGE = False
# 设置全局的截图精度为90
ST.SNAPSHOT_QUALITY = 90

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
        "ios:///http://127.0.0.1:8300", ])


# install(r"/Users/amber/Downloads/ColorBlast113.ipa")

class TestDailyLanguage(BaseElement):
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])

    language = "越南语iphone"
    name = rf"{language}/{language}"

    def test_file_path(self,filename):
        path = f"/Users/amber/PycharmProjects/color_blast/case/log/{filename}"
        if os.path.exists(path):
            return self
        else:
            os.makedirs(path)
        return self

    def test_open_app(self):
        package_path = r"/Users/amber/Downloads/ColorBlast113.ipa"
        app_name = "Color Blast"
        package_name = "ios.color.blast.inner"
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

    def test_get_daily_challenge(self):
        filename = "首页截图"
        setting_button = Template(r"setting_button.png", record_pos=(0.414, -0.918), resolution=(1284, 2778))
        replay_button = Template(r"replay_button.png", record_pos=(-0.11, 0.428), resolution=(1284, 2778))
        touch([683, 1656])
        sleep(5)
        swipe([652, 2180], [648, 1607])
        sleep(2)
        swipe([639, 2194], [728, 1470])
        sleep(2)
        swipe([643, 2189], [1034, 2087])
        sleep(3)
        for i in range(10):
            sleep(1)
            touch(setting_button)
            sleep(1)
            touch(replay_button)
            sleep(1)
        touch(setting_button)
        sleep(1)
        touch([359, 1927])
        sleep(2)
        self.get_snapshot(filename, self.name)


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
        TestDailyLanguage().test_file_path().test_get_daily_challenge()
