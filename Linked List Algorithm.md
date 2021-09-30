# 리스트 알고리즘
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

## 포인터를 이용한 연결리스트
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

<br>
</br>

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

### 초기화하는 \_\_init_\_() 함수
연결 리스트 클래스 LinkedList의 \_\_init()\_\_ 함수는 노드가 하나도 없는 빈 연결 리스트를 생성합니다.
- 머리 노드를 참조하기 위한 Node형 필드 head에 None을 대입합니다.
- head는 머리 노드에 대한 참조일뿐 머리 노드 그 자체가 아님을 주의
- 노드가 존재하지 않는 빈 연결리스트는 head가 참조하는 곳이 없으므로 **(참조해야 하는 노드가 존재하지 않으므로)** 그 값을 None으로 합니다.

### 노드 개수를 반환하는 \_\_len\_\_() 함수
연결 리스트의 노드 개수를 반환하는 함수입니다. no값을 그대로 반환합니다.

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

