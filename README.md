# AI CLI Chat

一个命令行 AI 工具，基于 DeepSeek API（兼容 OpenAI SDK）。支持多轮对话、长文本摘要、中英互译三种功能，通过子命令切换。

## 功能

| 命令 | 功能 | 说明 |
|---|---|---|
| `chat` | 多轮对话 | 持续问答，AI 记得上下文；输入「退出」结束 |
| `summarize` | 长文本摘要 | 粘贴多行文本，输出 200 字以内的中文摘要 |
| `translate` | 中英互译 | 自动判断语向，中文译英文，英文译中文 |

## 技术栈

- Python 3.10+
- `openai` SDK（用 `base_url` 指向 DeepSeek，接口与 OpenAI 兼容）
- `python-dotenv`（从 `.env` 读取 API Key）
- `argparse`（标准库，做子命令解析）

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/renyin11/project0-ai-cli.git
cd project0-ai-cli
```

### 2. 创建虚拟环境并安装依赖

```bash
python -m venv venv
source venv/Scripts/activate    # Git Bash
# .\venv\Scripts\Activate.ps1   # PowerShell
pip install -r requirements.txt
```

### 3. 配置 API Key

在项目根目录创建 `.env`：

```
DEEPSEEK_API_KEY=你的Key
```

> Key 在 https://platform.deepseek.com/ 申请，有免费额度。

### 4. 运行

```bash
python cli.py -h                # 查看所有子命令
python cli.py chat              # 进入多轮对话
python cli.py summarize         # 进入摘要模式（多行粘贴，单独一行 END 提交）
python cli.py translate         # 进入翻译模式（交互式）
python cli.py translate "你好"   # 一次性翻译一段文本
```

## 项目结构

```
project0-ai-cli/
├── cli.py             # 命令行入口：argparse 解析子命令并分发
├── commands.py        # 三个功能的具体实现
├── llm.py             # 大模型 client 初始化与统一调用封装
├── test.py            # 最小验证脚本：第一次调通 API 用
├── requirements.txt   # 依赖清单
├── .env               # API Key（不提交到 Git）
└── .gitignore         # 忽略 venv / .env / __pycache__
```

## 效果截图

![运行效果](screenshot.png)

## 踩过的坑

**1. 模型名写错，报 400**

```
openai.BadRequestError: Error code: 400 - The supported API model names are
deepseek-flash, deepseek-v4-pro, but you passed deepseek-v4.1-flash.
```

400 是「请求参数不对」，锅在自己。Traceback 里**最后一行才是真正的错误**，前面都是调用过程。改模型名后正常。

**2. PowerShell 拦住了激活脚本**

```
.\venv\Scripts\Activate.ps1 : 无法加载文件，因为在此系统上禁止运行脚本
```

Windows 默认执行策略不允许跑本地脚本。解决：

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

只对当前用户放开本地脚本，不需要管理员权限。

**3. `.env` 差点被提交上去**

先写好 `.gitignore` 再 `git init`，`git add .` 之后用 `git status` 确认 `.env` 不在暂存区。已经误加的话用 `git rm --cached .env` 从暂存区移除，硬盘上的文件保留。
