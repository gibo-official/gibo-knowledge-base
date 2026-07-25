---
lang: zh-CN
category: 仓库文档
title: "video-generation-integration-plan"
summary: "最后更新：2026-07-14"
updated: 2026-07-14
product: ""
tags: ["GIBO", "洁博利", "仓库文档", "AI知识库"]
---

#
 
视
频
生
成
A
P
I
集
成
方
案
 
—
 
P
F
B
C
-
5
9




*
*
文
档
版
本
*
*
：
V
1
.
0


*
*
最
后
更
新
*
*
：
2
0
2
6
-
0
7
-
1
4


*
*
适
用
范
围
*
*
：
品
牌
展
示
、
产
品
展
示
、
投
标
材
料
、
行
业
研
究
、
A
I
知
识
库
引
用




*
*
创
建
日
期
*
*
:
 
2
0
2
6
-
0
6
-
0
6
 
 


*
*
负
责
人
*
*
:
 
平
台
工
程
师
 
 


*
*
目
标
*
*
:
 
在
P
a
p
e
r
c
l
i
p
平
台
上
接
入
视
频
生
成
模
型
A
P
I
，
使
a
g
e
n
t
具
备
A
I
视
频
生
成
能
力




-
-
-




#
#
 
一
、
A
P
I
选
型
对
比




|
 
维
度
 
|
 
可
灵
 
K
l
i
n
g
 
A
I
 
|
 
R
u
n
w
a
y
 
G
e
n
-
3
 
A
l
p
h
a
 
|
 
L
u
m
a
 
D
r
e
a
m
 
M
a
c
h
i
n
e
 
|
 
P
i
k
a
 
2
.
0
 
|


|
-
-
-
-
-
-
|
-
-
-
-
-
-
-
-
-
-
-
-
-
-
|
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
|
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
|
-
-
-
-
-
-
-
-
-
|


|
 
*
*
地
区
*
*
 
|
 
🇨
🇳
 
中
国
 
|
 
🇺
🇸
 
美
国
 
|
 
🇺
🇸
 
美
国
 
|
 
🇺
🇸
 
美
国
 
|


|
 
*
*
中
国
可
访
问
*
*
 
|
 
✅
 
直
接
访
问
 
|
 
⚠
️
 
需
代
理
 
|
 
⚠
️
 
需
代
理
 
|
 
⚠
️
 
需
代
理
 
|


|
 
*
*
A
P
I
支
持
*
*
 
|
 
✅
 
有
A
P
I
 
|
 
✅
 
有
A
P
I
 
|
 
✅
 
有
A
P
I
 
|
 
✅
 
有
A
P
I
 
|


|
 
*
*
中
文
提
示
词
*
*
 
|
 
✅
 
原
生
支
持
 
|
 
⚠
️
 
有
限
支
持
 
|
 
⚠
️
 
有
限
支
持
 
|
 
⚠
️
 
有
限
支
持
 
|


|
 
*
*
分
辨
率
*
*
 
|
 
7
2
0
p
/
1
0
8
0
p
 
|
 
最
高
1
0
8
0
p
 
|
 
最
高
1
0
8
0
p
 
|
 
1
0
8
0
p
 
|


|
 
*
*
最
大
时
长
*
*
 
|
 
1
0
秒
 
(
1
.
0
)
 
/
 
5
秒
 
(
1
.
5
)
 
|
 
1
0
秒
 
|
 
5
秒
 
|
 
3
-
5
秒
 
|


|
 
*
*
无
水
印
*
*
 
|
 
✅
 
支
持
 
|
 
✅
 
支
持
 
|
 
✅
 
支
持
 
|
 
✅
 
P
r
o
计
划
 
|


|
 
*
*
定
价
模
式
*
*
 
|
 
积
分
制
 
|
 
月
费
/
按
量
 
|
 
按
量
计
费
 
|
 
月
费
 
|


|
 
*
*
性
价
比
*
*
 
|
 
⭐
⭐
⭐
⭐
⭐
 
|
 
⭐
⭐
⭐
⭐
 
|
 
⭐
⭐
⭐
 
|
 
⭐
⭐
⭐
 
|




#
#
#
 
推
荐
方
案




*
*
首
选
：
可
灵
 
K
l
i
n
g
 
A
P
I
*
*
 
🇨
🇳


-
 
中
国
区
直
接
可
访
问
，
无
需
特
殊
网
络


-
 
原
生
中
文
提
示
词
支
持
，
适
合
洁
博
利
品
牌
视
频


-
 
A
P
I
定
价
合
理
，
积
分
制
灵
活


-
 
1
.
0
版
本
支
持
1
0
秒
视
频
，
1
.
5
版
本
画
质
更
好
（
5
秒
）


-
 
支
持
图
生
视
频
（
I
m
a
g
e
-
t
o
-
V
i
d
e
o
）




*
*
备
选
：
R
u
n
w
a
y
 
G
e
n
-
3
 
A
l
p
h
a
*
*
 
🌐


-
 
视
频
质
量
业
界
领
先


-
 
需
要
A
P
I
 
K
e
y
和
网
络
配
置


-
 
适
合
高
质
量
品
牌
宣
传
片




-
-
-




#
#
 
二
、
架
构
设
计




`
`
`


┌
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
┐


│
 
 
P
a
p
e
r
c
l
i
p
 
A
g
e
n
t
 
│


│
 
 
(
C
l
a
u
d
e
 
C
L
I
)
 
 
 
 
│


└
─
─
─
─
─
─
─
─
┬
─
─
─
─
─
─
─
─
┘


 
 
 
 
 
 
 
 
 
│
 
调
用
 
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y


 
 
 
 
 
 
 
 
 
▼


┌
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
┐


│
 
 
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y
 
 
 
 
 
 
│


│
 
 
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
 
 
 
│


│
 
 
-
 
A
P
I
认
证
管
理
 
 
 
 
 
 
 
 
 
 
 
│


│
 
 
-
 
视
频
生
成
请
求
 
 
 
 
 
 
 
 
 
 
 
│


│
 
 
-
 
任
务
状
态
轮
询
 
 
 
 
 
 
 
 
 
 
 
│


│
 
 
-
 
结
果
下
载
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
│


│
 
 
-
 
错
误
重
试
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
│


└
─
─
─
─
─
─
─
─
┬
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
┘


 
 
 
 
 
 
 
 
 
│
 
H
T
T
P
请
求


 
 
 
 
 
 
 
 
 
▼


┌
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
┐


│
 
 
K
l
i
n
g
 
A
P
I
 
/
 
R
u
n
w
a
y
 
A
P
I
 
 
│


│
 
 
(
云
端
视
频
生
成
服
务
)
 
 
 
 
 
 
 
│


└
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
┘


 
 
 
 
 
 
 
 
 
│
 
文
件
输
出


 
 
 
 
 
 
 
 
 
▼


┌
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
┐


│
 
 
.
/
o
u
t
p
u
t
/
v
i
d
e
o
/
 
 
 
 
 
 
 
 
 
│


│
 
 
生
成
结
果
存
储
目
录
 
 
 
 
 
 
 
 
 
│


└
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
┘


`
`
`




-
-
-




#
#
 
三
、
A
P
I
密
钥
配
置




在
P
a
p
e
r
c
l
i
p
环
境
变
量
中
配
置
：




`
`
`
b
a
s
h


#
 
可
灵
 
K
l
i
n
g
 
A
P
I
 
(
J
W
T
认
证
方
式
)


e
x
p
o
r
t
 
K
L
I
N
G
_
A
K
=
"
y
o
u
r
_
a
c
c
e
s
s
_
k
e
y
"


e
x
p
o
r
t
 
K
L
I
N
G
_
S
K
=
"
y
o
u
r
_
s
e
c
r
e
t
_
k
e
y
"


`
`
`




>
 
*
*
⚠
️
 
2
0
2
6
年
6
月
验
证
发
现
*
*
:


>
 
-
 
A
P
I
主
机
:
 
`
o
p
e
n
a
p
i
.
k
l
i
n
g
a
i
.
c
o
m
`
（
不
是
 
`
a
p
i
.
k
l
i
n
g
a
i
.
c
o
m
`
）


>
 
-
 
认
证
方
式
:
 
J
W
T
 
H
S
2
5
6
 
T
o
k
e
n
（
`
A
u
t
h
o
r
i
z
a
t
i
o
n
:
 
B
e
a
r
e
r
 
{
j
w
t
}
`
）


>
 
-
 
端
点
:
 
`
P
O
S
T
 
/
v
1
/
v
i
d
e
o
s
/
t
e
x
t
2
v
i
d
e
o
`
（
文
本
生
视
频
）


>
 
-
 
环
境
变
量
:
 
推
荐
统
一
使
用
 
`
K
L
I
N
G
_
A
K
`
 
/
 
`
K
L
I
N
G
_
S
K
`


>
 
-
 
P
y
t
h
o
n
包
装
器
也
兼
容
 
`
K
L
I
N
G
_
A
C
C
E
S
S
_
K
E
Y
`
 
/
 
`
K
L
I
N
G
_
S
E
C
R
E
T
_
K
E
Y
`




K
l
i
n
g
 
A
P
I
密
钥
申
请
:
 
h
t
t
p
s
:
/
/
c
o
n
s
o
l
e
.
k
l
i
n
g
a
i
.
c
o
m
 
(
需
要
注
册
开
发
者
账
号
)




-
-
-




#
#
 
四
、
P
y
t
h
o
n
包
装
器
实
现




