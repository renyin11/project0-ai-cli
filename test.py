import os
from openai import OpenAI
from dotenv import load_dotenv

# 从同目录的 .env 文件里读取配置（也就是你的 Key）
load_dotenv()

# 创建一个客户端：用我的 Key，连到 DeepSeek 的服务器
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 让大模型回一句话
response = client.chat.completions.create(
    model="deepseek-flash",          # 用 DeepSeek 的通用对话模型
    messages=[
        {"role": "user", "content": "你好，请用一句话介绍你自己"}
    ]
)

# 把大模型的回复打印到终端
print(response.choices[0].message.content)
