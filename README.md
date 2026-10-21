# Lab9_SELENIUM_DG-KDPM
# THỰC HÀNH KIỂM THỬ TỰ ĐỘNG VỚI SELENIUM

## 1. Giới thiệu

Bài thực hành nhằm tìm hiểu và sử dụng Selenium để xây dựng các test case kiểm thử tự động cho một website thực tế.

Trong bài tập này, Selenium WebDriver kết hợp với Python và Pytest được sử dụng để tự động hóa các thao tác trên website bán hàng mẫu SauceDemo.

Website kiểm thử: https://www.saucedemo.com/

Các chức năng được kiểm thử bao gồm đăng nhập, xử lý đăng nhập sai, sắp xếp sản phẩm, thêm sản phẩm vào giỏ hàng và đăng xuất.

## 2. Mục tiêu

- Tìm hiểu cách sử dụng Selenium WebDriver để điều khiển trình duyệt tự động.
- Sử dụng Python để xây dựng các kịch bản kiểm thử.
- Sử dụng Pytest để thực thi và đánh giá kết quả các test case.
- Kiểm tra tính đúng đắn của các chức năng cơ bản trên website.
- Thực hành xác minh kết quả thực tế với kết quả mong đợi.

## 3. Công cụ và môi trường

- Hệ điều hành: Windows.
- Ngôn ngữ lập trình: Python 3.14.3.
- Trình soạn thảo: Visual Studio Code.
- Công cụ tự động hóa: Selenium WebDriver.
- Framework kiểm thử: Pytest 9.1.1.
- Trình duyệt: Google Chrome.
- Website kiểm thử: SauceDemo.

## 4. Cài đặt môi trường

### Bước 1: Cài đặt thư viện

Mở Terminal trong Visual Studio Code và chạy lệnh:

```bash
python -m pip install selenium pytest
```

### Bước 2: Tạo cấu trúc dự án

```text
Selenium/
├── tests/
│   └── test_saucedemo.py
└── README.md
```

Trong đó:

- `tests/test_saucedemo.py`: Chứa mã nguồn của 5 test case kiểm thử tự động.
- `README.md`: Tài liệu mô tả bài thực hành và kết quả kiểm thử.

### Bước 3: Tài khoản kiểm thử

- Website: https://www.saucedemo.com/
- Username: `standard_user`
- Password: `secret_sauce`

Đây là tài khoản mẫu được sử dụng để thực hiện các thao tác kiểm thử trên website.

## 5. Các test case kiểm thử

### TC01: Kiểm thử đăng nhập thành công

**Mục tiêu:** Kiểm tra chức năng đăng nhập với thông tin tài khoản hợp lệ.

**Dữ liệu đầu vào:**
- Username: `standard_user`
- Password: `secret_sauce`

**Các bước thực hiện:**
1. Mở website SauceDemo.
2. Nhập username và password hợp lệ.
3. Nhấn nút Login.
4. Kiểm tra trang sau khi đăng nhập.

**Kết quả mong đợi:** Người dùng đăng nhập thành công và danh sách sản phẩm được hiển thị.

### TC02: Kiểm thử đăng nhập thất bại

**Mục tiêu:** Kiểm tra khả năng xử lý khi người dùng nhập sai mật khẩu.

**Dữ liệu đầu vào:**
- Username: `standard_user`
- Password: `wrong_password`

**Các bước thực hiện:**
1. Mở website SauceDemo.
2. Nhập username hợp lệ.
3. Nhập mật khẩu không chính xác.
4. Nhấn nút Login.
5. Kiểm tra thông báo lỗi.

**Kết quả mong đợi:** Hệ thống từ chối đăng nhập và hiển thị thông báo lỗi phù hợp.

### TC03: Kiểm thử sắp xếp sản phẩm theo giá tăng dần

**Mục tiêu:** Kiểm tra chức năng sắp xếp sản phẩm theo giá từ thấp đến cao.

**Các bước thực hiện:**
1. Đăng nhập bằng tài khoản hợp lệ.
2. Mở danh sách sản phẩm.
3. Chọn tùy chọn Price (low to high).
4. Lấy giá của các sản phẩm được hiển thị.
5. So sánh thứ tự giá với danh sách đã sắp xếp tăng dần.

**Kết quả mong đợi:** Giá sản phẩm được sắp xếp theo thứ tự tăng dần.

### TC04: Kiểm thử thêm sản phẩm vào giỏ hàng

**Mục tiêu:** Kiểm tra chức năng thêm sản phẩm vào giỏ hàng.

**Các bước thực hiện:**
1. Đăng nhập bằng tài khoản hợp lệ.
2. Tìm sản phẩm Sauce Labs Backpack.
3. Nhấn nút Add to cart.
4. Kiểm tra số lượng sản phẩm trên biểu tượng giỏ hàng.

**Kết quả mong đợi:** Sản phẩm được thêm vào giỏ hàng và số lượng hiển thị là 1.

### TC05: Kiểm thử đăng xuất

**Mục tiêu:** Kiểm tra chức năng đăng xuất khỏi hệ thống.

**Các bước thực hiện:**
1. Đăng nhập bằng tài khoản hợp lệ.
2. Mở menu điều hướng.
3. Nhấn nút Logout.
4. Kiểm tra trang sau khi đăng xuất.

**Kết quả mong đợi:** Người dùng được đăng xuất và quay trở lại trang đăng nhập.

## 6. Cách thực thi kiểm thử

Mở Terminal tại thư mục gốc của dự án và chạy toàn bộ test case bằng lệnh:

```bash
python -m pytest tests/test_saucedemo.py -v
```

Để chạy riêng test case đăng xuất:

```bash
python -m pytest tests/test_saucedemo.py::test_logout -v --tb=long
```

Pytest sẽ thực thi các test case, hiển thị trạng thái PASS hoặc FAILED và cung cấp thông tin lỗi khi có vấn đề xảy ra.

## 7. Kết quả kiểm thử

<img width="1258" height="422" alt="SeleniumKQ" src="https://github.com/user-attachments/assets/dced541e-9de1-4fde-b6cd-8e7df8c1e0d6" />

Trong lần thực thi được ghi nhận, Pytest đã thu thập và chạy 5 test case.

- TC01 – Đăng nhập thành công: PASSED.
- TC02 – Đăng nhập thất bại: PASSED.
- TC03 – Sắp xếp sản phẩm theo giá tăng dần: PASSED.
- TC04 – Thêm sản phẩm vào giỏ hàng: PASSED.
- TC05 – Đăng xuất: FAILED.

Tổng kết lần chạy này: 4/5 test case thành công, tương đương 80%.

Test case đăng xuất cần được kiểm tra và sửa lỗi trước khi kết luận chức năng đã được kiểm thử thành công. Kết quả trên là kết quả của lần chạy được ghi nhận và có thể thay đổi sau khi sửa mã nguồn.


## 8. Kết luận
Selenium WebDriver kết hợp với Python và Pytest để kiểm thử tự động các chức năng cơ bản của một website bán hàng.

5 test case được xây dựng để kiểm tra đăng nhập thành công, đăng nhập thất bại, sắp xếp sản phẩm, thêm sản phẩm vào giỏ hàng và đăng xuất.

Kết quả cho thấy 4 test case đã chạy thành công trong lần thực thi được ghi nhận. Test case đăng xuất cần được tiếp tục kiểm tra và khắc phục lỗi.

Bài thực hành giúp củng cố kiến thức về kiểm thử tự động, cách viết test case, sử dụng assertion để xác minh kết quả và phát hiện lỗi trong quá trình kiểm thử.
