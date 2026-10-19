import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

print("=== AI 摘要工具（直接输入 END 退出）===")

while True:
    print("\n请粘贴要摘要的文本，粘贴完后单独一行输入 END：")

    # 内层循环：读多行，直到读到 END
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    text = "\n".join(lines)

    # 如果什么都没输就 END，就退出
    if not text.strip():
        print("再见！")
        break

    # 调用 AI
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {
                "role": "system",
                "content": "你是一个专业的摘要助手。请把用户给的长文本压缩成简洁的摘要，保留关键信息和核心观点，用中文输出，控制在200字以内。"
            },
            {"role": "user", "content": text}
        ]
    )

    print("\n=== 摘要结果 ===")
    print(response.choices[0].message.content)
