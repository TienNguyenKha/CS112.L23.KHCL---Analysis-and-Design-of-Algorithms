# Assignment 04

## Progress
| Problem | Status | Working Space in Colab |
|:---:|:---:|:--:|
| [Sửa hàng rào](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/6/6) |  ![](https://img.shields.io/badge/progress-0%25-red) | [Google Colab]() |
| [Phân số](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/6/13) | ![](https://img.shields.io/badge/progress-100%25-brightgreen) ![](https://img.shields.io/badge/-PASS%20%E2%9C%93-brightgreen) | [Google Colab]() |

## Problem 1: [Sửa hàng rào](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/6/6)
**Time limit per test: 1 second**

**Memory limit per test: 50 megabytes**

Sau khi dựng xong nhà kho chứa cỏ, dì Poly quyết định dùng ***m*** tấm gỗ còn thừa gia cố hàng rào của vườn rau ngăn không cho gà vào phá và giao công việc này cho Tôm và Hấc Phin làm. Nhiệm vụ của hai cậu bé tội nghiệp là đóng thêm vào các tấm ván hàng rào để có hàng rào mới càng cao càng tốt. Nhìn vẽ mặt buồn thiu và lóng ngóng của 2 đứa Jim quyết định sẽ làm giúp. Hàng rào được ghép từ ***n*** tấm gỗ cùng độ rộng như nhau và bằng độ rộng của các tấm gỗ còn thừa, tấm thứ ***i*** có độ cao ***a<sub>i</sub>, i = 1 ÷ n***. Tôm và Hấc Phin chỉ phải xếp các tấm còn thừa lên xe ba gác để Jim kéo đi. Các tấm gỗ được xếp thành một chồng, tính từ trên xuống tấm thứ ***j*** có độ dài ***b<sub>j</sub>, j = 1 ÷ m***. Jim kéo xe ba gác đi dọc theo hàng rào. Đến một tấm nào đó muốn gia cố Jim sẽ lấy một tấm gỗ từ xe đóng tiếp lên tấm gỗ trên hàng rào và độ cao mới của tấm này trên hàng rào sẽ là tổng độ cao của tấm cũ và tấm mới đóng thêm. Jim chỉ đóng thêm một tấm mới vào tấm cũ vì muốn đảm bảo độ chắc chắn của hàng rào. Jim có thể lấy tấm trên cùng ở xe hoặc vất ra khỏi xe một số tấm cho đến khi gặp tấm vừa ý. Người ta vẫn nói “Khôn đâu tới trẻ, khỏe đâu tới già!”  Jim đã đứng tuổi và không còn sức để xếp lại các tấm gỗ bị bỏ ra vào xe. Ngoài ra, Jim cũng khá mê tín nên không quay lại lấy những tấm đã loại.

Hãy xác định độ cao lớn nhất có thể đạt được của hàng rào sau khi gia cố. Độ cao của hàng rào được tính bằng độ cao tấm gỗ thấp nhất trên hàng rào.

***Dữ liệu:*** Vào từ thiết bị nhập chuẩn:
- Dòng đầu tiên chứa số nguyên ***n*** (1 ≤ ***n*** ≤ 105),
- Dòng thứ 2 chứa ***n*** số nguyên ***a<sub>1</sub>, a<sub>2</sub>, . . ., a<sub>n</sub>*** (1 ≤ ***a<sub>i</sub>*** ≤ 108, ***i = 1 ÷ n***),
- Dòng thứ 3 chứa số nguyên ***m***  (1 ≤ ***m*** ≤ 105),
- Dòng cuối cùng chứ ***m*** số nguyên ***b<sub>1</sub>, b<sub>2</sub>, . . ., b<sub>m</sub>*** (1 ≤ ***b<sub>j</sub>*** ≤ 108, ***j = 1 ÷ m***).

***Kết quả:*** Đưa ra thiết bị xuất chuẩn, dòng đầu tiên chứa 2 số nguyên ***h*** và ***k*** – độ cao lớn nhất có thể của hàng rào và số tấm gỗ đã được đóng thêm, mỗi dòng trong ***k*** dòng tiếp theo chứa 2 số nguyên ***x*** và ***y***, trong đó ***x*** – tấm gỗ trên hàng rào được đóng cao hơn, ***y*** – tấm gỗ được dùng để đóng. Đưa ra phương án có các số hiệu tấm ván được chọn là nhỏ nhất nếu tồn tại nhiều cách đóng khác nhau.

| Input | Output |
|:---|:---|
| **6 <br /> 2 5 4 1 7 5 <br /> 7 <br /> 2 3 1 3 2 4 6** | **5 3 <br /> 1 2 <br /> 3 3 <br /> 4 6** |

## Problem 2: [Phân số](https://khmt.uit.edu.vn/wecode/cs112.2021/assignment/6/13)
**Time limit per test: 1 second**

**Memory limit per test: 50 megabytes**

Cho 2 phân số đúng và tối giản ![equation](https://latex.codecogs.com/png.image?\dpi{120}&space;\mathbf{\frac{a}{b},&space;\frac{c}{c}}). Mỗi phép biến đổi là tăng ***a*** và ***b*** lên 1, sau đó giản ước phân số nhận được.

Hãy xác định sau bao nhiêu bước biến đổi từ phân số thứ nhất ban đầu nhận được phân số thứ 2 đã cho.

***Dữ liệu:*** Vào từ thiết bị nhập chuẩn gồm 4 dòng, mỗi dòng chứa 1 số nguyên ***a, b, c, d***, 0 < ***a*** < ***b*** ≤105, 0 < ***c*** < ***d*** ≤ 105, ***a*** và ***b*** nguyên tố cùng nhau, ***c*** và ***d*** nguyên tố cùng nhau ![equation](https://latex.codecogs.com/svg.image?\mathbf{\frac{a}{b}\neq&space;&space;\frac{c}{c}}).

***Kết quả:*** Đưa ra thiết bị xuất chuẩn số 0 nếu không có cách biến đổi hoặc một số nguyên – số lượng phép biến đổi.

| Input | Output |
|:---|:---|
|**1 6 2 3**|**5**|
