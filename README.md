## Flask_Bule

### 作为应用运行

#### 建立Python 虚拟环境

```
python3 -m venv VENV
```

#### 使用虚拟环境

```
.\VENV\Scripts\Activate.ps1
```

#### 安装依赖

```
pip install -r requirements.txt
```

#### PS ：生成依赖的命令

```
pip freeze > requirements.txt
```

#### 运行

```
python3 app.py
```

### 作为蓝图运行

复制`liuhuimin_woaini`文件夹到你的应用内

在你的flask应用内添加

```python
from liuhuimin_woaini import liuhuimin_woaini_blue
from flask import Blueprint

app.register_blueprint(liuhuimin_woaini_blue)
```

## VUE_moudle

依据你的环境调整`Vue_moudle\src\services\request.js`的内容，然后：

```
npm  install
npm  run serve
```

当然生产环境是需要build的。

晚安，各位~