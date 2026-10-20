import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# 把你的 Key 读出来。如果 .env 没配好，这里立刻停下并说人话，
# 而不是拖到调用 API 时才抛一个 401 让你猜。
_api_key = os.getenv("DEEPSEEK_API_KEY")
if not _api_key:
    raise RuntimeError("没有读到 DEEPSEEK_API_KEY，请检查项目根目录下的 .env 文件")

# 全局只建一次 client，所有功能共用它（这也是抽这个文件的意义）
_client = OpenAI(api_key=_api_key, base_url="https://api.deepseek.com")

# 模型名单拎出来放常量：以后换模型只改这一行
MODEL = "deepseek-flash"


def ask(messages: list) -> str:
    """把 messages 发给大模型，返回回复的纯文本。

    messages 的格式是：
        [{"role": "system", "content": "..."},
         {"role": "user",   "content": "..."}]
    """
    response = _client.chat.completions.create(model=MODEL, messages=messages)
    return response.choices[0].message.content
