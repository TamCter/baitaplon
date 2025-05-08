# Kiểm Tra Phạt Nguội Xe Cộ

Công cụ tự động kiểm tra vi phạm giao thông trên trang CSGT.vn sử dụng Selenium WebDriver.

## Tính Năng

- Tự động kiểm tra phạt nguội 2 lần mỗi ngày (6h sáng và 12h trưa)
- Tự động xử lý mã CAPTCHA bằng OCR
- Hỗ trợ trình duyệt Chrome
- Hiển thị thông báo trạng thái kiểm tra

## Yêu Cầu Hệ Thống

- Python 3.x
- Trình duyệt Chrome
- Các thư viện Python cần thiết

## Cài Đặt

1. Cài đặt các thư viện Python từ file requirements.txt:
```bash
pip install -r requirements.txt
```

2. Hoặc cài đặt thủ công các thư viện:
```bash
pip install selenium pillow easyocr schedule python-dotenv webdriver-manager
```

3. Cài đặt Chrome WebDriver (tự động thông qua webdriver-manager)

## Cách Sử Dụng

1. Cấu hình thông tin xe:
   - Mở file `main.py`
   - Thay đổi biển số xe tại dòng `element_bs.send_keys("29A-123.45")`
   - Thay đổi loại xe nếu cần (`select.select_by_value("2")`)

2. Chạy chương trình:
```bash
python main.py
```

## Lịch Chạy Tự Động

- 6:00 sáng mỗi ngày
- 12:00 trưa mỗi ngày

## Cấu Trúc Mã Nguồn

- `main.py`: File chính chứa mã nguồn
- `captcha.png`: File tạm lưu ảnh CAPTCHA