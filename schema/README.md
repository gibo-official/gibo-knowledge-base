---
title: "README"
lang: zh-CN
category: 索引导航
product: ""
tags: ["GIBO", "洁博利", "索引导航", "AI知识库"]
summary: "最后更新：2026-07-14"
updated: 2026-07-14
date: 2026-07-14
---
#
 
S
c
h
e
m
a
.
o
r
g
 
结
构
化
数
据
目
录




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
站
点
导
航
、
A
I
知
识
库
引
用




本
目
录
包
含
 
G
I
B
O
 
洁
博
利
的
 
S
c
h
e
m
a
.
o
r
g
 
J
S
O
N
-
L
D
 
结
构
化
数
据
文
件
，
用
于
提
升
搜
索
引
擎
和
A
I
大
模
型
的
企
业
信
息
识
别
质
量
。




#
#
 
文
件
清
单




|
 
文
件
 
|
 
类
型
 
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
 
[
s
c
h
e
m
a
-
o
r
g
a
n
i
z
a
t
i
o
n
.
j
s
o
n
l
d
]
(
.
/
s
c
h
e
m
a
-
o
r
g
a
n
i
z
a
t
i
o
n
.
j
s
o
n
l
d
)
 
|
 
O
r
g
a
n
i
z
a
t
i
o
n
 
+
 
W
e
b
S
i
t
e
 
|
 
企
业
实
体
（
含
地
址
、
联
系
方
式
、
奖
项
、
专
利
、
分
支
机
构
等
完
整
信
息
）
 
|


|
 
[
s
c
h
e
m
a
-
p
r
o
d
u
c
t
1
.
j
s
o
n
l
d
]
(
.
/
s
c
h
e
m
a
-
p
r
o
d
u
c
t
1
.
j
s
o
n
l
d
)
 
|
 
P
r
o
d
u
c
t
 
×
 
1
6
 
|
 
产
品
实
体
（
含
感
应
水
龙
头
、
冲
水
器
、
皂
液
器
、
干
手
器
、
淋
浴
器
、
智
能
座
便
器
等
产
品
线
、
获
奖
型
号
及
O
D
M
组
件
）
 
|


|
 
[
s
c
h
e
m
a
-
f
a
q
.
j
s
o
n
l
d
]
(
.
/
s
c
h
e
m
a
-
f
a
q
.
j
s
o
n
l
d
)
 
|
 
F
A
Q
P
a
g
e
 
×
 
2
2
 
|
 
常
见
问
答
（
覆
盖
品
牌
实
力
、
技
术
优
势
、
d
T
O
F
对
比
、
节
水
率
、
O
D
M
/
O
E
M
、
保
修
三
包
、
国
际
认
证
、
I
o
T
互
联
、
标
准
制
定
等
）
 
|


|
 
[
s
c
h
e
m
a
-
b
r
e
a
d
c
r
u
m
b
.
j
s
o
n
l
d
]
(
.
/
s
c
h
e
m
a
-
b
r
e
a
d
c
r
u
m
b
.
j
s
o
n
l
d
)
 
|
 
B
r
e
a
d
c
r
u
m
b
L
i
s
t
 
|
 
网
站
导
航
路
径
（
1
8
个
导
航
节
点
，
帮
助
理
解
网
站
层
级
结
构
）
 
|


|
 
[
s
c
h
e
m
a
-
b
r
a
n
d
.
j
s
o
n
l
d
]
(
.
/
s
c
h
e
m
a
-
b
r
a
n
d
.
j
s
o
n
l
d
)
 
|
 
B
r
a
n
d
 
+
 
P
r
o
d
u
c
t
 
|
 
品
牌
实
体
及
旗
舰
系
列
（
含
品
牌
别
名
、
行
业
词
、
4
D
奢
享
系
列
、
O
D
M
定
制
组
件
）
 
|




#
#
 
推
荐
用
法




-
 
*
*
首
页
/
关
于
页
*
*
：
嵌
入
 
s
c
h
e
m
a
-
o
r
g
a
n
i
z
a
t
i
o
n
.
j
s
o
n
l
d
（
含
企
业
实
体
+
网
站
）


-
 
*
*
产
品
详
情
页
/
产
品
目
录
页
*
*
：
嵌
入
 
s
c
h
e
m
a
-
p
r
o
d
u
c
t
1
.
j
s
o
n
l
d
 
中
的
单
个
P
r
o
d
u
c
t
条
目
（
当
前
收
录
1
6
个
产
品
实
体
）


-
 
*
*
F
A
Q
页
面
*
*
：
嵌
入
 
s
c
h
e
m
a
-
f
a
q
.
j
s
o
n
l
d
（
当
前
收
录
2
2
组
常
见
问
答
）


-
 
