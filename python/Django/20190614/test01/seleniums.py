from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless') #增加无界面选项
chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题

# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options=chrome_options)
mainUrl = "https://zz.58.com/zufang/38418522983076x.shtml?entinfo=38418522983076_0&shangquan=kaiyuanl&fzbref=0&params=rankbusitimeZZ8pc0020^desc&psid=147326990204579572495551711&cookie=market|u-2d2yxv86y3v43nkddh1.BDPCPZ_BT|https://sp0.baidu.com/9q9JcDHa2gU2pMbgoY3K/adrc.php?t=06KL00c00fD4F9Y0aXP60nW_R0Kin69I0000003sFNC00000JsWF23.THYdrnv__tT0UWdBmy-bIfK15ycYPWm1nAF-nj0sPHRYPWD0IHY1fb7jwb7An19KwWc1PH9An1PAPHKDwjc1nW64P1F7PsK95gTqFhdWpyfqn1c1rjRvPHb4nzusThqbpyfqnHm0uHdCIZwsT1CEQvGdUgK_Iy49QWR3QhPEUiqGQ1FbnM-3IW63PHPvPjP8pvwkryT0mLFW5Hn3P161&tpl=tpl_11534_19968_16032&l=1512386574&attach=location%3D%26linkName%3D%25E6%25A0%2587%25E5%2587%2586%25E5%25A4%25B4%25E9%2583%25A8-%25E6%25A0%2587%25E9%25A2%2598-%25E4%25B8%25BB%25E6%25A0%2587%25E9%25A2%2598%26linkText%3D58%25E5%2590%258C%25E5%259F%258E-%25E6%2589%25BE%25E5%25B7%25A5%25E4%25BD%259C%252C%25E6%2589%25BE%25E6%2588%25BF%25E5%25AD%2590%252C%25E4%25B9%25B0%25E5%258D%2596%25E4%25BA%258C%25E6%2589%258B%25E8%25BD%25A6%252C%25E5%259B%25BD%25E6%25B0%2591%25E7%2594%259F%25E6%25B4%25BB%25E6%259C%258D%25E5%258A%25A1%25E5%25B9%25B3%25E5%258F%25B0%25EF%25BC%2581%26xp%3Did(%2522m3238565993_canvas%2522)%252FDIV%255B1%255D%252FDIV%255B1%255D%252FDIV%255B1%255D%252FDIV%255B1%255D%252FDIV%255B1%255D%252FH2%255B1%255D%252FA%255B1%255D%26linkType%3D%26checksum%3D107&ie=utf-8&f=8&tn=baidu&wd=58%E5%90%8C%E5%9F%8E&rqlang=cn&inputT=2600|c5/nn1w1cWMzITefSyXPAg==&apptype=0&key=&pubid=77210272&trackkey=38418522983076_ede04a2e-8a5e-4eb4-85a6-90a08844d9af_20190618083756_1560818276025&fcinfotype=gz"
browser.get(mainUrl)
print(browser.page_source)
browser.quit()