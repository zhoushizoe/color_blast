# coding = utf-8
# Author: Zoe
# File: first_open_page.py
# Time: 2023/11/16 15:44
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from base.base_cb import BaseElement
from base.data_get import GetData


class FirstOpenPage(BaseElement):

    def __init__(self):
        self.GetData = GetData()

    def first_open_cb(self):
        """
        首次打开cb
        :return:
        """
        cb_package_name = self.GetData.get_data_2("color_blast_name")
        print(cb_package_name)
        self.clear_app(cb_package_name)


if __name__ == '__main__':
    if not cli_setup():
        auto_setup(__file__, logdir=True,
                   devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
        FirstOpenPage().first_open_cb()
