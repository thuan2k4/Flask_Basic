# Flask_Basic


### Note for sqlalchemy
- query.all(): truy vấn tất cả object
- query.filter_by("keyword arguments"): Truy vấn tìm kiếm tùy vào tham số 
- tham số lazy=True nghĩa là dữ liệu sẽ không được tải ngay lập tức mà chỉ tải khi thực hiện truy vấn
- query.get(): lọc theo khóa chính -> lấy ra 1 object

### Note for keyword:
- Circular Imports: là vấn đề xảy ra khi 2 module cố gắng gọi lẫn nhau, trực tiếp hoặc gián tiếp, dẫn đến xung đột trong quá trình khởi tạo
- Cross Site Request Forgery (CSRF): là một lỗ hổng bảo mật trong ứng dụng web, cho phép kẻ tấn công thực hiện các hành động không mong muốn thay mặt người dùng mà không có sự đồng ý của họ
- Raise được sử dụng để ném (throw) 1 ngoại lệ (exception) trong quá trình thực thi chương trình