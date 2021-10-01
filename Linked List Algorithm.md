# 리스트 알고리즘
* [연결 리스트 알아보기](#연결-리스트-알아보기)

## 연결 리스트 알아보기
리스트는 순서가 있는 데이터를 나열한 __자료구조__
### 선형 리스트(Linear list)
### 연결 리스트(Linked list)
> - 연결 리스트는 각각의 원소인 노드로 이어진 구조로, 노드는 데이터와 뒤쪽 노드를 가리키는(참조하는) 포인터로 구성되어 있다.
> - 맨 앞 노드: 머리 노드(Head node)
> - 맨 끝 노드: 꼬리 노드(Tail node)
> - 앞 노드: 앞쪽 노드(Predecessor node)
> - 뒤 노드: 뒤쪽 노드(Seccessor node)

## 배열로 연결 리스트 만들기
단순 배열은 데이터를 삽입·삭제함에 따라 데이터를 옮겨야 하기 때문에 비효율적

<br></br>
# 포인터를 이용한 연결리스트
## 포인터로 연결리스트 만들기
Node는 데이터용 필드인 data와 별도로 자신과 같은 클래스형의 인스턴스를 참조하기 위한 참조용 필드 next를 가진다.
- 자기 참조형(Self-Referential): 자신과 같은 형의 인스턴스를 참조하는 필드가 있는 구조
> data: 데이터에 대한 참조, next: 노드에 대한 참조
> 뒤쪽 노드가 없는 꼬리노드는 뒤쪽 포인터의 값이 None



### 노드 클래스 Node


```python
# 포인터로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    """연결 리스트용 노드 클래스"""

    def __init__(self, data: Any = None, next: Node = None):
        """초기화"""
        self.data = data    # 데이터
        self.next = next    # 뒤쪽 포인터
.
.
.
```
노드 클래스 Node에는 다음과 같은 필드와 \__init__()함수가 있습니다.

- 필드
> data: 데이터(데이터에 대한 참조: 임의의 형).
> next: 뒤쪽 포인터(뒤쪽 노드에 대한 참조: Node형).

- \_\_init()\_\_함수

\_\_init()\_\_ 함수는 전달받은 data와 next를 해당 필드에 대입. 호출할 때 어떤 인구도 생략할 수 있으며, 생략할 경우에는 None으로 간주

<br></br>

### 연결 리스트 클래스 LinkedList
```python
class LinkedList:
    """연결 리스트 클래스"""

    def __init__(self) -> None:
        """초기화"""
        self.no = 0           # 노드의 개수
        self.head = None      # 머리 노드
        self.current = None   # 주목 노드

    def __len__(self) -> int:
        """연결 리스트의 노드 개수를 반환"""
        return self.no
```
연결 리스트 클래스 LinkedList는 다음과 같이 필드 3개로 구성됩니다.

```
▶ no: 리스트에 등록되어 있는 노드의 개수입니다.
▶ head: 머리 노드에 대한 참조입니다.
▶ current: 현재 주목하고 있는 노드에 대한 참조이며, 주목 포인터. 리스트에서 노드를 검색하여, 그 노드를 주목한 직후에 노드를 삭제하는 등의 용도로 사용
```

<br></br>

### 초기화하는 \_\_init_\_() 함수
▶연결 리스트 클래스 LinkedList의 \_\_init()\_\_ 함수는 노드가 하나도 없는 빈 연결 리스트를 생성합니다.
- 머리 노드를 참조하기 위한 Node형 필드 head에 None을 대입합니다.
- head는 머리 노드에 대한 참조일뿐 머리 노드 그 자체가 아님을 주의
- 노드가 존재하지 않는 빈 연결리스트는 head가 참조하는 곳이 없으므로 **(참조해야 하는 노드가 존재하지 않으므로)** 그 값을 None으로 합니다.

<br></br>

### 노드 개수를 반환하는 \_\_len\_\_() 함수
▶연결 리스트의 노드 개수를 반환하는 함수입니다. no값을 그대로 반환합니다.

* 빈 연결 리스트
> 연결 리스트가 비어 있을 **(노드가 하나도 존재하지 않을)** 때 head값은 None입니다.   
> 그러므로 연결 리스트가 비어 있는지는 다음 식으로 검사할 수 있습니다.

```python
head is None    # 연결 리스트가 비어 있는지 확인
```

* 노트가 1개인 연결 리스트

<img src="https://user-images.githubusercontent.com/83271772/135371252-66390330-e044-42c1-961a-ecc7790e2297.png" width="40%" height="30%" title="노드가 1개인 연결리스트" alt="Node"></img>

> Node형 필드인 head가 참조하는 곳은 머리 노드A 입니다.   
> 이 머리노드 A는 리스트의 꼬리노드이기도 뒤쪽 포인터의 값은 None입니다.   
> head가 참조하는 뒤쪽 포인터의 값이 None이므로 연결 리스트에 존재하는 노드가 하나뿐인지는 다음 식으로 수행할 수 있습니다.   

```python
head.next is None    # 연결 리스트의 노드가 1개인지 확인
```

* 노드가 2개인 연결 리스트

<img src="https://user-images.githubusercontent.com/83271772/135372023-97375fb7-aea8-4fe4-aaf8-590c5b58c466.png" width="40%" height="30%" title="노드가 2개인 연결리스트" alt="Node"></img>

> 머리노드는 노드 A이고, 꼬리 노드는 노드 B입니다.   
> 이때, head가 참조하는 곳인 노드 A의 뒤쪽 포인터 next가 노드 B를 참조합니다.   
> 맨 끝에 위치한 노드 B의 뒤쪽 포인터가 None이므로 연결 리스트의 노드가 2개인지는 다음 식으로 수행할 수 있습니다.

```python
head.next.next is None    # 연결 리스트의 노드가 2개인지 확인
```
` ★ 뒤쪽 포인터가 아니라 데이터를 나타내는 식은 head.data, head.next.data`

` 지금까지 살펴본 3가지 경우의 판단은 no == 0, no == 1, no == 2를 사용할 수 있다.

* 꼬리 노드의 판단
> Node형인 변수 p가 리스트에 있는 노드를 참조한다면, 이때 p가 참조하는 노드가 연결 리스트의 꼬리 노드인지는 다음 식으로 수행할 수 있습니다.

```python
p.next is None    # p가 참조하는 노드가 꼬리 노드인지 확인
```

<br></br>

### 검색을 수행하는 search() 함수
▶인수로 주어진 데이터 data와 값이 같은 노드를 검색하는 함수
> * 검색 알고리즘은 선형 검색을 사용   
> * 목적 노드를 만날 때까지 머리 노드부터 순서대로 스캔

![노드 서치](https://user-images.githubusercontent.com/83271772/135406506-3c0ccd9e-217c-487e-b406-6f537b22fb6f.png)

**노드를 스캔할 때 다음 조건 가운데 하나만 성립해도 검색 종료**
> 1. 검색 조건을 만족하는 노드를 발견하지 못하고 꼬리 노드까지 왔을 경우   
> 2. 검색 조건을 만족하는 노드를 발견한 경우

```python
    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    
    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는지 확인"""
        return self.search(data) >= 0
```

> * 스캔 중인 노드를 참조하기 위한 변수 ptr을 head로 초기화   
> * ptr이 참조하는 곳은 head가 참조하는 머리 노드A   
> * 카운터용 변수 cnt를 0으로 초기화

***

> * ptr 값이 None이 아니면 루프를 실행   
> * ptr 값이 None이면 스캔한 노드가 존재하지 않으므로 while문을 종료하고 return -1

***

> * 앞에서 정리한 종료 조건 2의 판단을 수행하며, 검색할 data와 스캔 중인 노드의 데이터 ptr.data와 값이 같은지 판단합니다.   
> * 주목 포인터 current에 ptr을 대입하고 찾은 노드의 위치를 나타내는 카운터 cnt를 반환

<br></br>

### 데이터가 포함되어 있는지 판단하는 \_\_contains\_\_() 함수
▶리스트에 data와 값이 같은 노드가 포함되어 있는지 판단하는 함수입니다. 포함되어 있으면 True를 반환하고, 그렇지 않으면 False를 반환합니다

<br></br>

### 머리에 노드를 삽입하는 add_first() 함수


```python
def add_first(self, data: Any) -> None:
    """맨 앞에 노드를 삽입"""
    ptr = self.head # 삽입하기 전의 머리 노드
    self.head = self.current = Node(data, ptr)
    self.no += 1
```

> * 삽입하기 전의 머리 노드 A를 참조하는 포인터를 ptr에 저장해둡니다.
> * 삽입할 노드 G를 Node(data, ptr)로 생성합니다. 노드 G의 데이터는 data가 되고, 뒤쪽 포인터가 참조하는 곳은 ptr(삽입하기 전의 머리 노드 A)이 됩니다.   
> * 이때 수행하는 대입으로 head는 삽입한 노드를 참조하도록 업데이트됩니다.

` 주목 포인터 current도 삽입한 노드를 참조하도록 업데이트됩니다(꼬리에 노드를 삽입하는 add_last() 함수에서도 마찬가지입니다).`

<br></br>

### 꼬리에 노드를 삽입하는 add_last() 함수
▶ 리스트의 맨 끝에 노드를 삽입하는 함수입니다. 리스트가 비어 있는지(head is None이 성립하는지) 확인하고 그에 따라 다르게 처리

> 1. **리스트가 비어 있을 때**   
> 맨 앞에 노드를 삽입하는 것과 같은 처리를 수행하므로 add_first() 함수를 호출합니다.
> 2. **리스트가 비어있지 않을 때**
> 리스트의 맨 끝에 노드 G를 삽입합니다.

```python
def add_last(self, data: Any):
    """맨 끝에 노드를 삽입"""
    if self.head is None:    # 리스트가 비어 있으면
        self.add_first(data) # 맨 앞에 노드를 삽입
    else:
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = self.current = Node(data, None)
        self.no += 1
```

***

> * 꼬리 노드를 찾는 과정을 수행
> * ptr이 참조하는 곳을 그 뒤쪽 포인터로 업데이트 하는 과정을 반복함으로써 노드를 만 앞부터 순서대로 스캔
> * while 문의 반복이 종료되는 것은 ptr.next가 참조하는 곳이 None으로 되었을 때.
`while 문을 종료할 때 ptr은 꼬리 노드를 참조` 
```python
while ptr.next is not None:
    ptr = ptr.next
ptr.next = self.current = Node(data, None)
self.no += 1
````

***

> * 삽입하는 노드 G를 Node(data, None)으로 생성합니다.
> * 뒤쪽 포인터를 None으로 하는 것은 맨 끝에 위치한 노드 G가 어떤 노드도 참조하지 않도록 하기 위한 것입니다.
> * 노드 F의 뒤쪽 포인터 ptr.next가 참조하는 곳이 새로 삽입한 노드 G가 되도록 업데이트 합니다.

```python
ptr.next = self.current = Node(data, None)
```
<br></br>
### 머리 노드를 삭제하는 remove_first() 함수
▶ 머리 노드를 삭제하는 함수. 삭제 처리를 수행하는 것은 리스트가 비어 있지 않을 (head is not None이 성립할) 때입니다.

```python
def remove_first(self) -> None:
    """머리 노드를 삭제"""
    if self.head is not None:    # 리스트가 비어 있지 않으면
        self.head = self.current = self.head.next
    self.no -= 1
```

`리스트에 노드가 하나밖에 없는 경우: 삭제하기 전의 머리 노드는 꼬리 노드이기도 하므로 뒤쪽 포인터 head.next의 값은 None입니다.
이 None을 대입하면 리스트는 빈 상태가 됩니다.`

<br></br>

### 꼬리 노드를 삭제하는 remove_last() 함수
▶ 꼬리 노드를 삭제하는 함수. 삭제 처리를 수행하는 것은 리스트가 비어 있지 않을 때입니다. 리스트에 존재하는 노드가 하나뿐인지 확인하고 그에 따라 다음과 같이 다르게 처리합니다.

> * 리스트에 노드가 하나만 존재할 때
> 머리 노드를 삭제하는 것이므로 remove_first() 함수를 호출합니다.
> * 리스트에 노드가 2개 이상 존재할 때
> 리스트의 맨 끝에서 노드를 삭제합니다.

```python
def remove_last(self):
    """꼬리 노드를 삭제"""
    if self.head is not None:
        if self.head.next is None:    # 노드가 1개 뿐이라면
            self.remove_first()       # 머리 노드를 삭제
        else:
            ptr = self.head           # 스캔 중인 노드
            pre = self.head           # 스캔 중인 노드의 앞쪽 노드
            
            while ptr.next is not None:
                pre = ptr
                ptr = ptr.next
            pre.next = None           # pre는 삭제 뒤 꼬리 노드
            self.current = pre
            self.no -= 1
```

***

```python
ptr = self.head           # 스캔 중인 노드
pre = self.head           # 스캔 중인 노드의 앞쪽 노드
          
while ptr.next is not None:
pre = ptr
ptr = ptr.next
```

> 꼬리 노드와 맨 끝에서 2번째 노드를 찾습니다. 따라서 스캔 방법은 앞에서 살펴본 add_last() 함수와 거의 같습니다.   
> 다만 스캔 중인 노드의 앞쪽 노드를 참조하는 변수 pre를 추가한 점이 다릅니다.

` 즉, while 문을 종료할 때 ptr은 꼬리 노드를 참조하고, pre는 맨 끝에서 2번째 노드를 참조합니다.`

***

```python
pre.next = None    # pre는 삭제 뒤 꼬리 노드
self.current = pre
self.no -= 1
```
> 맨 끝에서 2번째 노드의 뒤쪽 포인터에 None을 대입합니다. 그 결과 꼬리 노드는 어디에서도 참조되지 않습니다.

`주목 포인터 current가 참조하는 곳은 삭제한 뒤의 꼬리 노드 pre로 업데이트 합니다.`

<br></br>

### 임의의 노드를 삭제하는 remove() 함수
▶ 임의의 노드를 삭제하는 함수입니다. 삭제 처리를 수행하는 것은 리스트가 비어 있지 않고 인수로 주어진 노드 p(p가 참조하는 노드)가 존재할 때입니다.

> * p가 머리 노드일 때
> 머리 노드를 삭제하는 것이므로 remove_first() 함수를 호출합니다.
> * p가 머리노드가 아닐 때
> 리스트에서 p가 참조하는 노드를 삭제합니다.

```python
def remove(self, p: Node) -> None:
    """노드 p를 삭제"""
    if self.head is not None:
        if p is self.head:         # p가 머리 노드이면
            self.remove_first()    # 머리 노드를 삭제
        else:
            ptr = self.head

            while ptr.next is not p:
                ptr = ptr.next
                if ptr is None:
                    return         # ptr은 리스트에 존재하지 않음
            ptr.next = p.next
            self.current = ptr
            self.no -= 1

def remove_current_node(self) -> None:
    """주목 노드를 삭제"""
    self.remove(self.current)

def clear(self) -> None:
    """전체 노드를 삭제"""
    while self.head is not None:   # 전체가 비어 있을 때까지
        self.remove_first()        # 머리 노드를 삭제
    self.current = None
    self.no = 0

def next(self) -> bool:
    """주목 노드를 한 칸 뒤로 이동"""
    if self.current is None or self.current.next is None:
        return False               # 이동할 수 없음
    self.current = self.current.next
    return True
```

***

```python
            ptr = self.head

            while ptr.next is not p:
                ptr = ptr.next
                if ptr is None:
                    return         # ptr은 리스트에 존재하지 않음
```

> 삭제할 노드 p의 앞쪽 노드를 찾는 과정을 수행합니다.   
> while 문은 머리 노드에서 시작하여 스캔 중인 노드 ptr의 뒤쪽 포인터인 ptr.next가 p와 같아질 때까지 반복합니다.   
> 다만 None을 만나는 경우에는 p가 참조하는 노드가 존재하지 않는다는 것입니다.   
> 삭제 처리를 수행하지 않고 return문으로 함수를 종료합니다.   
> ptr.next가 p와 같아지면 while 문은 종료합니다.

***

```python
ptr.next = p.next
self.current = ptr
self.no -= 1
```

> 주목 노드의 뒤쪽 포인터 p.next를 앞쪽 노드의 뒤쪽 포인터 ptr.next에 대입함으로써 노드 C의 뒤쪽 포인터가 참조하는 곳을 뒤쪽 노드로 업데이트 합니다.   
> 그 결과 주목 노드는 어디에서도 참조되지 않습니다

`주목 포인터 current가 참조하는 곳은 삭제한 노드의 앞쪽 노드가 되도록 업데이트 합니다.`

<br></br>

### 주목 노드를 삭제하는 remove_current_node() 함수
▶ 현재 주목하고 있는 노드를 삭제하는 함수입니다. 주목 포인터 current를 remove() 함수에 전달하여 처리를 맡깁니다.

`주목 포인터 current가 참조하는 곳은 삭제한 노드의 앞쪽 노드로 업데이트 합니다.`

<br></br>

### 모든 노드를 삭제하는 clear() 함수
▶ 모든 노드를 삭제하는 함수입니다. 연결 리스트가 비어 있을 때(head가 None이 될 때)까지 머리 노드의 삭제를 반복하여 모든 노드를 삭제합니다.

```python
def clear(self) -> None:
    """전체 노드를 삭제"""
    while self.head is not None:   # 전체가 비어 있을 때까지
        self.remove_first()        # 머리 노드를 삭제
    self.current = None
    self.no = 0
```

***

`리스트가 비어 있으므로 주목 포인터 current의 값도 None으로 업데이트 합니다.`

<br></br>

### 주목 노드를 한 칸 뒤로 이동시키는 next() 함수
▶ 주목 노드를 한 칸 뒤쪽으로 이동시키는 함수입니다. 다만 주목 노드를 한 칸 뒤로 이동시키려면 리스트가 비어 있지 않고 주목 노드에 뒤쪽 노드가 존재해야 합니다.   
▶ 구체적으로는 주목 포인터 current를 current.next로 업데이트 합니다. 주목 노드를 이동시키면 True를 반환하고, 그렇지 않으면 False를 반환합니다.

```python
def next(self) -> bool:
    """주목 노드를 한 칸 뒤로 이동"""
    if self.current is None or self.current.next is None:
        return False               # 이동할 수 없음
    self.current = self.current.next
    return True
```

<br></br>

### 주목 노드를 출력하는 print_current_node() 함수
▶ 주목 노드를 출력하는 함수입니다. 구체적으로 주목 포인터 current가 참조하는 곳의 노드 데이터인 current.data를 출력합니다.   
▶ 다만 주목 노드가 존재하지 않는 경우(current가 None인 경우)에는 "주목 노드가 존재하지 않습니다."를 출력합니다.

```python
def print_current_node(self) -> None:
    """주목 노드를 출력"""
    if self.current is None:
        print("주목 노드가 존재하지 않습니다.")
    else:
        print(self.current.data)
```

<br></br>

### 모든 노드를 출력하는 print() 함수
▶ 리스트 순서대로 모든 노드의 데이터를 출력하는 함수입니다. ptr을 사용하여 머리 노드에서 꼬리 노드까지 스캔하면서 각 노드의 데이터 ptr.data를 출력합니다.

`print_current_node() 함수와 print() 함수는 주목 포인터 current 값을 업데이트 하지 않습니다.

```python
def print(self) -> None:
    """모든 노드를 출력"""
    ptr = self.head

    while ptr is not None:
        print(ptr.next)
        ptr = ptr.next
```

<br></br>

### ★ 이터러블 객체와 이터레이터의 구현 ★
▶ str형 문자열, list형 리스트, tuple형 튜플 등은 이터러블(반복가능)하다는 공통점이 있습니다.
> * **이터러블 객체**는 원소를 1개씩 꺼내는 구조의 객체입니다.   
> * 이터러블 객체를 내장 함수인 iter() 함수에 인수로 전달하면 그 객체에 대한 이터레이터(반복자)를 반환합니다.   
> * **이터레이터**는 데이터가 줄지어 늘어선 것을 표현하는 객체입니다. 이터레이터의 \_\_next\_\_() 함수를 호출하거나,   
>   내장 함수인 next() 함수에 반복자를 전달하면 줄지어 늘어선 원소를 순차적으로 꺼냅니다.
> * 꺼낼 원소가 없으면 StopIteration 예외 처리를 내보냅니다.

```python
def __iter__(self) -> LinkedListIterator:
        """이터레이터를 반환"""
        return LinkedListIterator(self.head)

class LinkedListIterator:
    """클래스 LinkedList의 이터레이터용 클래스"""

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
```

***

> 클래스 LinkedList는 이터러블이 되도록 이터레이터를 구현합니다. 이터레이터를 나타내는 것이 클래스 LinkedListIterator입니다.

```
● __next__() 함수를 갖는 이터레이터를 반환하는 __iter__() 함수를 구현합니다.
● __next__() 함수는 다음 원소를 꺼내 반환합니다. 반환하는 원소가 없으면 StopIteration 예외 처리를 내보냅니다.
```

<br></br>

***

## 포인터로 연결 리스트 프로그램 만들기

```python
# 포인터를 이용한 연결 리스트 클래스 LinkedList 사용하기

from enum import Enum
from linked_list import LinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
                     '꼬리노드삭제', '주목노드출력', '주목노드이동',
                     '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
                     '모든노드출력', '스캔', '종료'])

def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = LinkedList()                     # 연결 리스트를 생성

while True:
    menu = select_Menu()               # 메뉴를 선택
    
    if menu == Menu.머리에노드삽입:    # 맨 앞에 노드를 삽입
        lst.add_first(int(input("머리 노드에 넣을 값을 입력하세요.: ")))

    elif menu == Menu.꼬리에노드삽입:  # 맨 끝에 노드를 삽입
        lst.add_last(int(input("꼬리 노드에 넣을 값을 입력하세요.: ")))
    
    elif menu == Menu.머리노드삭제:    # 맨 앞에 노드를 삭제
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:    # 맨 끝에 노드를 삭제
        lst.remove_last()
    
    elif menu == Menu.주목노드출력:    # 주목 노드를 출력
        lst.print_current_node()

    elif menu == Menu.주목노드이동:    # 주목 노드를 한 칸 뒤로 이동
        lst.next()

    elif menu == Menu.주목노드삭제:    # 주목 노드를 삭제
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:    # 모든 노드를 삭제
        lst.clear()

    elif menu == Menu.검색:            # 노드를 검색
        pos = lst.search(int(input("검색할 값을 입력하세요.: ")))
        if pos >= 0:
            print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print("해당하는 데이터가 없습니다.")
    
    elif menu == Menu.멤버십판단:      # 멤버십을 판단
        print("그 값의 데이터는 포함되어"
              + (" 있습니다." if int(input("판단할 값을 입력하세요.: ")) in lst
              else "있지 않습니다."))
    
    elif menu == Menu.모든노드출력:    # 모든 노드를 출력
        lst.print()

    elif menu == Menu.스캔:            # 모든 노드를 스캔
        for e in lst:
            print(e)

    else:                              # 종료
        break
```

## 커서를 이용한 연결리스트
