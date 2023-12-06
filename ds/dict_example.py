"""
创建
1、大括号
2、内建函数
3、 fromkeys()，从序列建立，默认为None，可指定
"""
d = dict()
d = {'a': 1, 'b': 2}

"""
获取
1、dict[key]，不存在KeyError
2、dict.get(key)，不存在返回None
"""
print(d.get('c'))
print(d.get('c', 'hello'))
# print(d['c'])


"""
新增或更新
1、字典[key]赋值
2、dict.setdefault(key),不存在则设置None
3、update批量更新
"""
d['c'] = 3
d['c'] = 4
d.setdefault('c', 666)
d.setdefault('d', 666)
d.setdefault('f')
d2 = {'aa': 11, 'bb': 22}
d.update(d2)
print(d)

"""
如果键在字典dict里返回true，否则返回false
"""
if 'c' in d:
    print("yes")

"""
删除
1、del d[key]
2、pop删除并返回值
"""
del d['f']
print(d.pop('a'))
print(d)
print(d.popitem())

"""
遍历
1、keys
2、values
3、item
"""
for k, v in d.items():
    print(k, v)

print(d.keys())
print(d.values())

from collections import OrderedDict  # 有序字典

od = OrderedDict()
od.setdefault('d', 4)
od.setdefault('a', 1)
od.setdefault('c', 3)

print(od)

from collections import deque  # 双端队列

d = deque()
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.appendleft(1)
d.pop()
d.popleft()
print(d)

import heapq  # 优先队列，heapify或heappush创建，heapqpop取出

array1 = [4, 2, 5, 1, 3]

array2 = []
for i in array1:
    heapq.heappush(array2, i)

print(array2)
print(array1)
heapq.heapify(array1)
print(array1)

array1.pop()
heapq.heappop(array1)
print(array1)

max = float("-inf")  # 负无穷
min = float("inf")  # 正无穷
print(max)
print(min)
print(1 > max)
