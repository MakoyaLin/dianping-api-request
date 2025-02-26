import pandas as pd
import os

# ✅ 1. 读取数据文件（确保路径正确）
file_path = r"C:\Users\pc\Desktop\filtered_data.xlsx"

# ✅ 2. 判断文件类型并读取
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path, encoding="utf-8")  # 读取 CSV
elif file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path, engine="openpyxl")  # 读取 Excel
else:
    raise ValueError("❌ 仅支持 CSV 或 Excel 文件，请检查文件格式！")

# ✅ 3. 确保“行政区”列存在
if "行政区" not in df.columns:
    print("❌ 未找到“行政区”列，请检查数据！")
    exit()

# ✅ 4. 按“行政区”分组
grouped = df.groupby("行政区")

# ✅ 5. 设置最终的 Excel 输出路径
output_path = r"C:\Users\pc\Desktop\filtered_by_district.xlsx"

# ✅ 6. 如果文件已存在，先删除旧文件
if os.path.exists(output_path):
    os.remove(output_path)

# ✅ 7. 将数据拆分存入不同 Sheet
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    for district, data in grouped:
        data.to_excel(writer, sheet_name=str(district), index=False)  # 确保 sheet_name 是字符串

print(f"✅ 数据拆分完成，已保存至 {output_path}")
