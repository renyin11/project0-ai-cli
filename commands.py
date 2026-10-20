"""三个功能的具体实现：对话、摘要、翻译。

这个文件只管「流程」——怎么读用户输入、怎么拼消息、怎么打印结果。
真正跟模型通信的部分全在 llm.ask() 里，这里一行 API 细节都不碰。
"""

from llm import ask

# 三段提示词提成常量：集中放上面，改措辞不用翻到函数里面找
SYSTEM_CHAT = "你是一个友好的助手，用简洁的中文回答问题。"

SYSTEM_SUMMARIZE = (
    "你是一个专业的摘要助手。请把用户给的长文本压缩成简洁的摘要，"
    "保留关键信息和核心观点，用中文输出，控制在200字以内。"
)

SYSTEM_TRANSLATE = (
    "你是一个专业翻译。自动检测用户输入的语言，如果是中文就翻译成英文，"
    "如果是英文就翻译成中文。只输出翻译结果，不要解释。"
)


def run_chat():
    """多轮对话：维护一个 messages 列表，每轮往里追加，让模型记得上下文。"""
    messages = [{"role": "system", "content": SYSTEM_CHAT}]
    print("AI 助手已启动！输入问题开始对话，输入「退出」结束。")

    try:
        while True:
            user_input = input("你：").strip()

            if not user_input:          # 直接回车，跳过这轮，不发给模型
                continue
            if user_input == "退出":
                print("再见！")
                return                  # return 直接结束整个函数

            messages.append({"role": "user", "content": user_input})
            reply = ask(messages)
            # AI 的回复也要追加进历史，否则下一轮它就忘了自己说过什么
            messages.append({"role": "assistant", "content": reply})
            print(f"AI：{reply}")

    except (KeyboardInterrupt, EOFError):
        # Ctrl+C 或输入流结束：干净退出，不吐 traceback
        print("\n再见！")


def run_summarize():
    """长文本摘要：一次读多行，读到单独一行 END 就提交。"""
    print("=== 摘要模式（粘贴文本后单独一行输入 END 提交，直接 END 退出）===")

    while True:
        print("\n请粘贴要摘要的文本：")
        lines = []

        try:
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
        except (KeyboardInterrupt, EOFError):
            print("\n再见！")
            return

        text = "\n".join(lines).strip()

        if not text:                    # 什么都没粘贴就 END → 退出
            print("再见！")
            return

        result = ask(
            [
                {"role": "system", "content": SYSTEM_SUMMARIZE},
                {"role": "user", "content": text},
            ]
        )
        print("\n=== 摘要结果 ===")
        print(result)


def run_translate(text=None):
    """中英互译。

    传了 text 就翻译这一句就结束（一次性）；
    没传就进交互循环，一句一句翻。
    """
    if text:
        result = ask(
            [
                {"role": "system", "content": SYSTEM_TRANSLATE},
                {"role": "user", "content": text},
            ]
        )
        print(f"翻译结果：{result}")
        return

    print("=== 翻译模式（输入「退出」结束）===")
    print("输入中文翻英文，输入英文翻中文\n")

    try:
        while True:
            user_input = input("你要翻译的内容：").strip()

            if not user_input:
                continue
            if user_input == "退出":
                print("再见！")
                return

            result = ask(
                [
                    {"role": "system", "content": SYSTEM_TRANSLATE},
                    {"role": "user", "content": user_input},
                ]
            )
            print(f"翻译结果：{result}\n")

    except (KeyboardInterrupt, EOFError):
        print("\n再见！")
