# coding = utf-8
# Author: Zoe
# File: data_get.py
# Time: 2023/11/16 16:44
import yaml
from base.base_cb import BaseElement
from airtest.cli.parser import cli_setup
from airtest.core.api import *

# if not cli_setup():
#     auto_setup(__file__, logdir=True,
#                devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
#

class GetData(BaseElement):
    file_path = '/Users/周喜萍/git_project/color_blast/base/cb_data.yaml'

    def open_file(self):
        """
        打开配置文件
        :return:
        """
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data

    def get_data(self, key1, key2):
        """
        嵌套两层key值，取value
        :param key1:外层key值
        :param key2:内层key值
        :return: value值
        """
        value = self.open_file()[key1][key2]
        return value

    def get_data_2(self, key):
        """
        嵌套一层key值，取value
        :param key:外层key值
        :return: value值"""
        value = self.open_file()[key]
        # print(value)
        return value


# GetData().get_data_2("color_blast_name")
