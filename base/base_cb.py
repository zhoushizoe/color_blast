# coding = utf-8
# Author: Zoe
# File: base_ws.py
# Time: 2023/10/16 11:14 上午
"""
如果要使用poco进行点击操作的话，需要调用放在之后

"""
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.ios import iosPoco


class BaseElement:

    def clear_app(self, package):
        """
        清除应用数据（仅安卓）
        :param package:
        :return:
        """
        clear_app(package)
        return self

    def uninstall_ios(self, package):
        """
        卸载应用，安卓与ios通用
        :param package:
        :return:
        """
        uninstall(package)
        sleep(4)
        return self

    def uninstall(self, package):
        """
        卸载应用，安卓与ios通用
        :param package:
        :return:
        """
        uninstall(package)
        self.sleep_time()
        return self

    def install_ios(self, package):
        install(package)
        self.sleep_time()
        return self

    def install(self, package):
        """
        安装应用（安卓与iOS通用）
        :param package:
        :return:
        """
        install(package)
        self.sleep_time()
        return self

    def image_click(self, image, times=1):
        """
        使用图片或者绝对坐标进行点击（iOS与安卓通用）
        :param image:
        :param times:
        :return:
        """
        touch(image, times)
        return self

        # 使用图像识别拖动

    def image_swipe(self, place, to):
        """
        使用图片或者坐标进行滑动（iOS与安卓通用）
        :param place:
        :param to:
        :return:
        """
        swipe(place, to)
        return self

    def stop_app(self, package):
        """
        杀掉应用进程（iOS与安卓通用）
        :param package:
        :return:
        """
        stop_app(package)
        sleep(2)
        return self

    def start_app(self, package):
        """
        打开应用（目前iOS17不支持）
        :param package:
        :return:
        """
        start_app(package)
        sleep(5)
        return self

    # 删除输入的文字
    def delete_word(self):
        """
        删除文字（安卓独有）
        :return:
        """
        keyevent("KEYCODE_DEL")
        sleep(0.5)
        return self

    # 输入所需要的文字
    def input_word(self, word):
        """
        输入文字（安卓独有）
        :param word:
        :return:
        """
        text(word)
        self.sleep_time(1)
        return self

    def get_snapshot(self, filename, language):
        """
        截图，多语言的时候需要文件名和语言（安卓 iOS通用）
        :param filename:截图的内容
        :param language:语言
        :return:
        """
        snapshot(filename=language + filename + ".png")
        return self

    def snapshot_log(self, filename):
        """
        仅仅需要截图log时候的截图（（安卓iOS通用））
        :param filename:
        :return:
        """
        snapshot(filename=filename + ".png")
        return self

    def sleep_time(self, second=2):
        """
        睡眠时间，默认是两秒
        :param second:
        :return:
        """
        sleep(second)
        return self

    # 进行图片点击操作时同时使用坐标点击
    def image_click_plus(self, image, coordinate):
        """
        防止图片找不到，做一个判断语句，如果有图片就点击图片，否则用坐标点击
        :param image:图片
        :param coordinate:坐标
        :return:
        """
        if exists(image):
            self.image_click(image)
        else:
            self.image_click(coordinate)
        return self

    def system_keyevent(self, para):
        """
        封装的一些键盘操作，部分iOS可用
        :param para: back：返回键；HOME：回到手机首页；
        :return:
        """
        keyevent(para)
        return self

    def image_click_coord(self, picture, coord):
        """
        判断是否存在某一个图片，如果存在，点击对应的坐标
        :return:
        """
        if exists(picture):
            self.image_click(coord)
        return self


class IosBaseElement:
    """
    封装关于iOS特殊的一些操作
    """

    def ios_delete_text(self):
        """
        ios中删除输入的字符
        :return:
        """
        text("\b", enter=False)
        return self

    def ios_inter_word(self, word,enter=False):
        """
          iOS的text()接口默认会在给定的输入字符后面加一个换行符 \n 。
          如果不想要输入之后出现换行的效果，可以把enter = False传到text()接口里面
        :return: 
        """""

        text(word, enter)
        return self

    def goback_home(self):
        """
        将应用回到后台，回到手机主页
        :return:
        """
        keyevent("HOME")
        return self

    def ios_open_app(self, app_name):
        """
        airtest中的[start_app]不支持iOS17
        游戏的名称永远是英文的，所以使用poco的方式打开应用
        :param app_name:app在首页显示的应用名字
        :return:
        """
        poco = iosPoco()
        poco(app_name).click()
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
    poco = iosPoco()
    IosBaseElement().ios_open_app("Water Sort")
