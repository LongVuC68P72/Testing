from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


chromepath = 'D:\\Testing\\chromedriver.exe'
service = Service(chromepath)
options = Options()
options.add_experimental_option("detach", True)

# Tạo options để tạo thư mục chứa thông tin người dùng tránh capcha
options.add_argument('--user-data-dir=D:\\Testing\\profile')

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()


# Befor test
def Befor():
    url = "https://tiki.vn//"
    driver.get(url)
    # Sử dụng cho lần đầu đăng nhập
    '''phone_number = "0365364878"
    password = ""
    driver.find_element(By.XPATH, " //span[contains(text(),'Tài khoản')]").click()
    sleep(2)
    driver.find_element(By.NAME, "tel").send_keys(phone_number)
    sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Tiếp Tục')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//body/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys(password)
    sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Đăng Nhập')]").click()'''


# Test
def TC_01():
    driver.get("https://tiki.vn/mo-hinh-doremon-sieu-de-thuong-p138111503.html?spid=138111510")
    sleep(5)

    # Thêm 5 sản phẩm bằng nút cộng
    add_click_count = 15
    add = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/main[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/button[2]")
    for i in range(add_click_count):
        add.click()
        sleep(1)
    # Bỏ bớt 15 sản phẩm bằng nút trừ
    less_click_count = 14
    less = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/button[1]")
    for i in range(less_click_count):
        less.click()
        sleep(1)
    # Thêm vào giỏ
    driver.find_element(By.XPATH, "//button[contains(text(),'Chọn mua')]").click()

    # Xem giỏ
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[2]/div[4]/a[1]/div[1]/div[1]").click()

def TC_02():
    # Sản phẩm A
    driver.get("https://tiki.vn/ao-so-mi-nam-tay-ngan-hoa-tiet-chim-khatoco-a1mn438t2-thmk027-2010-n-xanh-den-p54762383.html?itm_campaign=tiki-reco_UNK_DT_UNK_UNK_tiki-listing_UNK_p-category-mpid-listing-v1_202305210600_MD_batched_PID.54762395&itm_medium=CPC&itm_source=tiki-reco&spid=54762395")
    sleep(3)
    # Thêm 1 sản phẩm A bằng cách điền
    sp1_count = 1
    driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[6]/div[1]/div[1]/div[1]/input[1]").clear()
    driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[6]/div[1]/div[1]/div[1]/input[1]").send_keys(sp1_count)
    driver.find_element(By.XPATH, "//button[contains(text(),'Chọn mua')]").click()
    sleep(2)

    # Sản phẩm B
    driver.get("https://tiki.vn/quan-kaki-nam-chat-vai-suong-mem-min-chong-nhan-co-gian-chuan-phong-cach-thoi-trang-dokafashion-dkfqkk01-p220670591.html?itm_campaign=tiki-reco_UNK_DT_UNK_UNK_tiki-listing_UNK_p-category-mpid-listing-v1_202305210600_MD_batched_PID.220670609&itm_medium=CPC&itm_source=tiki-reco&spid=220670609")
    sleep(3)
    # Thêm 1 sản phẩm B bằng cách điền
    sp2_count = 1
    driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[6]/div[1]/div[1]/div[1]/input[1]").clear()
    sleep(2)
    driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[6]/div[1]/div[1]/div[1]/input[1]").send_keys(sp2_count)
    driver.find_element(By.XPATH, "//button[contains(text(),'Chọn mua')]").click()
    sleep(2)

    # Sản phẩm C
    driver.get("https://tiki.vn/ao-khoac-nam-ao-khoac-kaki-nam-don-gian-cao-cap-kk34-p15993454.html?itm_campaign=tiki-reco_UNK_DT_UNK_UNK_tiki-listing_UNK_p-category-mpid-listing-v1_202305210600_MD_batched_PID.15993462&itm_medium=CPC&itm_source=tiki-reco&spid=15993462")
    sleep(3)
    # Thêm 1 sản phẩm C bằng cách điền
    sp3_count = 1
    driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/input[1]").clear()
    sleep(2)
    driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/input[1]").send_keys(sp3_count)
    driver.find_element(By.XPATH, "//button[contains(text(),'Chọn mua')]").click()
    sleep(2)

    # Xem giỏ
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[2]/div[4]/a[1]/div[1]/div[1]").click()

def TC_03():
    Befor()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[2]/div[4]/a[1]/div[1]/div[1]").click()
    sleep(3)
    # Chọn nút "Tất cả"
    driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
    sleep(1)
    # Chọn nút "Xóa mục đã chọn"
    driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[4]").click()
    driver.find_element(By.XPATH,"//div[contains(text(),'Xác nhận')]").click()

def TC_04():
    Befor()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[2]/div[4]/a[1]/div[1]/div[1]").click()
    sleep(2)

    count = 2 # thực hiện bước 3,4:  2 lần

    # Sản phẩm A
    for i in range(count):
        # Bớt số lượng sản phẩm A đi 1 nhưng vì số lượng sản phẩm A = 1 nên chọn hủy
        less_A = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]/img[1]")
        less_A.click()
        sleep(1)
        driver.find_element(By.XPATH, "//div[contains(text(),'Huỷ')]").click()
        sleep(2)
        # Tăng số lượng sản phẩm A lên 1
        add_A = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]/img[1]")
        add_A.click()

    # Sản phẩm B thực hiện tương tự
    for i in range(count):
        # Bớt số lượng sản phẩm B đi 1
        less_B = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]/img[1]")
        less_B.click()
        sleep(1)
        driver.find_element(By.XPATH, "//div[contains(text(),'Huỷ')]").click()
        sleep(2)
        # Tăng số lượng sản phẩm B lên 1
        add_B = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]/img[1]")
        add_B.click()

    # Sản phẩm C thực hiện tương tự
    for i in range(count):
        # Bớt số lượng sản phẩm C đi 1
        less_B = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]/img[1]")
        less_B.click()
        sleep(1)
        driver.find_element(By.XPATH, "//div[contains(text(),'Huỷ')]").click()
        sleep(2)
        # Tăng số lượng sản phẩm C lên 1
        add_B = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]/img[1]")
        add_B.click()