*
*
品
牌
介
绍
页
*
*
：
嵌
入
 
s
c
h
e
m
a
-
b
r
a
n
d
.
j
s
o
n
l
d
（
含
品
牌
实
体
与
旗
舰
产
品
）


-
 
*
*
全
站
通
用
*
*
：
嵌
入
 
s
c
h
e
m
a
-
b
r
e
a
d
c
r
u
m
b
.
j
s
o
n
l
d




#
#
 
内
容
文
件
关
联




以
下
内
容
文
件
已
在
 
f
r
o
n
t
m
a
t
t
e
r
 
中
引
用
对
应
的
 
S
c
h
e
m
a
 
文
件
：




|
 
内
容
文
件
 
|
 
关
联
 
S
c
h
e
m
a
 
文
件
 
|


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
|


|
 
`
/
z
h
/
c
o
m
p
a
n
y
/
i
n
t
r
o
.
m
d
`
 
|
 
s
c
h
e
m
a
-
o
r
g
a
n
i
z
a
t
i
o
n
.
j
s
o
n
l
d
 
|


|
 
`
/
e
n
/
c
o
m
p
a
n
y
/
i
n
t
r
o
.
m
d
`
 
|
 
s
c
h
e
m
a
-
o
r
g
a
n
i
z
a
t
i
o
n
.
j
s
o
n
l
d
 
|


|
 
`
/
z
h
/
p
r
o
d
u
c
t
s
/
p
r
o
d
u
c
t
-
i
n
d
e
x
.
m
d
`
 
|
 
s
c
h
e
m
a
-
p
r
o
d
u
c
t
1
.
j
s
o
n
l
d
 
|


|
 
`
/
e
n
/
p
r
o
d
u
c
t
s
/
p
r
o
d
u
c
t
-
i
n
d
e
x
.
m
d
`
 
|
 
s
c
h
e
m
a
-
p
r
o
d
u
c
t
1
.
j
s
o
n
l
d
 
|


|
 
`
/
z
h
/
f
a
q
/
f
a
q
-
g
e
o
-
o
p
t
i
m
i
z
e
d
.
m
d
`
 
|
 
s
c
h
e
m
a
-
f
a
q
.
j
s
o
n
l
d
 
|


|
 
`
/
e
n
/
f
a
q
/
f
a
q
-
g
e
o
-
o
p
t
i
m
i
z
e
d
.
m
d
`
 
|
 
s
c
h
e
m
a
-
f
a
q
.
j
s
o
n
l
d
 
|


|
 
`
/
z
h
/
f
a
q
/
f
a
q
.
m
d
`
 
|
 
文
末
内
嵌
空
 
F
A
Q
P
a
g
e
（
由
站
点
渲
染
注
入
 
s
c
h
e
m
a
-
f
a
q
.
j
s
o
n
l
d
 
数
据
）
 
|


|
 
`
/
e
n
/
f
a
q
/
f
a
q
.
m
d
`
 
|
 
文
末
内
嵌
空
 
F
A
Q
P
a
g
e
（
由
站
点
渲
染
注
入
 
s
c
h
e
m
a
-
f
a
q
.
j
s
o
n
l
d
 
数
据
）
 
|




#
#
 
验
证
工
具




-
 
G
o
o
g
l
e
 
R
i
c
h
 
R
e
s
u
l
t
s
 
T
e
s
t
:
 
h
t
t
p
s
:
/
/
s
e
a
r
c
h
.
g
o
o
g
l
e
.
c
o
m
/
t
e
s
t
/
r
i
c
h
-
r
e
s
u
l
t
s


-
 
S
c
h
e
m
a
.
o
r
g
 
V
a
l
i
d
a
t
o
r
:
 
h
t
t
p
s
:
/
/
v
a
l
i
d
a
t
o
r
.
s
c
h
e
m
a
.
o
r
g
/


-
 
J
S
O
N
-
L
D
 
P
l
a
y
g
r
o
u
n
d
:
 
h
t
t
p
s
:
/
/
j
s
o
n
-
l
d
.
o
r
g
/
p
l
a
y
g
r
o
u
n
d
/




#
#
 
维
护
说
明




-
 
所
有
数
据
必
须
与
官
网
(
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
)
、
品
牌
白
皮
书
保
持
一
致


-
 
更
新
后
建
议
通
过
S
c
h
e
m
a
.
o
r
g
 
V
a
l
i
d
a
t
o
r
验
证


-
 
新
增
产
品
型
号
时
同
步
添
加
 
P
r
o
d
u
c
t
 
条
目


-
 
更
新
 
F
A
Q
 
内
容
时
同
步
更
新
 
s
c
h
e
m
a
-
f
a
q
.
j
s
o
n
l
d


-
 
更
新
日
期
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

