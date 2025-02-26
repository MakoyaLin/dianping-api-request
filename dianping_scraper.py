from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import json
import pandas as pd
import os
import random

# ✅ 1. 手动指定 ChromeDriver 路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMEDRIVER_PATH = os.path.join(BASE_DIR, "chromedriver.exe")

# ✅ 2. 配置 Selenium 选项
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--headless")  # 无头模式（不打开窗口）

# ✅ 3. 启动 Selenium
driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=chrome_options)

# ✅ 4. 访问大众点评上海餐饮页面
url = "https://www.dianping.com/shanghai/ch10/g110"
driver.get(url)

# ✅ 5. 反反爬 - 让 Selenium 更像真实浏览器
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# ✅ 6. 等待页面加载
time.sleep(random.uniform(5, 10))

# ✅ 7. 滚动页面，确保所有店铺加载出来
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # 给数据加载的时间

# ✅ 8. 等待店铺列表出现
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".shop-list .shop-item"))
    )
except Exception as e:
    print("⚠️ 页面加载超时，可能被反爬！")

# ✅ 9. 查找店铺列表
shops = driver.find_elements(By.CSS_SELECTOR, ".shop-list .shop-item")

# ✅ 10. 爬取店铺数据
results = []
for shop in shops:
    try:
        name = shop.find_element(By.CSS_SELECTOR, ".shopname").text.strip()
        address = shop.find_element(By.CSS_SELECTOR, ".address").text.strip()
        price_element = shop.find_element(By.CSS_SELECTOR, ".price")
        price_text = price_element.text.strip().replace("￥", "") if price_element else "0"
        price_value = int(price_text) if price_text.isdigit() else 0

        # 只保存人均消费 >= 100 元的店铺
        if price_value >= 100:
            results.append({"name": name, "address": address, "price": price_value})
            print(f"{name} - {address} - 人均消费: {price_value} 元")

    except Exception as e:
        print("⚠️ 跳过无效数据:", e)

# ✅ 11. 关闭浏览器
driver.quit()

# ✅ 12. 保存数据到 CSV 文件
csv_filename = "dianping_shops.csv"
if results:
    with open(csv_filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["店铺名称", "地址", "人均消费"])
        for shop in results:
            writer.writerow([shop["name"], shop["address"], shop["price"]])
    print(f"✅ 数据已成功写入 {csv_filename}")
else:
    print("⚠️ 没有爬到符合条件的数据，CSV 为空！")

# ✅ 13. 保存数据到 JSON 文件
json_filename = "dianping_shops.json"
with open(json_filename, mode="w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=4)

# ✅ 14. 保存数据到 Excel 文件
excel_filename = "dianping_shops.xlsx"
df = pd.DataFrame(results)
df.to_excel(excel_filename, index=False, engine="openpyxl")

print(f"\n✅ 爬取完成！数据已保存到：")
print(f"📂 {csv_filename}  (Excel 可打开)")
print(f"📂 {json_filename}  (JSON 格式)")
print(f"📂 {excel_filename}  (Excel 文件)")
