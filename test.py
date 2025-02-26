from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ✅ 指定 ChromeDriver 路径（必须匹配你的 Chrome 版本）
CHROMEDRIVER_PATH = "./chromedriver.exe"  # Windows 用户
# CHROMEDRIVER_PATH = "./chromedriver"  # Mac/Linux 用户

# ✅ 配置 Chrome 选项，防止反爬 & 闪退
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速
chrome_options.add_argument("--no-sandbox")  # 适用于 Linux 服务器
chrome_options.add_argument("--disable-dev-shm-usage")  # 适用于 Linux 服务器
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 防止反爬
chrome_options.add_argument("--headless")  # 无头模式（如果需要可取消）

# ✅ 启动 Selenium，手动加载 ChromeDriver
driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=chrome_options)

# ✅ 打开大众点评
url = "https://www.dianping.com/shanghai/ch10/g110"
driver.get(url)
print("✅ 成功打开大众点评！")

# ✅ 休眠 5 秒，确保页面加载完毕
time.sleep(5)

# ✅ 关闭浏览器
driver.quit()