`
`
`
p
y
t
h
o
n


#
!
/
u
s
r
/
b
i
n
/
e
n
v
 
p
y
t
h
o
n
3


"
"
"


V
i
d
e
o
 
G
e
n
e
r
a
t
i
o
n
 
A
P
I
 
W
r
a
p
p
e
r
 
f
o
r
 
P
a
p
e
r
c
l
i
p
 
P
l
a
t
f
o
r
m


S
u
p
p
o
r
t
s
:
 
K
l
i
n
g
 
A
I
 
(
p
r
i
m
a
r
y
)
,
 
R
u
n
w
a
y
 
G
e
n
-
3
 
(
f
a
l
l
b
a
c
k
)




U
s
a
g
e
:


 
 
 
 
p
y
t
h
o
n
 
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y
 
-
-
p
r
o
m
p
t
 
"
A
 
b
r
a
n
d
 
v
i
d
e
o
 
a
b
o
u
t
 
s
m
a
r
t
 
s
e
n
s
o
r
 
f
a
u
c
e
t
s
"
 
-
-
d
u
r
a
t
i
o
n
 
5


 
 
 
 
p
y
t
h
o
n
 
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y
 
-
-
p
r
o
m
p
t
 
"
.
.
.
"
 
-
-
m
o
d
e
l
 
k
l
i
n
g
 
-
-
o
u
t
p
u
t
 
.
/
o
u
t
p
u
t
/
v
i
d
e
o
/


 
 
 
 
p
y
t
h
o
n
 
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y
 
-
-
i
m
a
g
e
 
i
n
p
u
t
.
p
n
g
 
-
-
p
r
o
m
p
t
 
"
a
n
i
m
a
t
e
 
t
h
i
s
 
p
r
o
d
u
c
t
"
 
 
#
 
i
m
a
g
e
-
t
o
-
v
i
d
e
o


"
"
"




i
m
p
o
r
t
 
o
s


i
m
p
o
r
t
 
s
y
s


i
m
p
o
r
t
 
j
s
o
n


i
m
p
o
r
t
 
t
i
m
e


i
m
p
o
r
t
 
h
a
s
h
l
i
b


i
m
p
o
r
t
 
h
m
a
c


i
m
p
o
r
t
 
b
a
s
e
6
4


i
m
p
o
r
t
 
u
u
i
d


i
m
p
o
r
t
 
r
e
q
u
e
s
t
s


f
r
o
m
 
p
a
t
h
l
i
b
 
i
m
p
o
r
t
 
P
a
t
h


f
r
o
m
 
t
y
p
i
n
g
 
i
m
p
o
r
t
 
O
p
t
i
o
n
a
l
,
 
D
i
c
t
,
 
A
n
y




#
 
─
─
─
 
C
o
n
f
i
g
u
r
a
t
i
o
n
 
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─




K
L
I
N
G
_
A
C
C
E
S
S
_
K
E
Y
 
=
 
o
s
.
e
n
v
i
r
o
n
.
g
e
t
(
"
K
L
I
N
G
_
A
C
C
E
S
S
_
K
E
Y
"
,
 
"
"
)


K
L
I
N
G
_
S
E
C
R
E
T
_
K
E
Y
 
=
 
o
s
.
e
n
v
i
r
o
n
.
g
e
t
(
"
K
L
I
N
G
_
S
E
C
R
E
T
_
K
E
Y
"
,
 
"
"
)


R
U
N
W
A
Y
_
A
P
I
_
K
E
Y
 
=
 
o
s
.
e
n
v
i
r
o
n
.
g
e
t
(
"
R
U
N
W
A
Y
_
A
P
I
_
K
E
Y
"
,
 
"
"
)




D
E
F
A
U
L
T
_
O
U
T
P
U
T
_
D
I
R
 
=
 
P
a
t
h
(
"
.
/
o
u
t
p
u
t
/
v
i
d
e
o
"
)


D
E
F
A
U
L
T
_
M
O
D
E
L
 
=
 
"
k
l
i
n
g
"
 
 
#
 
k
l
i
n
g
 
o
r
 
r
u
n
w
a
y


D
E
F
A
U
L
T
_
D
U
R
A
T
I
O
N
 
=
 
5
 
 
 
 
 
#
 
s
e
c
o
n
d
s




#
 
─
─
─
 
K
l
i
n
g
 
A
P
I
 
C
l
i
e
n
t
 
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─




c
l
a
s
s
 
K
l
i
n
g
C
l
i
e
n
t
:


 
 
 
 
"
"
"
K
l
i
n
g
 
A
I
 
V
i
d
e
o
 
G
e
n
e
r
a
t
i
o
n
 
A
P
I
 
C
l
i
e
n
t
"
"
"


 
 
 
 


 
 
 
 
B
A
S
E
_
U
R
L
 
=
 
"
h
t
t
p
s
:
/
/
a
p
i
.
k
l
i
n
g
a
i
.
c
o
m
"


 
 
 
 


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
a
c
c
e
s
s
_
k
e
y
:
 
s
t
r
,
 
s
e
c
r
e
t
_
k
e
y
:
 
s
t
r
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
a
c
c
e
s
s
_
k
e
y
 
=
 
a
c
c
e
s
s
_
k
e
y


 
 
 
 
 
 
 
 
s
e
l
f
.
s
e
c
r
e
t
_
k
e
y
 
=
 
s
e
c
r
e
t
_
k
e
y


 
 
 
 


 
 
 
 
d
e
f
 
_
g
e
n
e
r
a
t
e
_
s
i
g
n
a
t
u
r
e
(
s
e
l
f
,
 
m
e
t
h
o
d
:
 
s
t
r
,
 
p
a
t
h
:
 
s
t
r
,
 
b
o
d
y
:
 
s
t
r
 
=
 
"
"
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
s
t
r
]
:


 
 
 
 
 
 
 
 
"
"
"
G
e
n
e
r
a
t
e
 
H
M
A
C
-
S
H
A
2
5
6
 
s
i
g
n
a
t
u
r
e
 
f
o
r
 
K
l
i
n
g
 
A
P
I
 
a
u
t
h
e
n
t
i
c
a
t
i
o
n
"
"
"


 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
 
=
 
i
n
t
(
t
i
m
e
.
t
i
m
e
(
)
)


 
 
 
 
 
 
 
 
n
o
n
c
e
 
=
 
u
u
i
d
.
u
u
i
d
4
(
)
.
h
e
x
[
:
1
6
]


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
#
 
B
u
i
l
d
 
s
i
g
n
a
t
u
r
e
 
s
t
r
i
n
g


 
 
 
 
 
 
 
 
s
i
g
n
_
s
t
r
 
=
 
f
"
{
m
e
t
h
o
d
}
\
n
{
p
a
t
h
}
\
n
{
t
i
m
e
s
t
a
m
p
}
\
n
{
n
o
n
c
e
}
\
n
{
b
o
d
y
}
\
n
"


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
#
 
C
o
m
p
u
t
e
 
H
M
A
C
-
S
H
A
2
5
6


 
 
 
 
 
 
 
 
s
i
g
n
a
t
u
r
e
 
=
 
h
m
a
c
.
n
e
w
(


 
 
 
 
 
 
 
 
 
 
 
 
s
e
l
f
.
s
e
c
r
e
t
_
k
e
y
.
e
n
c
o
d
e
(
'
u
t
f
-
8
'
)
,


 
 
 
 
 
 
 
 
 
 
 
 
s
i
g
n
_
s
t
r
.
e
n
c
o
d
e
(
'
u
t
f
-
8
'
)
,


 
 
 
 
 
 
 
 
 
 
 
 
h
a
s
h
l
i
b
.
s
h
a
2
5
6


 
 
 
 
 
 
 
 
)
.
d
i
g
e
s
t
(
)


 
 
 
 
 
 
 
 
s
i
g
n
a
t
u
r
e
_
b
6
4
 
=
 
b
a
s
e
6
4
.
b
6
4
e
n
c
o
d
e
(
s
i
g
n
a
t
u
r
e
)
.
d
e
c
o
d
e
(
'
u
t
f
-
8
'
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
{


 
 
 
 
 
 
 
 
 
 
 
 
"
C
o
n
t
e
n
t
-
T
y
p
e
"
:
 
"
a
p
p
l
i
c
a
t
i
o
n
/
j
s
o
n
"
,


 
 
 
 
 
 
 
 
 
 
 
 
"
A
K
"
:
 
s
e
l
f
.
a
c
c
e
s
s
_
k
e
y
,


 
 
 
 
 
 
 
 
 
 
 
 
"
S
i
g
n
a
t
u
r
e
"
:
 
s
i
g
n
a
t
u
r
e
_
b
6
4
,


 
 
 
 
 
 
 
 
 
 
 
 
"
T
i
m
e
s
t
a
m
p
"
:
 
s
t
r
(
t
i
m
e
s
t
a
m
p
)
,


 
 
 
 
 
 
 
 
 
 
 
 
"
N
o
n
c
e
"
:
 
n
o
n
c
e
,


 
 
 
 
 
 
 
 
}


 
 
 
 


 
 
 
 
d
e
f
 
g
e
n
e
r
a
t
e
_
v
i
d
e
o
(


 
 
 
 
 
 
 
 
s
e
l
f
,


 
 
 
 
 
 
 
 
p
r
o
m
p
t
:
 
s
t
r
,


 
 
 
 
 
 
 
 
m
o
d
e
l
_
n
a
m
e
:
 
s
t
r
 
=
 
"
k
l
i
n
g
-
v
1
"
,


 
 
 
 
 
 
 
 
d
u
r
a
t
i
o
n
:
 
i
n
t
 
=
 
5
,


 
 
 
 
 
 
 
 
m
o
d
e
:
 
s
t
r
 
=
 
"
p
r
o
"
,
 
 
#
 
p
r
o
 
o
r
 
s
t
d


 
 
 
 
 
 
 
 
i
m
a
g
e
:
 
O
p
t
i
o
n
a
l
[
s
t
r
]
 
=
 
N
o
n
e
,


 
 
 
 
 
 
 
 
n
e
g
a
t
i
v
e
_
p
r
o
m
p
t
:
 
O
p
t
i
o
n
a
l
[
s
t
r
]
 
=
 
N
o
n
e
,


 
 
 
 
 
 
 
 
c
f
g
_
s
c
a
l
e
:
 
f
l
o
a
t
 
=
 
0
.
5
,


 
 
 
 
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
G
e
n
e
r
a
t
e
 
v
i
d
e
o
 
u
s
i
n
g
 
K
l
i
n
g
 
A
P
I


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
 
 
 
 
p
r
o
m
p
t
:
 
T
e
x
t
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f
 
t
h
e
 
v
i
d
e
o


 
 
 
 
 
 
 
 
 
 
 
 
m
o
d
e
l
_
n
a
m
e
:
 
M
o
d
e
l
 
v
e
r
s
i
o
n
 
(
k
l
i
n
g
-
v
1
,
 
k
l
i
n
g
-
v
1
.
5
)


 
 
 
 
 
 
 
 
 
 
 
 
d
u
r
a
t
i
o
n
:
 
V
i
d
e
o
 
d
u
r
a
t
i
o
n
 
i
n
 
s
e
c
o
n
d
s
 
(
5
 
o
r
 
1
0
)


 
 
 
 
 
 
 
 
 
 
 
 
m
o
d
e
:
 
'
p
r
o
'
 
f
o
r
 
h
i
g
h
e
r
 
q
u
a
l
i
t
y
,
 
'
s
t
d
'
 
f
o
r
 
s
t
a
n
d
a
r
d


 
 
 
 
 
 
 
 
 
 
 
 
i
m
a
g
e
:
 
P
a
t
h
 
t
o
 
i
n
p
u
t
 
i
m
a
g
e
 
f
o
r
 
i
m
a
g
e
-
t
o
-
v
i
d
e
o


 
 
 
 
 
 
 
 
 
 
 
 
n
e
g
a
t
i
v
e
_
p
r
o
m
p
t
:
 
W
h
a
t
 
t
o
 
a
v
o
i
d
 
i
n
 
g
e
n
e
r
a
t
i
o
n


 
 
 
 
 
 
 
 
 
 
 
 
c
f
g
_
s
c
a
l
e
:
 
P
r
o
m
p
t
 
a
d
h
e
r
e
n
c
e
 
(
0
-
1
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
 
 
 
 
A
P
I
 
r
e
s
p
o
n
s
e
 
w
i
t
h
 
t
a
s
k
_
i
d


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
a
t
h
 
=
 
"
/
v
1
/
v
i
d
e
o
s
/
g
e
n
e
r
a
t
e
"


 
 
 
 
 
 
 
 
u
r
l
 
=
 
f
"
{
s
e
l
f
.
B
A
S
E
_
U
R
L
}
{
p
a
t
h
}
"


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
p
a
y
l
o
a
d
 
=
 
{


 
 
 
 
 
 
 
 
 
 
 
 
"
m
o
d
e
l
_
n
a
m
e
"
:
 
m
o
d
e
l
_
n
a
m
e
,


 
 
 
 
 
 
 
 
 
 
 
 
"
p
r
o
m
p
t
"
:
 
p
r
o
m
p
t
,


 
 
 
 
 
 
 
 
 
 
 
 
"
d
u
r
a
t
i
o
n
"
:
 
d
u
r
a
t
i
o
n
,


 
 
 
 
 
 
 
 
 
 
 
 
"
m
o
d
e
"
:
 
m
o
d
e
,


 
 
 
 
 
 
 
 
 
 
 
 
"
c
f
g
_
s
c
a
l
e
"
:
 
c
f
g
_
s
c
a
l
e
,


 
 
 
 
 
 
 
 
}


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
i
f
 
n
e
g
a
t
i
v
e
_
p
r
o
m
p
t
:


 
 
 
 
 
 
 
 
 
 
 
 
p
a
y
l
o
a
d
[
"
n
e
g
a
t
i
v
e
_
p
r
o
m
p
t
"
]
 
=
 
n
e
g
a
t
i
v
e
_
p
r
o
m
p
t


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
i
f
 
i
m
a
g
e
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
I
m
a
g
e
-
t
o
-
v
i
d
e
o
:
 
u
p
l
o
a
d
 
i
m
a
g
e
 
f
i
r
s
t
,
 
t
h
e
n
 
r
e
f
e
r
e
n
c
e


 
 
 
 
 
 
 
 
 
 
 
 
i
m
a
g
e
_
u
r
l
 
=
 
s
e
l
f
.
_
u
p
l
o
a
d
_
i
m
a
g
e
(
i
m
a
g
e
)


 
 
 
 
 
 
 
 
 
 
 
 
p
a
y
l
o
a
d
[
"
i
m
a
g
e
"
]
 
=
 
i
m
a
g
e
_
u
r
l


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
b
o
d
y
 
=
 
j
s
o
n
.
d
u
m
p
s
(
p
a
y
l
o
a
d
)


 
 
 
 
 
 
 
 
h
e
a
d
e
r
s
 
=
 
s
e
l
f
.
_
g
e
n
e
r
a
t
e
_
s
i
g
n
a
t
u
r
e
(
"
P
O
S
T
"
,
 
p
a
t
h
,
 
b
o
d
y
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
e
s
p
o
n
s
e
 
=
 
r
e
q
u
e
s
t
s
.
p
o
s
t
(
u
r
l
,
 
h
e
a
d
e
r
s
=
h
e
a
d
e
r
s
,
 
d
a
t
a
=
b
o
d
y
,
 
t
i
m
e
o
u
t
=
3
0
)


 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
r
e
s
p
o
n
s
e
.
j
s
o
n
(
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
i
f
 
r
e
s
u
l
t
.
g
e
t
(
"
c
o
d
e
"
)
 
!
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
E
x
c
e
p
t
i
o
n
(
f
"
K
l
i
n
g
 
A
P
I
 
e
r
r
o
r
:
 
{
r
e
s
u
l
t
.
g
e
t
(
'
m
e
s
s
a
g
e
'
,
 
'
U
n
k
n
o
w
n
 
e
r
r
o
r
'
)
}
"
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t
[
"
d
a
t
a
"
]


 
 
 
 


 
 
 
 
d
e
f
 
q
u
e
r
y
_
t
a
s
k
(
s
e
l
f
,
 
t
a
s
k
_
i
d
:
 
s
t
r
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
 
 
 
 
"
"
"
Q
u
e
r
y
 
v
i
d
e
o
 
g
e
n
e
r
a
t
i
o
n
 
t
a
s
k
 
s
t
a
t
u
s
"
"
"


 
 
 
 
 
 
 
 
p
a
t
h
 
=
 
f
"
/
v
1
/
v
i
d
e
o
s
/
{
t
a
s
k
_
i
d
}
"


 
 
 
 
 
 
 
 
u
r
l
 
=
 
f
"
{
s
e
l
f
.
B
A
S
E
_
U
R
L
}
{
p
a
t
h
}
"


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
h
e
a
d
e
r
s
 
=
 
s
e
l
f
.
_
g
e
n
e
r
a
t
e
_
s
i
g
n
a
t
u
r
e
(
"
G
E
T
"
,
 
p
a
t
h
)


 
 
 
 
 
 
 
 
r
e
s
p
o
n
s
e
 
=
 
r
e
q
u
e
s
t
s
.
g
e
t
(
u
r
l
,
 
h
e
a
d
e
r
s
=
h
e
a
d
e
r
s
,
 
t
i
m
e
o
u
t
=
1
5
)


 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
r
e
s
p
o
n
s
e
.
j
s
o
n
(
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
i
f
 
r
e
s
u
l
t
.
g
e
t
(
"
c
o
d
e
"
)
 
!
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
E
x
c
e
p
t
i
o
n
(
f
"
K
l
i
n
g
 
q
u
e
r
y
 
e
r
r
o
r
:
 
{
r
e
s
u
l
t
.
g
e
t
(
'
m
e
s
s
a
g
e
'
,
 
'
U
n
k
n
o
w
n
 
e
r
r
o
r
'
)
}
"
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t
[
"
d
a
t
a
"
]


 
 
 
 


 
 
 
 
d
e
f
 
w
a
i
t
_
f
o
r
_
c
o
m
p
l
e
t
i
o
n
(


 
 
 
 
 
 
 
 
s
e
l
f
,


 
 
 
 
 
 
 
 
t
a
s
k
_
i
d
:
 
s
t
r
,


 
 
 
 
 
 
 
 
p
o
l
l
_
i
n
t
e
r
v
a
l
:
 
i
n
t
 
=
 
5
,


 
 
 
 
 
 
 
 
t
i
m
e
o
u
t
:
 
i
n
t
 
=
 
6
0
0
,


 
 
 
 
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
 
 
 
 
"
"
"
P
o
l
l
 
u
n
t
i
l
 
v
i
d
e
o
 
g
e
n
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
e
s
"
"
"


 
 
 
 
 
 
 
 
s
t
a
r
t
 
=
 
t
i
m
e
.
t
i
m
e
(
)


 
 
 
 
 
 
 
 
w
h
i
l
e
 
t
i
m
e
.
t
i
m
e
(
)
 
-
 
s
t
a
r
t
 
<
 
t
i
m
e
o
u
t
:


 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
 
=
 
s
e
l
f
.
q
u
e
r
y
_
t
a
s
k
(
t
a
s
k
_
i
d
)


 
 
 
 
 
 
 
 
 
 
 
 
s
t
a
t
u
s
 
=
 
d
a
t
a
.
g
e
t
(
"
s
t
a
t
u
s
"
,
 
"
"
)


 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
s
t
a
t
u
s
 
=
=
 
"
s
u
c
c
e
e
d
"
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
a
t
a


 
 
 
 
 
 
 
 
 
 
 
 
e
l
i
f
 
s
t
a
t
u
s
 
=
=
 
"
f
a
i
l
e
d
"
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
E
x
c
e
p
t
i
o
n
(
f
"
V
i
d
e
o
 
g
e
n
e
r
a
t
i
o
n
 
f
a
i
l
e
d
:
 
{
d
a
t
a
.
g
e
t
(
'
f
a
i
l
_
r
e
a
s
o
n
'
,
 
'
U
n
k
n
o
w
n
'
)
}
"
)


 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
#
 
"
p
r
o
c
e
s
s
i
n
g
"
 
o
r
 
"
p
e
n
d
i
n
g
"
 
-
 
k
e
e
p
 
w
a
i
t
i
n
g


 
 
 
 
 
 
 
 
 
 
 
 
t
i
m
e
.
s
l
e
e
p
(
p
o
l
l
_
i
n
t
e
r
v
a
l
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
 
T
i
m
e
o
u
t
E
r
r
o
r
(
f
"
V
i
d
e
o
 
g
e
n
e
r
a
t
i
o
n
 
t
i
m
e
d
 
o
u
t
 
a
f
t
e
r
 
{
t
i
m
e
o
u
t
}
s
"
)


 
 
 
 


 
 
 
 
d
e
f
 
_
u
p
l
o
a
d
_
i
m
a
g
e
(
s
e
l
f
,
 
i
m
a
g
e
_
p
a
t
h
:
 
s
t
r
)
 
-
>
 
s
t
r
:


 
 
 
 
 
 
 
 
"
"
"
U
p
l
o
a
d
 
i
m
a
g
e
 
f
o
r
 
i
m
a
g
e
-
t
o
-
v
i
d
e
o
 
g
e
n
e
r
a
t
i
o
n
"
"
"


 
 
 
 
 
 
 
 
p
a
t
h
 
=
 
"
/
v
1
/
f
i
l
e
s
/
u
p
l
o
a
d
"


 
 
 
 
 
 
 
 
u
r
l
 
=
 
f
"
{
s
e
l
f
.
B
A
S
E
_
U
R
L
}
{
p
a
t
h
}
"


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
f
i
l
e
_
n
a
m
e
 
=
 
P
a
t
h
(
i
m
a
g
e
_
p
a
t
h
)
.
n
a
m
e


 
 
 
 
 
 
 
 
h
e
a
d
e
r
s
 
=
 
s
e
l
f
.
_
g
e
n
e
r
a
t
e
_
s
i
g
n
a
t
u
r
e
(
"
P
O
S
T
"
,
 
p
a
t
h
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
w
i
t
h
 
o
p
e
n
(
i
m
a
g
e
_
p
a
t
h
,
 
"
r
b
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
e
s
 
=
 
{
"
f
i
l
e
"
:
 
(
f
i
l
e
_
n
a
m
e
,
 
f
,
 
"
i
m
a
g
e
/
p
n
g
"
)
}


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
p
o
n
s
e
 
=
 
r
e
q
u
e
s
t
s
.
p
o
s
t
(
u
r
l
,
 
h
e
a
d
e
r
s
=
h
e
a
d
e
r
s
,
 
f
i
l
e
s
=
f
i
l
e
s
,
 
t
i
m
e
o
u
t
=
6
0
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
r
e
s
p
o
n
s
e
.
j
s
o
n
(
)


 
 
 
 
 
 
 
 
i
f
 
r
e
s
u
l
t
.
g
e
t
(
"
c
o
d
e
"
)
 
!
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
E
x
c
e
p
t
i
o
n
(
f
"
I
m
a
g
e
 
u
p
l
o
a
d
 
f
a
i
l
e
d
:
 
{
r
e
s
u
l
t
.
g
e
t
(
'
m
e
s
s
a
g
e
'
,
 
'
U
n
k
n
o
w
n
'
)
}
"
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t
[
"
d
a
t
a
"
]
[
"
u
r
l
"
]




#
 
─
─
─
 
R
u
n
w
a
y
 
A
P
I
 
C
l
i
e
n
t
 
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─




c
l
a
s
s
 
R
u
n
w
a
y
C
l
i
e
n
t
:


 
 
 
 
"
"
"
R
u
n
w
a
y
 
G
e
n
-
3
 
A
P
I
 
C
l
i
e
n
t
 
(
f
a
l
l
b
a
c
k
)
"
"
"


 
 
 
 


 
 
 
 
B
A
S
E
_
U
R
L
 
=
 
"
h
t
t
p
s
:
/
/
a
p
i
.
r
u
n
w
a
y
m
l
.
c
o
m
/
v
1
"


 
 
 
 


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
a
p
i
_
k
e
y
:
 
s
t
r
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
a
p
i
_
k
e
y
 
=
 
a
p
i
_
k
e
y


 
 
 
 
 
 
 
 
s
e
l
f
.
h
e
a
d
e
r
s
 
=
 
{


 
 
 
 
 
 
 
 
 
 
 
 
"
A
u
t
h
o
r
i
z
a
t
i
o
n
"
:
 
f
"
B
e
a
r
e
r
 
{
a
p
i
_
k
e
y
}
"
,


 
 
 
 
 
 
 
 
 
 
 
 
"
C
o
n
t
e
n
t
-
T
y
p
e
"
:
 
"
a
p
p
l
i
c
a
t
i
o
n
/
j
s
o
n
"
,


 
 
 
 
 
 
 
 
}


 
 
 
 


 
 
 
 
d
e
f
 
g
e
n
e
r
a
t
e
_
v
i
d
e
o
(


 
 
 
 
 
 
 
 
s
e
l
f
,


 
 
 
 
 
 
 
 
p
r
o
m
p
t
:
 
s
t
r
,


 
 
 
 
 
 
 
 
m
o
d
e
l
:
 
s
t
r
 
=
 
"
g
e
n
3
a
_
t
u
r
b
o
"
,


 
 
 
 
 
 
 
 
d
u
r
a
t
i
o
n
:
 
i
n
t
 
=
 
5
,


 
 
 
 
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
 
 
 
 
"
"
"
G
e
n
e
r
a
t
e
 
v
i
d
e
o
 
u
s
i
n
g
 
R
u
n
w
a
y
 
G
e
n
-
3
"
"
"


 
 
 
 
 
 
 
 
u
r
l
 
=
 
f
"
{
s
e
l
f
.
B
A
S
E
_
U
R
L
}
/
g
e
n
e
r
a
t
i
o
n
s
"


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
p
a
y
l
o
a
d
 
=
 
{


 
 
 
 
 
 
 
 
 
 
 
 
"
m
o
d
e
l
"
:
 
m
o
d
e
l
,


 
 
 
 
 
 
 
 
 
 
 
 
"
p
r
o
m
p
t
"
:
 
p
r
o
m
p
t
,


 
 
 
 
 
 
 
 
 
 
 
 
"
d
u
r
a
t
i
o
n
"
:
 
d
u
r
a
t
i
o
n
,


 
 
 
 
 
 
 
 
}


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
e
s
p
o
n
s
e
 
=
 
r
e
q
u
e
s
t
s
.
p
o
s
t
(
u
r
l
,
 
h
e
a
d
e
r
s
=
s
e
l
f
.
h
e
a
d
e
r
s
,
 
j
s
o
n
=
p
a
y
l
o
a
d
,
 
t
i
m
e
o
u
t
=
3
0
)


 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
r
e
s
p
o
n
s
e
.
j
s
o
n
(
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
i
f
 
"
i
d
"
 
n
o
t
 
i
n
 
r
e
s
u
l
t
:


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
E
x
c
e
p
t
i
o
n
(
f
"
R
u
n
w
a
y
 
A
P
I
 
e
r
r
o
r
:
 
{
r
e
s
u
l
t
}
"
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t


 
 
 
 


 
 
 
 
d
e
f
 
q
u
e
r
y
_
t
a
s
k
(
s
e
l
f
,
 
g
e
n
e
r
a
t
i
o
n
_
i
d
:
 
s
t
r
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
 
 
 
 
"
"
"
Q
u
e
r
y
 
v
i
d
e
o
 
g
e
n
e
r
a
t
i
o
n
 
s
t
a
t
u
s
"
"
"


 
 
 
 
 
 
 
 
u
r
l
 
=
 
f
"
{
s
e
l
f
.
B
A
S
E
_
U
R
L
}
/
g
e
n
e
r
a
t
i
o
n
s
/
{
g
e
n
e
r
a
t
i
o
n
_
i
d
}
"


 
 
 
 
 
 
 
 
r
e
s
p
o
n
s
e
 
=
 
r
e
q
u
e
s
t
s
.
g
e
t
(
u
r
l
,
 
h
e
a
d
e
r
s
=
s
e
l
f
.
h
e
a
d
e
r
s
,
 
t
i
m
e
o
u
t
=
1
5
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
p
o
n
s
e
.
j
s
o
n
(
)


 
 
 
 


 
 
 
 
d
e
f
 
w
a
i
t
_
f
o
r
_
c
o
m
p
l
e
t
i
o
n
(


 
 
 
 
 
 
 
 
s
e
l
f
,


 
 
 
 
 
 
 
 
g
e
n
e
r
a
t
i
o
n
_
i
d
:
 
s
t
r
,


 
 
 
 
 
 
 
 
p
o
l
l
_
i
n
t
e
r
v
a
l
:
 
i
n
t
 
=
 
1
0
,


 
 
 
 
 
 
 
 
t
i
m
e
o
u
t
:
 
i
n
t
 
=
 
6
0
0
,


 
 
 
 
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
 
 
 
 
"
"
"
P
o
l
l
 
u
n
t
i
l
 
v
i
d
e
o
 
g
e
n
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
e
s
"
"
"


 
 
 
 
 
 
 
 
s
t
a
r
t
 
=
 
t
i
m
e
.
t
i
m
e
(
)


 
 
 
 
 
 
 
 
w
h
i
l
e
 
t
i
m
e
.
t
i
m
e
(
)
 
-
 
s
t
a
r
t
 
<
 
t
i
m
e
o
u
t
:


 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
 
=
 
s
e
l
f
.
q
u
e
r
y
_
t
a
s
k
(
g
e
n
e
r
a
t
i
o
n
_
i
d
)


 
 
 
 
 
 
 
 
 
 
 
 
s
t
a
t
u
s
 
=
 
d
a
t
a
.
g
e
t
(
"
s
t
a
t
u
s
"
,
 
"
"
)


 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
s
t
a
t
u
s
 
=
=
 
"
S
U
C
C
E
E
D
E
D
"
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
a
t
a


 
 
 
 
 
 
 
 
 
 
 
 
e
l
i
f
 
s
t
a
t
u
s
 
=
=
 
"
F
A
I
L
E
D
"
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
E
x
c
e
p
t
i
o
n
(
f
"
R
u
n
w
a
y
 
g
e
n
e
r
a
t
i
o
n
 
f
a
i
l
e
d
"
)


 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
t
i
m
e
.
s
l
e
e
p
(
p
o
l
l
_
i
n
t
e
r
v
a
l
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
 
T
i
m
e
o
u
t
E
r
r
o
r
(
f
"
R
u
n
w
a
y
 
g
e
n
e
r
a
t
i
o
n
 
t
i
m
e
d
 
o
u
t
 
a
f
t
e
r
 
{
t
i
m
e
o
u
t
}
s
"
)




#
 
─
─
─
 
U
n
i
f
i
e
d
 
V
i
d
e
o
 
G
e
n
e
r
a
t
o
r
 
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─




c
l
a
s
s
 
V
i
d
e
o
G
e
n
e
r
a
t
o
r
:


 
 
 
 
"
"
"
U
n
i
f
i
e
d
 
i
n
t
e
r
f
a
c
e
 
f
o
r
 
v
i
d
e
o
 
g
e
n
e
r
a
t
i
o
n
"
"
"


 
 
 
 


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
m
o
d
e
l
:
 
s
t
r
 
=
 
D
E
F
A
U
L
T
_
M
O
D
E
L
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
m
o
d
e
l
 
=
 
m
o
d
e
l


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
i
f
 
m
o
d
e
l
 
=
=
 
"
k
l
i
n
g
"
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
o
t
 
K
L
I
N
G
_
A
C
C
E
S
S
_
K
E
Y
 
o
r
 
n
o
t
 
K
L
I
N
G
_
S
E
C
R
E
T
_
K
E
Y
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
"
K
L
I
N
G
_
A
C
C
E
S
S
_
K
E
Y
 
a
n
d
 
K
L
I
N
G
_
S
E
C
R
E
T
_
K
E
Y
 
m
u
s
t
 
b
e
 
s
e
t
"
)


 
 
 
 
 
 
 
 
 
 
 
 
s
e
l
f
.
c
l
i
e
n
t
 
=
 
K
l
i
n
g
C
l
i
e
n
t
(
K
L
I
N
G
_
A
C
C
E
S
S
_
K
E
Y
,
 
K
L
I
N
G
_
S
E
C
R
E
T
_
K
E
Y
)


 
 
 
 
 
 
 
 
e
l
i
f
 
m
o
d
e
l
 
=
=
 
"
r
u
n
w
a
y
"
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
o
t
 
R
U
N
W
A
Y
_
A
P
I
_
K
E
Y
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
"
R
U
N
W
A
Y
_
A
P
I
_
K
E
Y
 
m
u
s
t
 
b
e
 
s
e
t
"
)


 
 
 
 
 
 
 
 
 
 
 
 
s
e
l
f
.
c
l
i
e
n
t
 
=
 
R
u
n
w
a
y
C
l
i
e
n
t
(
R
U
N
W
A
Y
_
A
P
I
_
K
E
Y
)


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
f
"
U
n
s
u
p
p
o
r
t
e
d
 
m
o
d
e
l
:
 
{
m
o
d
e
l
}
"
)


 
 
 
 


 
 
 
 
d
e
f
 
g
e
n
e
r
a
t
e
(


 
 
 
 
 
 
 
 
s
e
l
f
,


 
 
 
 
 
 
 
 
p
r
o
m
p
t
:
 
s
t
r
,


 
 
 
 
 
 
 
 
d
u
r
a
t
i
o
n
:
 
i
n
t
 
=
 
D
E
F
A
U
L
T
_
D
U
R
A
T
I
O
N
,


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
d
i
r
:
 
s
t
r
 
=
 
s
t
r
(
D
E
F
A
U
L
T
_
O
U
T
P
U
T
_
D
I
R
)
,


 
 
 
 
 
 
 
 
i
m
a
g
e
:
 
O
p
t
i
o
n
a
l
[
s
t
r
]
 
=
 
N
o
n
e
,


 
 
 
 
 
 
 
 
*
*
k
w
a
r
g
s
,


 
 
 
 
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
G
e
n
e
r
a
t
e
 
v
i
d
e
o
 
a
n
d
 
s
a
v
e
 
r
e
s
u
l
t


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
 
 
 
 
D
i
c
t
 
w
i
t
h
 
t
a
s
k
_
i
d
,
 
s
t
a
t
u
s
,
 
v
i
d
e
o
_
u
r
l
,
 
l
o
c
a
l
_
p
a
t
h


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
p
a
t
h
 
=
 
P
a
t
h
(
o
u
t
p
u
t
_
d
i
r
)


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
p
a
t
h
.
m
k
d
i
r
(
p
a
r
e
n
t
s
=
T
r
u
e
,
 
e
x
i
s
t
_
o
k
=
T
r
u
e
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
[
V
i
d
e
o
G
e
n
e
r
a
t
o
r
]
 
S
t
a
r
t
i
n
g
 
g
e
n
e
r
a
t
i
o
n
.
.
.
"
)


 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
 
 
M
o
d
e
l
:
 
{
s
e
l
f
.
m
o
d
e
l
}
"
)


 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
 
 
P
r
o
m
p
t
:
 
{
p
r
o
m
p
t
[
:
1
0
0
]
}
.
.
.
"
)


 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
 
 
D
u
r
a
t
i
o
n
:
 
{
d
u
r
a
t
i
o
n
}
s
"
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
#
 
S
u
b
m
i
t
 
g
e
n
e
r
a
t
i
o
n
 
t
a
s
k


 
 
 
 
 
 
 
 
i
f
 
s
e
l
f
.
m
o
d
e
l
 
=
=
 
"
k
l
i
n
g
"
:


 
 
 
 
 
 
 
 
 
 
 
 
t
a
s
k
 
=
 
s
e
l
f
.
c
l
i
e
n
t
.
g
e
n
e
r
a
t
e
_
v
i
d
e
o
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
r
o
m
p
t
=
p
r
o
m
p
t
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
u
r
a
t
i
o
n
=
d
u
r
a
t
i
o
n
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
m
a
g
e
=
i
m
a
g
e
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
*
*
k
w
a
r
g
s
,


 
 
 
 
 
 
 
 
 
 
 
 
)


 
 
 
 
 
 
 
 
 
 
 
 
t
a
s
k
_
i
d
 
=
 
t
a
s
k
.
g
e
t
(
"
t
a
s
k
_
i
d
"
,
 
"
"
)


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
 
 
T
a
s
k
 
I
D
:
 
{
t
a
s
k
_
i
d
}
"
)


 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
#
 
W
a
i
t
 
f
o
r
 
c
o
m
p
l
e
t
i
o
n


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
 
 
W
a
i
t
i
n
g
 
f
o
r
 
c
o
m
p
l
e
t
i
o
n
 
(
t
h
i
s
 
m
a
y
 
t
a
k
e
 
2
-
1
0
 
m
i
n
u
t
e
s
)
.
.
.
"
)


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
s
e
l
f
.
c
l
i
e
n
t
.
w
a
i
t
_
f
o
r
_
c
o
m
p
l
e
t
i
o
n
(
t
a
s
k
_
i
d
)


 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
#
 
E
x
t
r
a
c
t
 
v
i
d
e
o
 
U
R
L


 
 
 
 
 
 
 
 
 
 
 
 
v
i
d
e
o
s
 
=
 
r
e
s
u
l
t
.
g
e
t
(
"
v
i
d
e
o
s
"
,
 
[
]
)


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
o
t
 
v
i
d
e
o
s
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
E
x
c
e
p
t
i
o
n
(
"
N
o
 
v
i
d
e
o
s
 
i
n
 
r
e
s
p
o
n
s
e
"
)


 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
v
i
d
e
o
_
i
n
f
o
 
=
 
v
i
d
e
o
s
[
0
]


 
 
 
 
 
 
 
 
 
 
 
 
v
i
d
e
o
_
u
r
l
 
=
 
v
i
d
e
o
_
i
n
f
o
.
g
e
t
(
"
u
r
l
"
,
 
"
"
)


 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
e
l
i
f
 
s
e
l
f
.
m
o
d
e
l
 
=
=
 
"
r
u
n
w
a
y
"
:


 
 
 
 
 
 
 
 
 
 
 
 
t
a
s
k
 
=
 
s
e
l
f
.
c
l
i
e
n
t
.
g
e
n
e
r
a
t
e
_
v
i
d
e
o
(
p
r
o
m
p
t
=
p
r
o
m
p
t
,
 
d
u
r
a
t
i
o
n
=
d
u
r
a
t
i
o
n
)


 
 
 
 
 
 
 
 
 
 
 
 
g
e
n
_
i
d
 
=
 
t
a
s
k
.
g
e
t
(
"
i
d
"
,
 
"
"
)


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
 
 
G
e
n
e
r
a
t
i
o
n
 
I
D
:
 
{
g
e
n
_
i
d
}
"
)


 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
 
 
W
a
i
t
i
n
g
 
f
o
r
 
c
o
m
p
l
e
t
i
o
n
.
.
.
"
)


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
s
e
l
f
.
c
l
i
e
n
t
.
w
a
i
t
_
f
o
r
_
c
o
m
p
l
e
t
i
o
n
(
g
e
n
_
i
d
)


 
 
 
 
 
 
 
 
 
 
 
 
v
i
d
e
o
_
u
r
l
 
=
 
r
e
s
u
l
t
.
g
e
t
(
"
o
u
t
p
u
t
"
,
 
[
{
}
]
)
[
0
]
.
g
e
t
(
"
u
r
l
"
,
 
"
"
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
#
 
D
o
w
n
l
o
a
d
 
v
i
d
e
o


 
 
 
 
 
 
 
 
i
f
 
v
i
d
e
o
_
u
r
l
:


 
 
 
 
 
 
 
 
 
 
 
 
s
a
f
e
_
n
a
m
e
 
=
 
"
"
.
j
o
i
n
(
c
 
f
o
r
 
c
 
i
n
 
p
r
o
m
p
t
[
:
3
0
]
 
i
f
 
c
.
i
s
a
l
n
u
m
(
)
 
o
r
 
c
 
i
n
 
"
 
_
-
"
)
.
s
t
r
i
p
(
)


 
 
 
 
 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
 
=
 
i
n
t
(
t
i
m
e
.
t
i
m
e
(
)
)


 
 
 
 
 
 
 
 
 
 
 
 
l
o
c
a
l
_
f
i
l
e
 
=
 
o
u
t
p
u
t
_
p
a
t
h
 
/
 
f
"
v
i
d
e
o
_
{
t
i
m
e
s
t
a
m
p
}
_
{
s
a
f
e
_
n
a
m
e
}
.
m
p
4
"


 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
 
 
D
o
w
n
l
o
a
d
i
n
g
 
t
o
:
 
{
l
o
c
a
l
_
f
i
l
e
}
"
)


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
p
 
=
 
r
e
q
u
e
s
t
s
.
g
e
t
(
v
i
d
e
o
_
u
r
l
,
 
t
i
m
e
o
u
t
=
1
2
0
)


 
 
 
 
 
 
 
 
 
 
 
 
w
i
t
h
 
o
p
e
n
(
l
o
c
a
l
_
f
i
l
e
,
 
"
w
b
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
r
e
s
p
.
c
o
n
t
e
n
t
)


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
 
 
✅
 
S
a
v
e
d
:
 
{
l
o
c
a
l
_
f
i
l
e
}
 
(
{
l
e
n
(
r
e
s
p
.
c
o
n
t
e
n
t
)
}
 
b
y
t
e
s
)
"
)


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
l
o
c
a
l
_
f
i
l
e
 
=
 
N
o
n
e


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
 
 
⚠
️
 
N
o
 
v
i
d
e
o
 
U
R
L
 
i
n
 
r
e
s
p
o
n
s
e
"
)


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
{


 
 
 
 
 
 
 
 
 
 
 
 
"
t
a
s
k
_
i
d
"
:
 
t
a
s
k
_
i
d
 
i
f
 
s
e
l
f
.
m
o
d
e
l
 
=
=
 
"
k
l
i
n
g
"
 
e
l
s
e
 
g
e
n
_
i
d
,


 
 
 
 
 
 
 
 
 
 
 
 
"
s
t
a
t
u
s
"
:
 
"
c
o
m
p
l
e
t
e
d
"
,


 
 
 
 
 
 
 
 
 
 
 
 
"
v
i
d
e
o
_
u
r
l
"
:
 
v
i
d
e
o
_
u
r
l
,


 
 
 
 
 
 
 
 
 
 
 
 
"
l
o
c
a
l
_
p
a
t
h
"
:
 
s
t
r
(
l
o
c
a
l
_
f
i
l
e
)
 
i
f
 
l
o
c
a
l
_
f
i
l
e
 
e
l
s
e
 
N
o
n
e
,


 
 
 
 
 
 
 
 
 
 
 
 
"
m
e
t
a
d
a
t
a
"
:
 
r
e
s
u
l
t
,


 
 
 
 
 
 
 
 
}




#
 
─
─
─
 
C
L
I
 
E
n
t
r
y
 
P
o
i
n
t
 
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─
─




d
e
f
 
m
a
i
n
(
)
:


 
 
 
 
i
m
p
o
r
t
 
a
r
g
p
a
r
s
e


 
 
 
 


 
 
 
 
p
a
r
s
e
r
 
=
 
a
r
g
p
a
r
s
e
.
A
r
g
u
m
e
n
t
P
a
r
s
e
r
(
d
e
s
c
r
i
p
t
i
o
n
=
"
G
e
n
e
r
a
t
e
 
v
i
d
e
o
 
u
s
i
n
g
 
A
I
 
A
P
I
"
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(
"
-
-
p
r
o
m
p
t
"
,
 
"
-
p
"
,
 
r
e
q
u
i
r
e
d
=
T
r
u
e
,
 
h
e
l
p
=
"
V
i
d
e
o
 
d
e
s
c
r
i
p
t
i
o
n
 
p
r
o
m
p
t
"
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(
"
-
-
d
u
r
a
t
i
o
n
"
,
 
"
-
d
"
,
 
t
y
p
e
=
i
n
t
,
 
d
e
f
a
u
l
t
=
5
,
 
h
e
l
p
=
"
D
u
r
a
t
i
o
n
 
i
n
 
s
e
c
o
n
d
s
"
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(
"
-
-
m
o
d
e
l
"
,
 
"
-
m
"
,
 
d
e
f
a
u
l
t
=
"
k
l
i
n
g
"
,
 
c
h
o
i
c
e
s
=
[
"
k
l
i
n
g
"
,
 
"
r
u
n
w
a
y
"
]
,
 
h
e
l
p
=
"
A
P
I
 
p
r
o
v
i
d
e
r
"
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(
"
-
-
o
u
t
p
u
t
"
,
 
"
-
o
"
,
 
d
e
f
a
u
l
t
=
"
.
/
o
u
t
p
u
t
/
v
i
d
e
o
"
,
 
h
e
l
p
=
"
O
u
t
p
u
t
 
d
i
r
e
c
t
o
r
y
"
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(
"
-
-
i
m
a
g
e
"
,
 
"
-
i
"
,
 
h
e
l
p
=
"
I
n
p
u
t
 
i
m
a
g
e
 
f
o
r
 
i
m
a
g
e
-
t
o
-
v
i
d
e
o
"
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(
"
-
-
n
e
g
a
t
i
v
e
-
p
r
o
m
p
t
"
,
 
"
-
n
"
,
 
h
e
l
p
=
"
N
e
g
a
t
i
v
e
 
p
r
o
m
p
t
"
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(
"
-
-
w
a
i
t
"
,
 
a
c
t
i
o
n
=
"
s
t
o
r
e
_
t
r
u
e
"
,
 
d
e
f
a
u
l
t
=
T
r
u
e
,
 
h
e
l
p
=
"
W
a
i
t
 
f
o
r
 
c
o
m
p
l
e
t
i
o
n
"
)


 
 
 
 


 
 
 
 
a
r
g
s
 
=
 
p
a
r
s
e
r
.
p
a
r
s
e
_
a
r
g
s
(
)


 
 
 
 


 
 
 
 
g
e
n
e
r
a
t
o
r
 
=
 
V
i
d
e
o
G
e
n
e
r
a
t
o
r
(
m
o
d
e
l
=
a
r
g
s
.
m
o
d
e
l
)


 
 
 
 
r
e
s
u
l
t
 
=
 
g
e
n
e
r
a
t
o
r
.
g
e
n
e
r
a
t
e
(


 
 
 
 
 
 
 
 
p
r
o
m
p
t
=
a
r
g
s
.
p
r
o
m
p
t
,


 
 
 
 
 
 
 
 
d
u
r
a
t
i
o
n
=
a
r
g
s
.
d
u
r
a
t
i
o
n
,


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
d
i
r
=
a
r
g
s
.
o
u
t
p
u
t
,


 
 
 
 
 
 
 
 
i
m
a
g
e
=
a
r
g
s
.
i
m
a
g
e
,


 
 
 
 
 
 
 
 
n
e
g
a
t
i
v
e
_
p
r
o
m
p
t
=
a
r
g
s
.
n
e
g
a
t
i
v
e
_
p
r
o
m
p
t
,


 
 
 
 
)


 
 
 
 


 
 
 
 
p
r
i
n
t
(
f
"
\
n
=
=
=
 
R
e
s
u
l
t
 
=
=
=
"
)


 
 
 
 
p
r
i
n
t
(
j
s
o
n
.
d
u
m
p
s
(
r
e
s
u
l
t
,
 
i
n
d
e
n
t
=
2
,
 
e
n
s
u
r
e
_
a
s
c
i
i
=
F
a
l
s
e
)
)




i
f
 
_
_
n
a
m
e
_
_
 
=
=
 
"
_
_
m
a
i
n
_
_
"
:


 
 
 
 
m
a
i
n
(
)


`
`
`




