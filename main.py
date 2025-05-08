# Import các thư viện cần thiết
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from PIL import Image
from io import BytesIO
import easyocr
import schedule
from dotenv import load_dotenv
import os

def check_phat_nguoi():
    """Hàm chính để kiểm tra phạt nguội"""
    print("Đang kiểm tra phạt nguội...")
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()
    # Truy cập trang web kiểm tra phạt nguội
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")

    # Nhập biển số xe
    name = 'BienKiemSoat'
    element_bs = driver.find_element(By.NAME, name)
    element_bs.send_keys("29A-123.45")  # Thay đổi biển số xe tại đây

    # Chọn loại phương tiện (1 = Ô tô, 2 = Xe máy, 3 = xe máy điện)
    loai_xe = driver.find_element(By.XPATH,'/html/body/center/div[3]/div/div[2]/div[2]/div/div/div[1]/form/div/div[2]/div[2]/select')
    select = Select(loai_xe)
    select.select_by_value("2")

    # Lấy và lưu ảnh captcha
    img_url = driver.find_element(By.ID, 'imgCaptcha')
    img_src = img_url.screenshot_as_png
    img = Image.open(BytesIO(img_src))
    img.save("captcha.png")

    # Đọc captcha bằng OCR
    time.sleep(5)  # Chờ 5 giây để đảm bảo ảnh đã được lưu
    reader = easyocr.Reader(['en'])  # Khởi tạo EasyOCR với ngôn ngữ tiếng Anh
    result = reader.readtext('captcha.png',detail=0)  # Đọc text từ ảnh captcha

    # Nhập mã captcha vào form
    captcha_input = driver.find_element(By.XPATH, '/html/body/center/div[3]/div/div[2]/div[2]/div/div/div[1]/form/div/div[2]/div[3]/div/input')
    captcha_input.click()
    captcha_input.send_keys(result[0])
    time.sleep(1)

    # Nhấn nút tra cứu
    btn = driver.find_element(By.CLASS_NAME,'btnTraCuu')
    btn.click()
    time.sleep(10)

    # Kiểm tra kết quả
    check_code = driver.find_element(By.CLASS_NAME,'xe_texterror').text
    if check_code != "":
        print('Giải mã thất bại')
        driver.close()
        check_phat_nguoi()  # Thử lại nếu giải mã thất bại
    else:
        # Xử lý kết quả tìm kiếm
        fin = driver.find_element(By.XPATH,'/html/body/center/div[3]/div/div[2]/div[2]/div/div/div[2]/div').text
        if fin == "Không tìm thấy kết quả !":
            print('Không tìm thấy phương tiện của bạn')
        else:
            print('Tìm kiếm thành công')
        driver.close()

# Thiết lập lịch chạy tự động
schedule.every().day.at("6:00").do(check_phat_nguoi)  # Chạy lúc 6 giờ sáng
schedule.every().day.at("12:00").do(check_phat_nguoi)  # Chạy lúc 12 giờ trưa

# Vòng lặp chính của chương trình
print("Đang chạy script kiểm tra phạt nguội...")
while True:
    schedule.run_pending()  # Kiểm tra và thực thi các tác vụ đã lập lịch
    time.sleep(60)  # Chờ 60 giây trước khi kiểm tra lại
