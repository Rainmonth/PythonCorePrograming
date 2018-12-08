import pandas as pd

# 基本柱状图绘制
data_1 = pd.read_excel('./20180630空气质量指数.xlsx', sheet_name=0)  # 读取数据
data_1.head()