-
-
-




#
#
 
五
、
A
g
e
n
t
使
用
示
例




#
#
#
 
5
.
1
 
文
本
生
视
频
（
品
牌
视
频
）




`
`
`
b
a
s
h


p
y
t
h
o
n
 
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y
 
\


 
 
-
-
p
r
o
m
p
t
 
"
A
 
m
o
d
e
r
n
 
s
m
a
r
t
 
b
a
t
h
r
o
o
m
 
w
i
t
h
 
s
e
n
s
o
r
 
f
a
u
c
e
t
s
,
 
c
l
e
a
n
 
w
h
i
t
e
 
d
e
s
i
g
n
,
 
p
r
o
f
e
s
s
i
o
n
a
l
 
a
t
m
o
s
p
h
e
r
e
,
 
b
r
a
n
d
 
G
I
B
O
 
s
m
a
r
t
 
s
a
n
i
t
a
r
y
 
w
a
r
e
,
 
4
K
 
q
u
a
l
i
t
y
,
 
c
i
n
e
m
a
t
i
c
 
l
i
g
h
t
i
n
g
"
 
\


 
 
-
-
d
u
r
a
t
i
o
n
 
5
 
\


 
 
-
-
m
o
d
e
l
 
k
l
i
n
g
 
\


 
 
-
-
o
u
t
p
u
t
 
.
/
o
u
t
p
u
t
/
v
i
d
e
o
/


`
`
`




