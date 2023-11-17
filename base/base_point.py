# coding = utf-8
# Author: Zoe
# File: base_point.py
# Time: 2023/11/17 11:49
import re
import subprocess


class GetPoint:
    def get_point(self):
        # 需要过滤的日志
        grep_info = "A_ANALYSIS : FIREBASE     : EVENT_SEND       :"
        command = f"adb logcat -d | grep '{grep_info}'"
        grep_output = subprocess.check_output(command, shell=True)
        # subprocess.call(clear, shell=True)
        grep_output = grep_output.decode()
        print(grep_output)
        point_list = grep_output.split("\n")
        # point 是原始信息，需要按行分割，放到一个list里
        event_list = []
        # 遍历这个list 用正则提取 ':' 和 '=>' 之间的字符串
        pattern = r"(?<=:)([^:=>]+)(?= =>)"
        for text in point_list:
            result = re.search(pattern, text)
            if result:
                event_list.append(result.group().strip())
            print(event_list)
