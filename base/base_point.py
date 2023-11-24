# coding = utf-8
# Author: Zoe
# File: base_point.py
# Time: 2023/11/17 11:49
import re
import subprocess
from airtest.core.api import *
import yaml


class GetPoint:
    """
    前置条件
    1.清除数据
    2.进行操作（操作的步骤放在框架外）
    3.过滤埋点，进行对比（能过滤到证明有埋点，需要断言，断言的标准就是是否过滤到了埋点）
    4.放入数据库（暂时为txt文档）
    5.一些操作之后对埋点进行对比


    """
    def clear_command(self):
        """
        1.清除数据
        :return:
        """
        clear = "adb logcat -c"
        subprocess.call(clear, shell=True)
        print("清除日志已完成")
        return self

    def read_point(self, key):
        """
        3.过滤埋点，进行对比
        :return:
        """
        with open("standard_point.yaml", "r", encoding="utf-8") as f:
            all_data = yaml.safe_load(f)
            get_data = all_data[key]
            print(get_data)
            return get_data

    def output_command(self, key):
        sleep(10)
        """
        进行对比
        """
        grep_info = self.read_point(key)
        command = f"adb logcat -d | grep '{grep_info}'"
        grep_output = subprocess.check_output(command, shell=True)
        grep_output = grep_output.decode()
        grep_output = grep_output.strip()
        print(grep_output)
        return grep_output

    def get_correct_log(self, key):
        raw_string = self.output_command(key)
        pattern = r'EVENT_SEND\s+:\s+(.*?)\s*lib_net_status:'
        # 使用正则表达式提取目标部分
        match = re.search(pattern, raw_string)
        if match:
            extracted_content = match.group(1)
            print(extracted_content)
            extracted_string = extracted_content.strip()
            return extracted_string
        else:
            print("没找到对应log")

    def write_contrast(self, key):
        with open("contrast.yaml", "a", encoding="utf-8") as f:
            yaml.dump(self.get_correct_log(key), f)

    def write_contrast2(self, key):
        with open("test.txt", "a", encoding="utf-8") as f:
            f.write(self.get_correct_log(key) + "\n")
        return self

    def contrast_step(self, key):
        """
        点击操作之后的步骤
        :return:
        """
        self.read_point(key)
        self.output_command(key)
        self.get_correct_log(key)
        self.write_contrast2(key)


if __name__ == "__main__":
    GetPoint().clear_command().contrast_step("game_new_start")