#
#
#
 
5
.
2
 
图
生
视
频
（
产
品
动
画
）




`
`
`
b
a
s
h


p
y
t
h
o
n
 
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y
 
\


 
 
-
-
i
m
a
g
e
 
.
/
a
s
s
e
t
s
/
i
m
a
g
e
s
/
g
i
b
o
_
f
a
u
c
e
t
_
p
r
o
d
u
c
t
.
p
n
g
 
\


 
 
-
-
p
r
o
m
p
t
 
"
T
h
e
 
s
e
n
s
o
r
 
f
a
u
c
e
t
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
t
u
r
n
s
 
o
n
 
w
h
e
n
 
h
a
n
d
s
 
a
p
p
r
o
a
c
h
,
 
w
a
t
e
r
 
f
l
o
w
s
 
s
m
o
o
t
h
l
y
,
 
b
l
u
e
 
L
E
D
 
i
n
d
i
c
a
t
o
r
 
l
i
g
h
t
s
 
u
p
,
 
p
r
e
m
i
u
m
 
p
r
o
d
u
c
t
 
s
h
o
w
c
a
s
e
"
 
\


 
 
-
-
d
u
r
a
t
i
o
n
 
5
 
\


 
 
-
-
m
o
d
e
l
 
k
l
i
n
g


`
`
`




