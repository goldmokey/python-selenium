## ide录制 – 如何使用selenium的IDE

[Download](http://seleniumhq.org/download)

### 录制测试用例

开启插件，默认是开启录制。Selenium IDE使用关键字驱动的测试方法。

- Command  表示要执行的操作是什么
- Target   表示要操作的界面元素是哪个
- Value    表示操作时使用的值是什么

### 编写测试用例

通过关键字分别设置不同的值，来组织用例的执行顺序。

### Command

    > 用于测试UI元素是否存在、验证指定内容是否正确、检查链接是否可用，并可以输入字段、选择列表的选项、提交表单并操作表格中的数据。

    > 验证窗口大小、鼠标位置、警告信息、Ajax功能、弹出窗口、事件处理以及其他

    > Selenium命令分3钟类型：Action(操作)、Accessor(存储)、Assertion(断言)

#### Action

1. 浏览器操作

    - open(url)
    - goBack() 
    - refresh()
    - windowFocus() 激活当前选中的浏览器窗口
    - windowMaximize()
    - close()

2. 界面元素的基本操作

    - type(locator,value) input类型的元素中输入值
    - typeKeys(locator,value) 模拟键盘敲击事件
    - click(locator)
    - clickAndWait() 单击动作会导致页面重新加载使用该Action
    - clickAt(locator,coordString) 带坐标的点击
    - doubleClick(locator)
    - select(selectLocator,optionLocator) 下拉列表框中选择指定选项
    - check(locator) 勾选复选框或单选框
    - uncheck(locator)
    - focus(locator) 焦点转移

3. 键盘鼠标模拟操作

    |名称|作用|参数|
    |-|-|-|
    |altKeyDown()|模拟按下Alt键不放，直到调用altKeyUp命令或加载新的页面|无|
    |altKeyUp()|松开Alt键|无|
    |controlKeyDown()|||
    |controlKeyUp()|||
    |shiftKeyDown()|||
    |shiftKeyUp()|||
    |keyDown(locator,keySequence)|模拟按下某个键不放，直到执行keyUp命令|Target - 元素的定位表达式、Value - 要输入的字符串，是按键的ASCII编码|
    |keyPress(locator,keySequence)|模拟用户敲击了某个按键||
    |keyUp(locator,keySequence)|模拟松开某个键||
    |mouseDown(locator)|模拟用户在指定元素上按下鼠标左键不放||
    |mouseDownAt(locator,coordString)|和mouseDown命令相同，区别是需要填写相对坐标||
    |mouseDownRight(locator)|指定元素右键不放||
    |mouseDownRightAt(locator,coordString)|根据相对坐标进行右键不放||
    |mouseUp(locator)|松开之前使用mouseDown在指定元素上按下的鼠标左键||
    |mouseUpAt(locator,coordString)|松开之前使用mouseDownAt在指定元素上按下的鼠标左键||
    |mouseUpRight(locator)|松开之前使用mouseDownRight在指定元素上按下的鼠标右键||
    |mouseUpRightAt(locator,coordString)|松开之前使用mouseDownRightAt在指定元素上按下的鼠标右键||
    |mouseOver(locator)|将鼠标光标移动到指定元素内||
    |mouseOut(locator)|将鼠标光标移动到指定元素外||
    |示例：Ctrl+Alt+C CtrlKeyDown + AltKeyDown + KeyDown |


4. 设置类操作

    - setTimeOut(timeout) 适用 open()、waitFor开头、AndWait后缀
    - setSpeed(value) 测试执行速度

5. 测试控制/调试类操作

    - pause(waitTime)
    - break()
    - captureEntirePageScreenshot(filename,kwargs) 当前窗口截屏并保存为.PNG文件
    - highlight(locator) 增强元素背景色
    - echo(message) 打印信息

#### Accessor

Accessor命令用于检查应用程序的状态，并将结果存储在变量中。变量的值可以用“${变量名称}”来读取。

    - store(expression,variableName) 将指定的值存储在变量中
    - storeTitle(variableName) 存放当前网页的标题
    - storeLocation(variableName) 用于存储当前网页的URL
    - storeValue(locator,variableName) 存储input元素所存放的值 （on-勾选\off-未勾选）
    - storeEditable(locator,,variableName) 存储input元素的可编辑状态
    - storeText(locator,variableName) 用于存储某个元素的文本值（例如链接、纯文本）
    - storeChecked(locator,variableName)
    - storeSelectedIndex(selectLocator,variableName) 获取所选项在列表中的索引（从0开始）
    - storeSelectedLabel(selecLocator,variableName) 获取指定列表中所选项的文本值
    - storeSelectedValue(selectLocator,variableName) 获取指定列表中所选项的真实值
    - storeSelectedOption(selectLocator,variableName) 获取指定列表中所有选项的文本，以逗号隔开
    - storeTable(tableCellAddress,variableName) 其中Target的格式为“表格的定位表达式.行号.列号”，行号和列号都从0开始
    - storeAttribute(attributeLocator,variableName) 获得指定属性的值 Target为属性的定位表达式：”元素定位表达式@属性名称“
    - storeTextPresent(pattern,variableName) 验证指定的文本是否在页面出现
    - storeElementPresent(locator,variableName) 验证指定元素是否存在页面中
    - storeVisiable(locator,variableName) 验证页面元素是否存在（visibility:hidden/display:none）
    - storeSpeed(variableName) 获取执行速度

#### Assertion

    验证某一个结果。所有的assertion命令都可以通过3种模式使用：assert、verify和waitFor。

    > assert失败，测试会中断verify失败，失败将记录下来，测试依然会继续执行。
    > 建议单个assert来确认当前应用程序是否位于正确的页面，然后接下来使用一系列verify命令来测试表单字段的值、标签值。
    > waitFor命令用于执行等待，直到等待的条件为真（非常适合测试Ajax应用程序）

    1. 验证网页的标题是否等于或不等于预期值 assertTitle(pattern)
    2. 验证网页的URL是否等于或不等于预期值 assertLocation(pattern)
    3. 验证input元素的值是否等于或不等于预期值 assertvalue(locator，pattern)
    4. 验证input元素的可编辑状态是否为预期状态 assertEditable(locator)
    5. 验证某个元素的文本值是否等于预期值 assertText(locator，pattern)
    6. 验证复选框或单选框的勾选情况是否符合预期 assertChecked(locator)
    7. 验证所选项在列表中的索引是否符合预期值 assertSelectedIndex(selectLocator,pattern)
    8. 验证指定列表中所选项的文本值是否符合预期值 assertSelectedLabel(selectLocator,pattern)
    9. 验证指定列表中所选项的真实值（value属性）是否为预期值 assertSelectedValue(selectLocator,pattern)
    10. 验证指定列表中所有选项的文本是否符合预期值 assertSelectOptions(selectLocator,pattern)
    11. 验证表格（table元素）中某个单元格（td元素）的值是否为预期值 assertTable(tableCellAddress,pattern)
    12. 验证指定属性的值是否为预期值 assertAttribute(attributeLocator,pattern)
    13. 验证指定的文本是否在页面中出现 assertTextPresent(pattern)
    14. 验证指定元素是否存在于页面上 assertElementPresent(locator)
    15. 验证页面中是否显示指定元素 assertVisible(locator)

#### Target

1. identifier定位

> 最常见的元素定位方式，首先寻找首个id属性，然后寻找首个name属性，如果都没找到，就定位失败

2. id定位

3. name定位

4. XPath定位

XPath表达式用于在xml文档中定位节点。表达式以“//”开头。//input[@name='continue'][@type='button']

5. 链接文字定位

 - link=Continue

6. DOM定位

    DOM用于描述HTML文档，可以通过JavaScript进行访问。该定位方式需要JavaScript来计算出元素在页面，通过分级符号（.）可以轻松定位元素。
    由于只有DOM定位才会在开头使用“document"。

    - document.getElementById('id')
    - document.froms['id']
    - document.forms[0].name
    - document.forms[0].elements['name']

    [了解更多](http://www.w3schools.com/HTMLDOM/dom_reference.asp)

7. CSS定位

    CSS(Cascading Style Sheets)描述HTML和XML文档显示方式的语言。CSS使用选择器来为文档中的元素绑定样式属性。

    [更多关于CSS选择器](http://www.w3.org/TR/css3-selectors)

    > 推荐使用CSS定位，这种方式比Xpath更快，更容易找到在HTML中的复杂对象。

8. 隐式定位

    > 在遇到以下情况时，Target表达式中可以省略“定位类型=”
    - 没有指定定位方式，默认使用identifier
    - 如果以“//”开头，则会使用Xpath
    - 如果以“document”开头，则会使用DOM定位

#### Value

1. 带变量的字符串 

    |Command|Target|Value|
    |-|-|-|
    |store|Bill|firstName|
    |store|Gates|lastName|
    |open|http://www.baidu.com||
    |type|id=kw|Full name is:${firstName} ${lastName}|

2. 带JavaScript的字符串

    |Command|Target|Value|
    |-|-|-|
    |store|Bill|firstName|
    |store|Gates|lastName|
    |open|http://www.baidu.com||
    |type|id=kw|javascript{"Full name is:"+storedVars["firstName"].toUpperCase()+""+storeVars["lastName"].toUpperCase()}|

#### 日志与引用

Log|Reference|UI-Element|Rollup

#### 命令复制与导出为代码

- 复制不同源码的代码
- 导出不同源码的代码



