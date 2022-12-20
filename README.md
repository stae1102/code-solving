https://github.com/tony9402/baekjoon 의 정리법을 참고하여 작성

- [알고리즘 문제집](#알고리즘-문제집)
- [도움될 스킬들](#도움될-스킬들)
  - [1. 딕셔너리](#1-딕셔너리)
    - [딕셔너리 값 추가](#딕셔너리-값-추가)
    - [딕셔너리 + zip 활용](#딕셔너리--zip-활용)
    - [딕셔너리 setdefault 메서드](#딕셔너리-setdefault-메서드)
  - [2. 문자열](#2-문자열)
    - [strip 활용](#strip-활용)
    - [배열 회전하기](#배열-회전하기)
  - [3. 조합론](#3-조합론)
    - [Combination/Permutation](#combinationpermutation)
  - [4. 수학](#4-수학)
    - [최대 공약수](#최대-공약수)
    - [나머지를 같게 하는 공약수](#나머지를-같게-하는-공약수)
- [알고리즘 스터디](#알고리즘-스터디)
  - [스택&큐](#스택큐)
  - [그래프 탐색](#그래프-탐색)

---

# 알고리즘 문제집

| 순번 | 알고리즘(Kor)   | 알고리즘(Eng)             | 문제집 | 총 문제                                                 |
| ---- | --------------- | ------------------------- | ------ | ------------------------------------------------------- |
| 00   | 스택            | Stack                     |        |                                                         |
| 01   | 큐              | Queue                     |        |                                                         |
| 02   | 트리            | Tree                      |        | [바로가기](./Workbook/Tree/README.md)                   |
| 03   | 맵              | Map                       |        | [바로가기](./Workbook/Map/README.md)                    |
| 04   | 힙, 우선순위 큐 | Heap, Priority Queue      |        | [바로가기](./Workbook/Priority%20Queue/README.md)       |
| 05   | 탐욕법          | Greedy                    |        | [바로가기](./Workbook/Greedy/README.md)                 |
| 06   | 분할 정복       | Divide & Conquer          |        | [바로가기](./Workbook/Divide%20%26%20Conquer/README.md) |
| 07   | 완전 탐색       | Brute Force               |        |                                                         |
| 08   | 백트래킹        | Backtracking              |        | [바로가기](./Workbook/Backtracking/README.md)           |
| 09   | 그래프 탐색     | Graph Traversal(DFS, BFS) |        | [바로가기](./Workbook/Graph%20Traversal/README.md)      |
| 10   | 수학            | Math                      |        | [바로가기](./Workbook/Math/README.md)                   |
| 11   | 이분탐색        | Binary Search             |        | [바로가기](./Workbook/Math/Binary%20Search.md)          |
| 12   | 정렬            | Sorting                   |        |                                                         |
| 13   | 문자열          | String                    |        |                                                         |
| 14   | 동적 프로그래밍 | Dynamic Programming       |        | [바로가기](./Workbook/Dynamic%20Programming/README.md)  |
| 15   | 위상정렬        | Topological Sorting       |        |                                                         |
| 16   | 투 포인터       | Two Pointer               |        |                                                         |

# 도움될 스킬들

## 1. 딕셔너리

### 딕셔너리 값 추가

```py
딕셔너리 값 추가

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)
```

`counts.get(name, 0)` 의 의미는 counts 딕셔너리에 name이라는 키가 존재할 경우 name에 대한 값에 1을 더하고, 그렇지 않을 경우에는 counts 딕셔너리에 name이라는 키에 1 값을 추가

---

### 딕셔너리 + zip 활용

```py
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]

_dict = dict(zip(fruit, price))
# {'apple' : 3200, 'grape' : 15200, 'orange' : 9800, 'banana' : 5000}
```

zip을 적절히 활용하여 리스트 자료형 두 개를 딕셔너리로 바꿀 수 있다.

---

### 딕셔너리 setdefault 메서드

```py
print(_dict.setdefault('strawberry', 0)) # 0
```

딕셔너리 값이 있을 땐 해당 값을 리턴하고, 값이 없을 땐 두 번째 인자로 넘겨준 값을 추가하고 추가한 값을 리턴

## 2. 문자열

### strip 활용

```py
print('===chicken==='.strip('=')) # chicken

print('=^chicken^='.strip('=^')) # chicken
```

strip의 인자로 값을 부여하면 그 인자 속 문자열들을 모두 삭제한다.

---

### 배열 회전하기

```py
def rotate(arr):
    return list(zip(*arr[::-1]))

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [(7, 4, 1), (8, 5, 2), (9, 6, 3)]
```

arr 배열을 역순으로 unpacking하며 그것을 zip을 통해 리스트로 저장한다. 그렇게 하면

<table>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <td>4</td>
        <td>5</td>
        <td>6</td>
    </tr>
    <tr>
        <td>7</td>
        <td>8</td>
        <td>9</td>
    </tr>
</table>

위와 같은 2차원 배열을

<table>
    <tr>
        <td>7</td>
        <td>4</td>
        <td>1</td>
    </tr>
    <tr>
        <td>8</td>
        <td>5</td>
        <td>2</td>
    </tr>
    <tr>
        <td>9</td>
        <td>6</td>
        <td>3</td>
    </tr>
</table>

위와 같이 로테이션이 가능하다.

## 3. 조합론

### Combination/Permutation

```py
import itertools
_list = [1, 2, 3, 4]
```

1. 중복이 없고 순서를 구분

```py
iter = itertools.combinations(_list, 2)
# 12 13 14 23 24 34
```

2. 중복이 없지만 순서를 구분

```py
iter = itertools.permutations(_list, 2)
# 12 13 14 21 23 24 31 32 34 41 42 43
```

3. 중복이 가능한 조합

```py
iter = itertools.combinations_with_replacement(_list, 2)
# 11 12 13 14 22 23 24 33 34 44
```

4. 모든 경우의 수

```py
iter = itertools.product(_list, repeat=2)
# 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44
```

## 4. 수학

### 최대 공약수

1. 유클리드 호제법

```py
def gcd(a, b):
    tmp = a % b
    while tmp != 0:
        a = b
        b = tmp
        tmp = a % b
    return b

print(gcd(10, 12)) # 2
```

### 나머지를 같게 하는 공약수

예를 들어,

```
A = M * a + R
B = M * b + R
C = M * c + R
```

와 같은 수가 있다고 하자.

이때, B - A를 통해 나머지를 없애면,

```
B - A = M * b - M * a = M(b - a)
```

와 같다. 이는 동일하게

```
C - B = M(c - b)
```

와 같이 나온다.

즉, 각 수들을 빼준 다음 그 수들 간의 공약수를 계산하면 된다.

---

예)

```py
n = int(input())
l = sorted([int(input()) for _ in range(n)])
re_l = []

for i in range(1, n):
    re_l.append(l[i] - l[i-1])

def gcd(a, b):
    tmp = a % b
    while tmp != 0:
        a = b
        b = tmp
        tmp = a % b
    return b

GCD = re_l[0]
for i in range(1, len(re_l)):
    GCD = gcd(GCD, re_l[i])
```

이때 마지막 for 반복문으로 최대 공약수를 구하고, 최대 공약수의 약수들을 구하면 모든 공약수를 구할 수 있다.

공약수는 기존의 수의 제곱근을 통해 구하는 것이 시간 복잡도를 줄일 수 있는 방법이다. 예를 들어 36의 공약수는
`1, 2, 3, 4, 6, 9, 12, 18, 36` 이렇게 나오는데, 유심히 보면 마치 데칼코마니 같은 구조를 갖고 있다.

1 _ 36 = 36, 2 _ 18 = 36, 3 _ 12 = 36, 4 _ 9 = 36, 6 \* 6 = 36

```py
result = set()
for i in range(1, int(GCD ** 0.5) + 1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
```

즉 위와 같이 구하는 것이 시간을 최대한 단축할 수 있는 방법이다.

# 알고리즘 스터디

## 스택&큐

## 그래프 탐색

수정 예정