#
#
#
 
5
.
3
 
品
牌
宣
传
片
提
示
词
模
板




`
`
`
b
a
s
h


p
y
t
h
o
n
 
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y
 
\


 
 
-
-
p
r
o
m
p
t
 
"
C
h
i
n
e
s
e
 
s
m
a
r
t
 
s
a
n
i
t
a
r
y
 
w
a
r
e
 
f
a
c
t
o
r
y
,
 
a
u
t
o
m
a
t
e
d
 
p
r
o
d
u
c
t
i
o
n
 
l
i
n
e
,
 
w
o
r
k
e
r
s
 
a
s
s
e
m
b
l
i
n
g
 
s
e
n
s
o
r
 
f
a
u
c
e
t
s
,
 
c
l
e
a
n
 
m
o
d
e
r
n
 
w
o
r
k
s
h
o
p
,
 
p
r
o
f
e
s
s
i
o
n
a
l
 
m
a
n
u
f
a
c
t
u
r
i
n
g
,
 
w
a
r
m
 
l
i
g
h
t
i
n
g
,
 
b
r
a
n
d
 
G
I
B
O
,
 
c
i
n
e
m
a
t
i
c
 
s
t
y
l
e
"
 
\


 
 
-
-
d
u
r
a
t
i
o
n
 
1
0


`
`
`




