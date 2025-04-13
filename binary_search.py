import streamlit as st


class BinarySearch:
    def __init__(self):
        self.start = 0
        self.end = 100
        self.target = 1

    def input_your_target(self):
        """
        输入你期望查找的数字
        """
        target = st.slider("请选择一个数字", self.start, self.end, self.target)
        if target:
            self.target = int(target)

    def input_the_range(self):
        """
        输入二分查找数字的范围
        """
        start_number = st.number_input("起始值", value=None, placeholder="0")
        end_number = st.number_input("终点值", value=None, placeholder="100")
        if start_number:
            self.start = int(start_number)
        if end_number:
            self.end = int(end_number)

    def show_process(self):
        """
        输出二分查找过程
        """
        search_list = range(self.start, self.end + 1)
        start_search = st.button("开始查找")
        bingo = False
        search_qty = 0
        if start_search:
            if self.target > self.end or self.target < self.start:
                st.write(f'目标值不在查找范围内， 请更换目标值')
                return
            while not bingo:
                search_qty += 1
                check_index = len(search_list) // 2
                check_item = search_list[check_index]
                msg = f'第 {search_qty} 次查找， 此次校验: {check_item}, 目标值为：{self.target}; '
                if check_item == self.target:
                    bingo = True
                    msg += f'目标已找到, 共查找：{search_qty} 次，查找结束'
                if check_item > self.target:
                    search_list = search_list[:check_index]
                    msg += f'数据较大， 继续查找, 查找列表为: {search_list}'
                if check_item < self.target:
                    search_list = search_list[check_index:]
                    msg += f'数据较小， 继续查找, 查找列表为: {search_list}'

                st.write(msg)

    def frontpage(self):
        self.input_the_range()
        self.input_your_target()
        self.show_process()
