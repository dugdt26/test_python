#  Q1:What is the difference between list and tuples in Python?
-   tuple:
    - Tuple bát biến, không thể thay đổi, không thể xoá phần tử trong Tuple
- List: 
    - Có thể thay đổi được, gán, thêm sửa xóa các giá trị.

# Q2: What are the key features of Python?
- Dễ học, dễ sử dụng
- Đa nền tảng
- Mã nguồn mở miễn phí, nhiều thư viện
- Dễ dàng mở rộng
- Là ngôn ngữ lập trình hướng đối tượng

# Q3: What type of language is python?
- Là ngôn ngữ hướng đối tượng.
- Python là ngôn ngữ thông dịch

# Q4: How is Python an interpreted language?
- Dòng lệnh được dịch sang bytecode, sau đó bytecode tiếp tục được thực thi bởi VM. Nhưng vì quá trình  dịch sang bytecode và thực thi bytecode hoàn toàn ẩn bởi Interactive Prompt của Python.

# Q5: What is pep 8?
 -  PEP_8  là tập hợp các chỉ dẫn về định dạng code, phong cách lập trình được chia sẻ chung giữa các lập trình viên Python 

# Q6 : How is memory managed in Python?

# Q7: What is name space in Python?
- Namespace trong Python còn gọi là không gian tên, là một hệ thống có một tên duy nhất cho mỗi mọi đối tượng trong Python. Một đối tượng có thể là một biến hoặc một phương thức.

# Q8:  What is PYTHON PATH?
-  là một biến môi trường để thêm các thư mục python sẽ tìm kiếm các mô-đun và gói
# Q9: What are python modules?
- Module đề cập đến một file chứa những câu lệnh Python và các định nghĩa

# Q10: What are local variables and global variables in Python? Please give an exam
- Biến toàn cục sẽ có tác dụng cho cả chương trình. Bộ nhớ chỉ được giải phóng khi chương trình kết thúc
     - vd: 
            x = "global"
            def foo():
                print("x inside :", x)
 
            foo()
                print("x outside:", x)

- biến cục bộ chỉ có tác dụng trong 1 hàm. Bộ nhớ sẽ được giải phóng khi kết thúc hàm đó
    - vd: 
        def foo():
            y = "local"
            print(y)

# Q11: What is __init__?
- __init__ là hàm khởi tạo hay constructor của một class

# Q12: What is self in Python?
- self biến đại diện cho thể hiện của chính đối tượng