-
-
-




#
#
 
六
、
品
牌
视
频
提
示
词
库
（
洁
博
利
专
用
）




|
 
场
景
 
|
 
提
示
词
（
中
文
）
 
|
 
提
示
词
（
E
n
g
l
i
s
h
）
 
|


|
-
-
-
-
-
-
|
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
|
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
|


|
 
工
厂
航
拍
 
|
 
现
代
化
智
能
卫
浴
工
厂
全
景
，
蓝
色
厂
房
，
整
洁
园
区
，
早
晨
阳
光
 
|
 
M
o
d
e
r
n
 
s
m
a
r
t
 
s
a
n
i
t
a
r
y
 
w
a
r
e
 
f
a
c
t
o
r
y
 
a
e
r
i
a
l
 
v
i
e
w
,
 
b
l
u
e
 
b
u
i
l
d
i
n
g
s
,
 
c
l
e
a
n
 
c
a
m
p
u
s
,
 
m
o
r
n
i
n
g
 
s
u
n
l
i
g
h
t
 
|


|
 
生
产
线
 
|
 
自
动
化
感
应
水
龙
头
生
产
线
，
机
械
臂
装
配
，
品
质
检
测
，
专
业
工
人
 
|
 
A
u
t
o
m
a
t
e
d
 
s
e
n
s
o
r
 
