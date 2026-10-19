\# AI CLI Chat



一个命令行 AI 聊天助手，基于 DeepSeek API（兼容 OpenAI SDK），支持多轮对话和上下文记忆。



\## 功能



\- \*\*多轮对话\*\*：输入问题，AI 回复，持续聊天直到输入"退出"

\- \*\*上下文记忆\*\*：AI 记得之前聊过什么

\- \*\*安全\*\*：API Key 通过环境变量管理，不上传到 GitHub



\## 技术栈



\- Python 3.10+

\- openai SDK（兼容 DeepSeek API）

\- python-dotenv（读取环境变量）



\## 快速开始



\### 1. 克隆项目



&#x20;   git clone https://github.com/renyin11/project0-ai-cli.git

&#x20;   cd project0-ai-cli



\### 2. 创建虚拟环境并安装依赖



&#x20;   python -m venv venv

&#x20;   source venv/Scripts/activate

&#x20;   pip install -r requirements.txt



\### 3. 配置 API Key



在项目根目录创建 `.env` 文件，写入：



&#x20;   DEEPSEEK\_API\_KEY=你的DeepSeek API Key



> API Key 在 https://platform.deepseek.com/ 申请。



\### 4. 运行



&#x20;   python main.py



输入问题开始对话，输入"退出"结束。



\## 项目结构



&#x20;   project0-ai-cli/

&#x20;   ├── main.py           # 主程序：多轮对话逻辑

&#x20;   ├── .env              # API Key（不提交到 Git）

&#x20;   ├── .gitignore        # Git 忽略规则

&#x20;   └── requirements.txt  # 依赖列表



\## 示例对话



&#x20;   AI 助手已启动！输入问题开始对话，输入「退出」结束。

&#x20;   你：你好，你是谁？

&#x20;   AI：你好！我是基于 DeepSeek 模型的命令行 AI 助手。

&#x20;   你：我刚才问了什么？

&#x20;   AI：你刚才问我是谁。

&#x20;   你：退出

&#x20;   再见！



