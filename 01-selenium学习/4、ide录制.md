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
|altKeyDown()|||

4. 