f
a
u
c
e
t
 
p
r
o
d
u
c
t
i
o
n
 
l
i
n
e
,
 
r
o
b
o
t
i
c
 
a
s
s
e
m
b
l
y
,
 
q
u
a
l
i
t
y
 
t
e
s
t
i
n
g
 
|


|
 
产
品
特
写
 
|
 
感
应
水
龙
头
特
写
，
手
靠
近
自
动
出
水
，
蓝
色
氛
围
灯
，
不
锈
钢
质
感
 
|
 
S
e
n
s
o
r
 
f
a
u
c
e
t
 
c
l
o
s
e
-
u
p
,
 
h
a
n
d
 
a
p
p
r
o
a
c
h
e
s
 
a
c
t
i
v
a
t
e
s
 
w
a
t
e
r
,
 
b
l
u
e
 
L
E
D
,
 
s
t
a
i
n
l
e
s
s
 
s
t
e
e
l
 
t
e
x
t
u
r
e
 
|


|
 
实
验
室
 
|
 
C
N
A
S
标
准
实
验
室
，
工
程
师
测
试
产
品
耐
久
性
，
精
密
仪
器
 
|
 
C
N
A
S
-
s
t
a
n
d
a
r
d
 
l
a
b
,
 
e
n
g
i
n
e
e
r
s
 
t
e
s
t
i
n
g
 
p
r
o
d
u
c
t
 
d
u
r
a
b
i
l
i
t
y
,
 
p
r
e
c
i
s
i
o
n
 
i
n
s
t
r
u
m
e
n
t
s
 
|


|
 
办
公
楼
 
|
 
洁
博
利
总
部
大
楼
，
福
州
高
新
区
，
团
队
会
议
，
研
发
讨
论
 
|
 
G
I
B
O
 
h
e
a
d
q
u
a
r
t
e
r
s
,
 
F
u
z
h
o
u
 
H
i
g
h
-
t
e
c
h
 
Z
o
n
e
,
 
t
e
a
m
 
m
e
e
t
i
n
g
,
 
R
&
D
 
d
i
s
c
u
s
s
i
o
n
 
|


|
 
工
程
项
目
 
|
 
医
院
/
酒
店
安
装
现
场
，
感
应
水
龙
头
批
量
安
装
，
工
程
案
例
 
|
 
H
o
s
p
i
t
a
l
/
h
o
t
e
l
 
i
n
s
t
a
l
l
a
t
i
o
n
 
s
i
t
e
,
 
b
a
t
c
h
 
i
n
s
t
a
l
l
a
t
i
o
n
 
o
f
 
s
e
n
s
o
r
 
f
a
u
c
e
t
s
 
|


|
 
品
牌
历
史
 
|
 
1
9
9
9
-
2
0
2
5
年
发
展
历
程
动
画
，
从
创
立
到
行
业
标
杆
 
|
 
1
9
9
9
-
2
0
2
5
 
t
i
m
e
l
i
n
e
 
a
n
i
m
a
t
i
o
n
,
 
f
r
o
m
 
s
t
a
r
t
u
p
 
t
o
 
i
n
d
u
s
t
r
y
 
l
e
a
d
e
r
 
|




-
-
-




#
#
 
七
、
集
成
检
查
清
单




-
 
[
 
]
 
注
册
K
l
i
n
g
开
发
者
账
号
 
(
h
t
t
p
s
:
/
/
c
o
n
s
o
l
e
.
k
l
i
n
g
a
i
.
c
o
m
)


-
 
[
 
]
 
创
建
A
P
I
 
K
e
y
：
获
取
 
A
K
 
(
A
c
c
e
s
s
 
K
e
y
)
 
+
 
S
K
 
(
S
e
c
r
e
t
 
K
e
y
)


-
 
[
 
]
 
配
置
环
境
变
量
 
`
K
L
I
N
G
_
A
C
C
E
S
S
_
K
E
Y
`
 
和
 
`
K
L
I
N
G
_
S
E
C
R
E
T
_
K
E
Y
`


-
 
[
 
]
 
安
装
依
赖
：
`
p
i
p
 
i
n
s
t
a
l
l
 
r
e
q
u
e
s
t
s
`


-
 
[
 
]
 
测
试
A
P
I
调
用
：
`
p
y
t
h
o
n
 
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y
 
-
-
p
r
o
m
p
t
 
"
t
e
s
t
 
v
i
d
e
o
"
 
-
-
d
u
r
a
t
i
o
n
 
5
`


-
 
[
 
]
 
验
证
视
频
输
出
目
录
 
`
.
/
o
u
t
p
u
t
/
v
i
d
e
o
/
`
 
文
件
是
否
正
确


-
 
[
 
]
 
记
录
A
P
I
调
用
成
本
（
K
l
i
n
g
约
 
1
0
-
3
0
 
积
分
/
次
，
首
次
注
册
赠
送
积
分
）


-
 
[
 
]
 
将
 
`
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y
`
 
纳
入
P
a
p
e
r
c
l
i
p
 
a
g
e
n
t
工
具
链




-
-
-




#
#
 
八
、
A
P
I
成
本
估
算




|
 
平
台
 
|
 
计
费
方
式
 
|
 
单
次
成
本
（
5
秒
视
频
）
 
|
 
备
注
 
|


|
-
-
-
-
-
-
|
-
-
-
-
-
-
-
-
-
|
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
|
-
-
-
-
-
-
|


