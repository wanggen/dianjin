import baostock as bs
import pandas as pd

bs.login()


# 定义要测试的频率
frequencies = ["5", "15", "30", "60", "d", "w", "m"]
code = "sh.000001"

for freq in frequencies:
    print(f"正在尝试频率: {freq} ...")

    # 统一使用一个安全的历史日期范围（2023年11月）
    rs = bs.query_history_k_data_plus(
        code,
        "date,time,code,open,high,low,close,volume,amount",
        start_date='2025-11-01',
        end_date='2025-11-03',
        frequency=freq,
        adjustflag="3"
    )

    data = []
    while (rs.error_code == '0') & rs.next():
        data.append(rs.get_row_data())

    print(f"结果: 频率 {freq} 获取到 {len(data)} 条数据")
    if len(data) > 0:
        df = pd.DataFrame(data, columns=rs.fields)
        # 打印第一行看看格式（分钟线有 time 列，日线 time 列为空）
        print(df.head(1))
    print("-" * 30)