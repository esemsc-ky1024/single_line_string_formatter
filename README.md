# 单行字符串格式化器 Single-line String Formatter

## 功能

输入正常格式文本（有回车和段首空格）  
输出适合用作json字符串的单行文本（删除回车和段首空格，用\n表示换段）

## 使用场景

我也不确定都有啥场景，反正我自己是在写某游戏同人Mod时感到这个需要的。  
这个游戏的情节都以json文件的形式组织起来，以供程序在运行时读取。改起来非常简单，但是把自己的正常格式文本挤成单行塞进json字符串里这种重复性工作实在有些——就像游戏里某角色时常感叹的那样——无聊，于是就有了这个。  
我不知道有多少游戏是这样组织的，毕竟这是我下载Steam第一个游戏，但是我实在删空字符快删痿了（搞的可明明是一个令人怒然大勃的角色（对不起这个词是跟AO3一位作者学的））而且很好写（功能逻辑就3行）所以不管使用场景广不广泛我都写了。

## 使用方式

下载index.html，双击它，就能用了——只要你装了浏览器。