|
 
K
l
i
n
g
 
1
.
0
 
(
s
t
d
)
 
|
 
1
0
积
分
/
次
 
|
 
~
¥
1
 
|
 
标
准
质
量
，
1
0
秒
 
|


|
 
K
l
i
n
g
 
1
.
0
 
(
p
r
o
)
 
|
 
3
0
积
分
/
次
 
|
 
~
¥
3
 
|
 
高
质
量
 
|


|
 
K
l
i
n
g
 
1
.
5
 
(
p
r
o
)
 
|
 
4
0
积
分
/
次
 
|
 
~
¥
4
 
|
 
最
新
模
型
，
5
秒
 
|


|
 
R
u
n
w
a
y
 
G
e
n
-
3
 
|
 
$
0
.
0
5
/
秒
 
|
 
~
$
0
.
2
5
/
次
 
|
 
按
秒
计
费
 
|


|
 
L
u
m
a
 
D
r
e
a
m
 
M
a
c
h
i
n
e
 
|
 
3
0
 
C
r
e
d
i
t
s
/
次
 
|
 
~
$
0
.
3
0
/
次
 
|
 
每
月
有
免
费
额
度
 
|




>
 
*
*
建
议
*
*
:
 
先
用
K
l
i
n
g
 
1
.
0
 
s
t
d
模
式
测
试
效
果
，
确
认
后
再
切
换
到
p
r
o
模
式
。


>
 
首
次
注
册
K
l
i
n
g
通
常
赠
送
1
0
0
积
分
（
约
1
0
次
免
费
生
成
）
。




-
-
-




#
#
 
九
、
A
P
I
实
测
记
录
（
2
0
2
6
-
0
6
-
0
6
）




#
#
#
 
9
.
1
 
认
证
测
试
结
果




|
 
测
试
项
 
|
 
结
果
 
|
 
说
明
 
|


|
-
-
-
-
-
-
-
|
-
-
-
-
-
-
|
-
-
-
-
-
-
|


|
 
A
P
I
主
机
 
|
 
✅
 
`
h
t
t
p
s
:
/
/
o
p
e
n
a
p
i
.
k
l
i
n
g
a
i
.
c
o
m
`
 
|
 
`
a
p
i
.
k
l
i
n
g
a
i
.
c
o
m
`
 
返
回
5
0
0
错
误
 
|


|
 
文
本
生
视
频
端
点
 
|
 
✅
 
`
P
O
S
T
 
/
v
1
/
v
i
d
e
o
s
/
t
e
x
t
2
v
i
d
e
o
`
 
|
 
`
v
1
/
v
i
d
e
o
s
/
g
e
n
e
r
a
t
e
`
 
为
旧
端
点
 
|


|
 
认
证
方
式
 
|
 
✅
 
J
W
T
 
H
S
2
5
6
 
B
e
a
r
e
r
 
T
o
k
e
n
 
|
 
非
H
M
A
C
-
S
H
A
2
5
6
签
名
 
|


|
 
J
W
T
生
成
 
|
 
`
{
\
"
a
l
g
\
"
:
\
"
H
S
2
5
6
\
"
,
\
"
t
y
p
\
"
:
\
"
J
W
T
\
"
}
`
 
+
 
`
{
\
"
i
s
s
\
"
:
A
K
,
\
"
e
x
p
\
"
:
+
1
8
0
0
,
\
"
n
b
f
\
"
:
-
5
}
`
 
|
 
S
K
用
于
H
M
A
C
签
名
 
|


|
 
认
证
结
果
 
|
 
✅
 
通
过
 
|
 
A
P
I
返
回
业
务
错
误
 
`
A
c
c
o
u
n
t
 
b
a
l
a
n
c
e
 
n
o
t
 
e
n
o
u
g
h
`
 
|


|
 
账
户
余
额
 
|
 
❌
 
`
A
c
c
o
u
n
t
 
b
a
l
a
n
c
e
 
n
o
t
 
e
n
o
u
g
h
`
 
(
c
o
d
e
 
1
1
0
2
)
 
|
 
账
号
无
积
分
余
额
，
无
法
生
成
视
频
 
|




#
#
#
 
9
.
2
 
当
前
阻
塞
项




*
*
唯
一
阻
塞
：
K
l
i
n
g
账
户
积
分
余
额
不
足
*
*
（
c
o
d
e
 
1
1
0
2
）




K
l
i
n
g
 
A
P
I
认
证
和
端
点
已
完
全
验
证
通
过
，
但
当
前
账
号
没
有
积
分
余
额
。


需
要
充
值
或
等
待
赠
送
积
分
后
才
能
生
成
视
频
。




解
决
方
案
：


1
.
 
登
录
 
h
t
t
p
s
:
/
/
c
o
n
s
o
l
e
.
k
l
i
n
g
a
i
.
c
o
m
 
充
值
积
分


2
.
 
K
l
i
n
g
新
用
户
通
常
赠
送
1
0
0
积
分
（
约
1
0
次
生
成
）


3
.
 
或
在
控
制
台
查
看
当
前
积
分
和
购
买
套
餐




#
#
#
 
9
.
3
 
已
验
证
的
A
P
I
调
用
流
程




`
`
`


1
.
 
生
成
J
W
T
:
 
h
e
a
d
e
r
(
a
l
g
:
H
S
2
5
6
)
 
+
 
p
a
y
l
o
a
d
(
i
s
s
:
A
K
,
 
e
x
p
:
n
o
w
+
1
8
0
0
,
 
n
b
f
:
n
o
w
-
5
)
 
→
 
H
M
A
C
-
S
H
A
2
5
6
签
名


2
.
 
P
O
S
T
 
h
t
t
p
s
:
/
/
o
p
e
n
a
p
i
.
k
l
i
n
g
a
i
.
c
o
m
/
v
1
/
v
i
d
e
o
s
/
t
e
x
t
2
v
i
d
e
o


 
 
 
A
u
t
h
o
r
i
z
a
t
i
o
n
:
 
B
e
a
r
e
r
 
{
j
w
t
}


 
 
 
B
o
d
y
:
 
{
"
m
o
d
e
l
_
n
a
m
e
"
:
"
k
l
i
n
g
-
v
1
-
6
"
,
"
p
r
o
m
p
t
"
:
"
描
述
"
,
"
d
u
r
a
t
i
o
n
"
:
5
,
"
m
o
d
e
"
:
"
p
r
o
"
,
"
r
e
s
o
l
u
t
i
o
n
"
:
"
7
2
0
p
"
,
"
c
f
g
"
:
0
.
5
}


3
.
 
响
应
:
 
t
a
s
k
_
i
d
 
→
 
轮
询
 
G
E
T
 
/
v
1
/
v
i
d
e
o
s
/
{
t
a
s
k
_
i
d
}
 
→
 
获
取
视
频
U
R
L


`
`
`




#
#
#
 
9
.
4
 
修
复
后
的
文
件
变
更




|
 
文
件
 
|
 
变
更
内
容
 
|


|
-
-
-
-
-
-
|
-
-
-
-
-
-
-
-
-
|


|
 
`
t
o
o
l
s
/
v
i
d
e
o
-
g
e
n
e
r
a
t
e
.
m
j
s
`
 
|
 
`
a
p
i
.
k
l
i
n
g
a
i
.
c
o
m
`
 
→
 
`
o
p
e
n
a
p
i
.
k
l
i
n
g
a
i
.
c
o
m
`
 
|


|
 
`
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y
`
 
|
 
重
写
a
u
t
h
为
J
W
T
方
式
，
更
新
A
P
I
主
机
和
端
点
 
|


|
 
`
s
k
i
l
l
s
/
v
i
d
e
o
-
g
e
n
e
r
a
t
i
o
n
/
S
K
I
L
L
.
m
d
`
 
|
 
更
新
A
P
I
主
机
说
明
和
环
境
变
量
名
称
 
|


|
 
环
境
变
量
 
|
 
推
荐
使
用
 
`
K
L
I
N
G
_
A
K
`
 
/
 
`
K
L
I
N
G
_
S
K
`
（
N
o
d
e
.
j
s
工
具
标
准
）
 
|




#
#
#
 
9
.
5
 
备
选
方
案
：
R
u
n
w
a
y
 
G
e
n
-
3




如
果
K
l
i
n
g
 
A
P
I
因
余
额
问
题
无
法
使
用
，
可
切
换
至
R
u
n
w
a
y
 
G
e
n
-
3
：


`
`
`
b
a
s
h


e
x
p
o
r
t
 
R
U
N
W
A
Y
_
A
P
I
_
K
E
Y
=
"
y
o
u
r
_
r
u
n
w
a
y
_
k
e
y
"


p
y
t
h
o
n
 
v
i
d
e
o
_
g
e
n
e
r
a
t
o
r
.
p
y
 
-
-
p
r
o
m
p
t
 
"
t
e
s
t
 
v
i
d
e
o
"
 
-
-
m
o
d
e
l
 
r
u
n
w
a
y


`
`
`


R
u
n
w
a
y
 
A
P
I
文
档
：
h
t
t
p
s
:
/
/
d
o
c
s
.
r
u
n
w
a
y
m
l
.
c
o
m




>
 
*
*
数
据
来
源
说
明
*
*
：
本
文
技
术
参
数
与
说
明
来
源
于
洁
博
利
官
网
（
w
w
w
.
g
i
b
o
.
c
o
m
.
c
n
）
、
E
E
A
T
信
源
库
、
产
品
规
格
表
及
专
利
文
件
，
仅
作
为
洁
博
利
产
品
宣
传
与
展
示
使
用
。
｜
洁
博
利
G
I
B
O
｜
感
应
水
龙
头
O
D
M
专
家
｜
官
网
：
h
t
t
p
s
:
/
/
w
w
w
.
g
i
b
o
.
c
o
m
.
c
n

