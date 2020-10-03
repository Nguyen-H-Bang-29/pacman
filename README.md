# Pacman - A* algorithm - Nguyễn Hữu Bằng (18020196)
## Đề bài :  http://ai.berkeley.edu/search.html

## Điểm autograder
- Question q1: 3/3
- Question q2: 3/3
- Question q3: 3/3
- Question q4: 3/3
- Question q5: 3/3
- Question q6: 0/3
- Question q7: 0/4
- Question q8: 0/3
- **Total**: 15/25

## Question 1 
- Duyệt trạng thái bằng thuật toán DFS sử dụng Đệ quy 
    - Lấy start statestate và kiểm tra có phải GoalState không. Nếu có thì return [].
    - Gọi hàm search với mỗi node con của state hiện tại, kiểm tra, nếu là goalstate thì đánh dấu là đã tìm thấy, nếu không thì gọi đệ quy với các node con, nếu là node lá thì return None.
    - Sau khi goalstate được tìm thấy, mỗi hàm dẫn tới state đó sẽ thêm action vào list. 
    - Đảo ngược list, trả về kết quả.

## Question 2 
- Duyệt trạng thái bằng thuật toán DFS sử dụng Queue:
    - Lấy start statestate và kiểm tra có phải GoalState không. Nếu có thì return [].
    - Khởi tạo 1 queue để lưu những state chuẩn bị xét, state vào sau thì sẽ được xét trước, 1 list visited để lưu những state đã xét.
    - Push start state, path[](để lưu đường đi đến state đó) vào trong stack để bắt đầu duyệt cây statestate.
    - Duyệt state cho đến khi queue empty, pop ra stack cuối cùng mới được thêm và kiểm tra goalState, nếu phải return path[], còn không thì thêm state vào trong visited để duyệt những lần sau không thêm state đã duyệt vào stack.
    - Lặp những trạng thái tiếp theo và hành động đến trạng thái đó và push vào trong queue.


## Question 3 
- Giống Question2 nhưng thay Queue bằng PriorityPriorityQueue với tham số priority = cost đến state đó.
- Khi push vào PriorityQueue thì push object gồm(state, path, cost) và tham số prority.

## Question 4 
- Giống Question3 nhưng thay tham số priority = cost + heuristic.

## Question 5
- Function getStartState(self) 
    - Return vị trí startState sử dụng startingPosition = startingGameState.getPacmanPosition().

- Function isGoalState(self, state)
    - Kiểm tra danh sách các corner còn lại có rỗng hay không (return true nếu rỗng).

- Function getSuccessors(self, state)
    - Lấy độ dài của dx, dy để đi đến state tiếp theo, khởi tạo độ của state tiếp theo = int(x + dx), int(y + dy).
    - Check xem state tiếp theo có là wall không, nếu không cập nhật tọa độ của nextState.
    - Check nextState đã visited hay không, nếu không thì append vào successor ((tọa độ next_state, danh sách những góc còn lại), action, cost).   
## Question 6
- Dự tính cách làm: Viết hàm heuristic cho state, là khoảng cách đến góc gần nhất, sau đó sử dụng thuật toán A* đã cài đặt ở Q4.
## Question 7
- Dự tính cách làm: Viết hàm heuristic cho state, là khoảng cách đến dot gần nhất, sau đó sử dụng thuật toán A* đã cài đặt ở Q4.
## Question 8
- Chưa có dự tính.
