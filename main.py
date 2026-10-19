import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 对话历史，开始时先放一条 system 消息（设定 AI 的人设）
messages = [
    {"role": "system", "content": "你是一个友好的助手，用简洁的中文回答问题。"}
]

print("AI 助手已启动！输入问题开始对话，输入「退出」结束。")

while True:
    # 等你输入一句话
    user_input = input("你：")

    # 如果输入"退出"，就结束循环
    if user_input.strip() == "退出":
        print("再见！")
        break

    # 把你刚说的话，追加到对话历史末尾
    messages.append({"role": "user", "content": user_input})

    # 把完整的对话历史发给大模型
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=messages
    )

    # 取出大模型的回复
    reply = response.choices[0].message.content

    # 把 AI 的回复也追加到对话历史，这样下一轮它才记得自己说过什么
    messages.append({"role": "assistant", "content": reply})

    # 打印出来
    print(f"AI：{reply}")
