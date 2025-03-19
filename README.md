# Flask_Basic


### Note for sqlalchemy
- query.all(): truy vấn tất cả object
- query.filter_by("keyword arguments"): Truy vấn tìm kiếm tùy vào tham số 
- tham số lazy=True nghĩa là dữ liệu sẽ không được tải ngay lập tức mà chỉ tải khi thực hiện truy vấn

### Note for keyword:
- Circular Imports: là vấn đề xảy ra khi 2 module cố gắng gọi lẫn nhau, trực tiếp hoặc gián tiếp, dẫn đến xung đột trong quá trình khởi tạo