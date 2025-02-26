import pandas as pd
import os

# ✅ 1. 读取数据
file_path = r"C:\Users\pc\Documents\WeChat Files\RioLzzy\FileStorage\File\2025-02\上海.csv"

# ✅ 2. 判断文件类型并读取
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path, encoding="utf-8")  # 读取 CSV
elif file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path, engine="openpyxl")  # 读取 Excel
else:
    raise ValueError("❌ 仅支持 CSV 或 Excel 文件，请检查文件格式！")

# ✅ 3. 修改 `create_time` 列的值
if "create_time" in df.columns:
    df["create_time"] = "2025-2-25 23:52"
    print("✅ 已将 create_time 全部修改为 2025-2-25 23:52")
else:
    print("⚠️ 警告：未找到 create_time 列，未做修改！")

# ✅ 4. 过滤条件：
#  - 人均消费 ≥ 100
#  - 营业状态 ≠ "暂停营业"
if "营业状态" in df.columns:
    df_filtered = df[(df["平均消费"] >= 100) & (df["营业状态"] != "暂停营业")]
else:
    df_filtered = df[df["平均消费"] >= 100]
    print("⚠️ 没有找到“营业状态”列，仅按照‘人均消费 ≥ 100’过滤！")

# ✅ 5. 删除已存在的 `filtered_data.xlsx`
filtered_file_path = r"C:\Users\pc\Desktop\filtered_data.xlsx"
if os.path.exists(filtered_file_path):
    os.remove(filtered_file_path)

# ✅ 6. 保存清理后的数据
df_filtered.to_excel(filtered_file_path, index=False, engine="openpyxl")

print(f"✅ 数据清洗完成，已保存至 {filtered_file_path}")
