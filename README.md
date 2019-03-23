# Giới thiệu về Source Tree, Package, File Json, Class.

# Tổ chức thư mục theo kiểu Source Tree trong Python và các ký hiệu đối với File và Class

## Chỉ đơn giản là cách tạo thư mục và lưu trữ File cho dễ quản lý hơn và dễ xử lý.
### Trong 1 Folder chính đối với python ta cần tạo 4 Folder con sau
- Folder 'static' : Folder này dùng để chứa các thư mục chứa các file hình ảnh(.jpg,.jpge,.png,...) hoặc thư mục chứa các file thiết kế(.css)
- Folder 'templates' : Folder này dùng để lưu trữ các File Giao diện như (.py tkinter, .pyQt, .md, .html, ...)
- Folder 'env' : Folder này sẽ chứa các file khởi tạo thư viện hoặc file khai báo thư viện.
- Folder 'modules' : Folder này mục đich chứa các thư mục xử lý chức năng cho các file trong folder 'env'.

Ta phải lưu ý là Folder 'env' và 'modules' có thể đặt tên là bất kì cái gì cũng được, tuy nhiên folder 'static' và 'templates' bắt buộc phải ghi đúng.

Ngoài ra ta còn tổ chức thêm 1 file run.py hay app.py ở trong Folder chính, cùng cấp độ với các Folder phía trên. Mục đích của việc tạo file này là ta sẽ gọi các framework được xây dựng từ các thư viện mà ta khởi tạo trong env và chạy lệnh trực tiếp lên file này. Vừa đảm bảo tính bảo mật tốt hơn, vừa đảm bảm dễ dàng chạy file khi gọi lệnh từ Commandline hay Terminal.

## Về quy tắc đặt tên File, tên biến, tên hàm và Class trong Python
### Chúng ta có 2 cách đặt tên cho dễ nhìn đối với tất cả các biến và hàm như sau:
-Quy tắc thứ nhất quy tắc con rắn: tên sẽ được đặt như sau ví dụ toi_hoc_python. Mỗi 1 từ cách nhau bởi dấu "_"
-Quy tắc thứ hai quy tắc lưng lạc đà: tên sẽ đặt như sau ví dụ toiHocPython. Từ đầu tiên viết thường và những chữ đầu tiên trở về sau viết hoa.


### Quy tắc đặt tên Class:
- Quy tắc đặt tên Class thì sẽ theo quy tắc lưng lạc đà, tuy nhiên là phải viết hoa chữ cái đầu tiên luôn. Lưu ý tên file phải theo tên class chứ không phải đặt tên class theo tên File (phần này về sau sẽ nói rõ hơn), ví dụ:
class ToiHocPython,class BaiTapVeNha

### Quy tắc đặt tên file:
- Quy tắc đặt tên file trong python là sử dụng quy tắc con rắn(trùng ý nghĩa với python) và trùng tên với tên Class khai báo bên trong, tất cả chữ cái phải viết thường, ví dụ:
+ Đối với class khai báo là class ToiHocPython thì tên file sẽ là toi_hoc_python.py
+ Tương tự đối với class BaiTapVeNha thì tên file sẽ là bai_tap_ve_nha.py

## **Lưu ý quan trọng trong tất cả các folder có chứa file .py . Ta luôn phải tạo 1 file có tên là __init__.py trong từng folder mà có file .py hiện hành. Điều này sẽ giúp ta có thể import file từ folder này sang folder khác.

