## HTML 超文本标记语言

html 网页的骨架

## XML 可扩展标记语言

设计的宗旨是传输数据，使用自定义标签。

## Xpath 元素定位


使用路径表达式来选取xml文档中的节点和节点集。

- ‘/’  开始表示元素的绝对路径 /AAA/BBB/CCC
- ‘//’ 开始表示选择文档中所有满足“//之后规则的元素（无论层级关系） //BBB
- ‘*’  表示星号之前的路径所定位的元素(全匹配) /AAA/BBB/*
- ‘[]’ 表示限定元素，相当于数组下标 [last()],取集合中的最后一个元素 /AAA/BBB[1] 或 /AAA/BBB[las()]
- @    通过前缀@来指定属性 //@id、//BBB[@id]、//BBB[@name]、//BBB[@*]、//BBB[not(@*)]、//BBB[@id=“b1"]
- |    取合集的并集 //CCC|//BBB 

[更多](http://www.w3school.com.cn/xpath/index.asp)

