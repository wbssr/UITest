# UITest - SauceDemo 电商网站 UI 自动化测试

## 项目介绍
基于 Python + Selenium + Pytest 的 UI 自动化测试框架，采用 POM（Page Object Model）设计模式，覆盖 SauceDemo 电商网站的核心业务流程。

## 技术栈
- Python 3.12
- Selenium + Pytest
- POM 设计模式
- HTML 测试报告
- 失败自动截图

## 项目结构
- `base/`：基础页面类（BasePage，封装等待、点击、输入、截图）
- `page/`：页面对象（LoginPage、ProductPage、CartPage、CheckoutPage、OrderPage）
- `test_saucedemo.py`：测试用例（正常流程 + 异常场景 + 参数化）

## 核心功能
- 登录 → 添加商品 → 购物车 → 结算 → 下单 完整流程
- 多用户参数化测试（standard_user、performance_glitch_user）
- 异常场景测试（错误密码登录验证）
- 失败自动截图

## 前置条件

### ChromeDriver 配置
因网络限制，本项目使用**手动下载的 ChromeDriver**，请按以下步骤配置：

1. 查看本地 Chrome 版本：浏览器访问 `chrome://version/`
2. 从 [ChromeDriver 官网](https://chromedriver.chromium.org/) 下载对应版本
3. 将 `chromedriver.exe` 放在项目根目录
4. 修改 `test_saucedemo.py` 中的驱动路径（如需要）

## 运行方式

```bash
# 安装依赖
pip install selenium pytest pytest-html

# 运行测试
pytest test_saucedemo.py --html=report.html
