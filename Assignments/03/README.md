# Assignment 03

## Progress
| Problem | Status | Working Space in Colab |
|:---:|:---:|:--:|
| [Đổi mới](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/5/8) | ![](https://img.shields.io/badge/progress-0%25-red) | [Google Colab]() |
| [Số nguyên mới](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/5/15) | ![](https://img.shields.io/badge/progress-0%25-red) | [Google Colab]() |

## Problem 1: [Đổi mới](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/5/8)
**Time limit per test: 0.1 second**

**Memory limit per test: 50 megabytes**

Thành phố quyết định chặt hạ hết ***n*** cây xanh hiện có trong thành phố để trồng chỉ một loại cây mới. Nhiệm vụ được giao cho Công ty Cây xanh thành phố. Do hạn chế về thiết bị Công ty chỉ tổ chức được 2 đội đốn hạ cây. Đội I hạ được ***a*** cây mỗi ngày, nhưng cứ mối ngày thứ ***k*** thì phải nghỉ để bảo dưỡng kỹ thuật, tức là đội I sẽ nghỉ vào các ngày ***k***, 2***k***, 3***k***, ... Đội II hạ được ***b*** cây mỗi ngày, nhưng cứ mỗi ngày thứ ***m*** thì phải nghỉ để bảo dưỡng kỹ thuật, tức là đội II sẽ nghỉ vào các ngày ***m***, 2***m***, 3***m***, ... Ở ngày nghỉ, số cây chặt hạ của đội sẽ là 0. Cả hai đội bắt đầu công việc vào cùng một ngày và làm việc song song với nhau.

Công việc trồng cây mới sẽ bắt đầu sau khi toàn bộ cây cũ đã bị đốn hạ.

Hãy xác định sau bao nhiêu ngày thì có thể bắt đầu việc trồng mới cây.

**Dữ liệu:** Vào từ thiết bị nhập chuẩn gồm một dòng chứa 5 số nguyên ***a***, ***k***, ***b***, ***m*** và ***n*** (1 ≤ ***a***, ***b*** ≤ 10<sup>9</sup>, 2 ≤ ***k***, ***m*** ≤ 10<sup>18</sup>, 1 ≤ ***n*** ≤ 10<sup>18</sup>).

**Kết quả:** Đưa ra thiết bị xuất chuẩn một số nguyên – số ngày tính được.

| Input | Output |
|:---:|:---:|
| 2 4 3 3 25 | 7 |


## Problem 2: [Số nguyên mới](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/5/15)
**Time limit per test: 0.1 second**

**Memory limit per test: 50 megabytes**

Cho số nguyên dương ***n*** có không quá 100 chữ số. Hãy xác định số nguyên lớn nhất ***m*** chia hết cho 3 và khác ***n*** ở đúng một chữ số.

Ví dụ, ***n*** = 123 thì ***m*** sẽ là 723.

**Dữ liệu:** Vào từ thiết bị nhập chuẩn gồm một dòng chứa số nguyên ***n*** có không quá 100 chữ số và không chứa các số 0 không có nghĩa.

**Kết quả:** Đưa ra thiết bị xuất chuẩn số nguyên ***m*** tìm được.

| Input | Output |
|:---:|:---:|
| 123 | 723 |
