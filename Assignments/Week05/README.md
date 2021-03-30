# Week 5

## Progrees
| Problem | Status | Working Space in Colab |
|:---:|:---:|:--:|
| [H-index](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/3/4) | ![](https://img.shields.io/badge/progress-0%25-red) | [Google Colab]() |
| [Khóa số](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/3/9) | ![](https://img.shields.io/badge/progress-0%25-red) | [Google Colab]() |
| [Con đường gốm sứ (KHTN)](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/3/17) | ![](https://img.shields.io/badge/progress-0%25-red) | [Google Colab]() |

## Problem 1: [H-index](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/3/4)
**Time limit per test: 1 second**

**Memory limit per test: 100 megabytes**

Làm thế nào để đánh giá sự thành công của một nhà khoa học?  Dựa vào số bài báo được công bố hay dựa vào số lần một bài báo được trích dẫn tới ở công trình của những người khác? Cả hai tham số đó đều quan trọng.

Một bài báo có điểm số trích dẫn là ***c*** nếu nó được trích dẫn tới ***c*** lần trong các công trình của những nhà khoa học khác. Một trong số các cách đánh giá sự thành công của một nhà khoa học là tính chỉ số ảnh hưởng ***H_Index*** dựa trên sự kết hợp giữa số lượng bài báo và chỉ số trích dẫn của các bài báo đó.

Chỉ số ***H_Index*** của một nhà khoa học bằng ***k*** lớn nhất nếu người đó có ***k*** bài báo, mỗi bài có điểm số trích dẫn không nhỏ hơn ***k***. Ví dụ, một người có 10 bài báo, mỗi bài báo được trích dẫn không dưới 10 lần thì ***H_Index*** của người đó ít nhất là bằng 10.

Một người có ***n*** bài báo, bài báo thứ ***i*** có điểm trích dẫn là ***c<sub>i</sub>***, ***i = 1 ÷ n***. Hãy xác định ***H_Index*** của người đó.

**Dữ liệu:** Vào từ thiết bị nhập chuẩn:

  - Dòng đầu tiên chứa một số nguyên ***n*** (1 ≤ ***n*** ≤ 5×10<sup>5</sup>)),
  - Dòng thứ 2 chứa ***n*** số nguyên ***c<sub>1</sub>, c<sub>2</sub>, . . ., c<sub>n</sub>*** (0 ≤ c<sub>i</sub> ≤ 10<sup>6</sup>, ***i*** = 1 ÷ ***n***).
  
**Kết quả:** Đưa ra thiết bị xuất chuẩn một số nguyên ***– H_Index*** tìm được.

| Input | Output |
|:---|:---:|
| 5 <br /> 8 5 3 4 10 | 15 |
