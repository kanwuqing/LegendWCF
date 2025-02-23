# LegendWCF 🚀

[**LegendWCF**](https://github.com/kanwuqing/LegendWCF) 是一个基于 [**WCFerry**](https://github.com/lich0821/WeChatFerry) 的 Python 第三方库，旨在优化微信自动操作库的编码体验，并提供更多开发微信机器人时常用的方法与对象。无论你是初学者还是经验丰富的开发者，LegendWCF 都能帮助你更轻松、更高效地构建微信自动化应用

---

## 主要特性 ✨

- **编码体验优化**：对 WCFerry 的 API 进行了封装和优化，降低学习和使用成本
- **新增常用方法**：提供更多实用的方法, 如字典中快速根据键查找、计数等
- **面向对象设计**：通过封装常用对象，简化开发流程
- **易于扩展**：模块化设计，方便开发者根据需求扩展功能

---

## 安装 🛠️

### 使用 pip 快速安装 LegendWCF:

```bash
pip install legendwcf
```

### 使用本地安装:

```bash
pip install wheel
python setup.py sdist build
python setup.py sdist bdist_wheel
python setup.py install
```

---

## 快速上手 🚀 (具体应用请移步[LegendWechatBot](https://github.com/kanwuqing/LegendWechatBot))

### 消息发送 (确保已安装wcferry) 📤

```python
from legendwcf.wcf import *
from wcferry import Wcf

wcf = Wcf()

# 优化前
name1 = wcf.get_alias_in_chatroom('wxid_xxx', 'group@xxx')
name2 = wcf.get_alias_in_chatroom('wxid_yyy', 'group@xxx')
wcf.send_text(f'@{name1} @{name2} 你们好哇', 'group@xxx', 'wxid_xxx,wxid_yyy')


# 优化后(效果一样)
sendMsg(wcf, '你们好哇', 'group@xxx', ['wxid_xxx', 'wxid_yyy'])
```


### 数据快速读写 💾⚡

```python
from legendwcf.data import *

# json文件快速读写 (比原生json更快)
data = read_json('example.json')
data['kanwuqing'] = 'NB'
write_json(data, 'example.json')


# yaml文件快速读写
data = read_yaml('example.yaml')
data['kanwuqing'] = 'NB'
write_yaml(yaml, 'example.yaml')
```

### 文本消息全半角转换 💬
>妈妈再也不担心消息处理会出奇奇怪怪的错了

```python
from legendwcf.wcf import *

content = '。，！（）【】「」？'
content = str_to_half(content)
print(content)  # .,!()[]{}?
```

### 字典值查找 (用于处理 *jieba* 分词结果) 📖🔍

```python
from legendwcf.msg import *

example = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1, 'f': 1}
print(get_key(example, 1, 2)) # 'f'
print(get_keys(example, 1)) # ['a', 'e', 'f']
print(count_key(example, 1)) # 3
```

---

## 进阶功能 🛠️

### 敏感词检测 (DFA) ⚠️🚫
>算法来自[zbt](https://blog.csdn.net/weixin_39666736/article/details/104903518)
```python
from legendwcf.dfa import *

s = '阿弥陀佛观世音如来神掌' # 佛教人士请注意, 这里的代码没有歧视佛教等意见, 宗教不宜在公众范围内不受控制传播, 故将所有已知宗教列入敏感词
dfa_filter = SensitiveFilter('src/text/ban.txt')
print(dfa_filter.checkSensitiveWord(s, 0)) # 4
print(dfa_filter.getSensitiveWord(s)) # ['阿弥陀佛', '观世音', '如来']
print(dfa_filter.replaceSensitiveWord(s)) # *********神掌

dfa_filter.add('你好') # 往词库中添加'你好'敏感词
print(dfa_filter.replaceSensitiveWord('你好')) # **

dfa_filter.delete('你好') # 从词库中删除'你好'敏感词
print(dfa_filter.replaceSensitiveWord('你好')) # 你好
```

### 定时任务 ⏰
>cron完整参数格式见[官方文档](https://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html#module-apscheduler.triggers.cron)

>cron中文参数文档见[APScheduler官方文档翻译](https://blog.csdn.net/weixin_42881588/article/details/111401799)
```python
from legendwcf.job import *
from datetime import datetime
import time

job = LegendJob({'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '20'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '5'
    }}) # 线程池最多同时运行20个线程的任务, 进程池最多同时运行5个进程的任务

def p(x):
    print(x)

job.one_time_job(p, datetime_=datetime(2025, 11, 12, 0, 0, 0), args=['一句冰冷的生日快乐'])

job.interval_job(p, seconds=2, args=['又是两秒过去...'])

job.cron_job(p, standard_cron='0 0 1-15 may-aug *', args=['每年5~8月1~15日0点0分输出'])

job.start() # 启动任务

for i in range(10):
    time.sleep(1) # 保持程序不退出, 实际有机器人消息监听就不用这样

job.shutdown()
```

### 日志集成 📅
对微信~~懒~~机器人提供的真正开箱即用的日志模板, 内涵控制台日志、完整日志、错误日志

```python
from legendwcf.wcf import *
import logging

SetLegendLogging() # 其实就是这么简单, 源代码有彩蛋
```

## todo ⏱️
>## 代码要一行行写, 功能要一个个实现, 莫急莫急

### 不完整的自然语义处理 🧠
建议配合[字典操作](#字典值查找-用于处理-jieba-分词结果-)共同食用
```python
from legendwcf.msg import *

nlp = LegendJieba()
print(nlp.strtime('2025年11月12日13点14')) # ('2025-11-12', '13:14')
print(nlp.strtime('2025年11月12日13点14分')) # ('2025-11-12', '13:14')
```

### 未开始的数据库读写与查询操作 🧾

---

## 未来计划 📝
### 投稿csdn, 知乎等博客平台
### 完成todo的内容

---

## 建议与支持 📚

如果有任何问题或建议，欢迎提交 [Issue](https://github.com/kanwuqing/legendwcf/issues) ~~或加入我们的 [微信机器人技术讨论群(暂未开放)](https://github.com/kanwuqing/LegendWechatBot)~~

---

## 贡献指南 🤝

我们非常欢迎社区贡献! 以下是贡献的步骤：

1. Fork 项目仓库
2. 创建你的分支 (`git checkout -b branchname`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin branchname`)
5. 提交 Pull Request

请确保你的代码符合项目的编码规范，并附上详细的说明。

---

## 许可证 📜

LegendWCF 遵循 **MPL 许可证**。详情请查看 [LICENSE](https://github.com/kanwuqing/legendwcf/blob/main/LICENSE) 文件。

---

## 致谢 🙏

感谢 [WCFerry](https://github.com/lich0821/WeChatFerry) 项目提供的基础支持，以及所有社区的贡献者！

---

**LegendWCF - 让你的微信自动化开发更轻松！** 🚀