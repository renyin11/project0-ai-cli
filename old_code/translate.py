import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

print("=== AI 翻译工具（输入退出结束）===")
print("输入中文翻英文，输入英文翻中文\n")

while True:
    text = input("你要翻译的内容：")
    if text.strip() == "退出":
        print("再见！")
        break

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {
                "role": "system",
                "content": "你是一个专业翻译。自动检测用户输入的语言，如果是中文就翻译成英文，如果是英文就翻译成中文。只输出翻译结果，不要解释。"
            },
            {"role": "user", "content": text}
        ]
    )

    print(f"翻译结果：{response.choices[0].message.content}\n")