def TC_05():
    Befor()
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[2]/div[4]/a[1]/div[1]/div[1]").click()
    sleep(2)
    # A
    A = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/p[1]/span[1]")
    price_A = int((A.text).replace(" ₫", "").replace(".", ""))
    price_A_bh = int(((driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/p[1]/span[1]")).text).replace(" ₫", "").replace(".", ""))
    count_A = int(driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/input[1]").get_property("value"))

    # B
    B = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div/div/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div[2]/p/span")
    price_B = int((B.text).replace(" ₫", "").replace(".", ""))
    price_B_bh = int(((driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/p[1]/span[1]")).text).replace(" ₫", "").replace(".", ""))
    count_B = int(driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/input[1]").get_property("value"))

    # C
    C = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/p[1]/span[1]")
    price_C = int((C.text).replace(" ₫", "").replace(".", ""))
    price_C_bh = int(((driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/p[1]/span[1]")).text).replace(" ₫", "").replace(".", ""))
    count_C = int(driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/input[1]").get_property("value"))

    # Tổng giá
    total = price_A * count_A + price_A_bh * count_A +\
            price_B * count_B + price_B_bh * count_B +\
            price_C * count_C + price_C_bh * count_C
    print(total)
    # Tổng Giá từ giỏ hàng
    driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
    sleep(2)
    web_total = int(((driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/ul[1]/li[1]/span[2]")).text).replace("đ", "").replace(".", ""))
    # Hiện thông báo
    if (web_total == total):
        driver.execute_script("alert('{} = {}. True');".format(web_total, total))
    else:
        driver.execute_script("alert('False');")



# After test
def After():
    sleep(10)
    driver.quit()


#Befor()
#TC_01()
#TC_02()
#TC_03()
#TC_04()
#TC_05()
#After()
