"""命令行入口：解析参数，把命令分发到 commands.py 里的三个函数。

用法：
    python cli.py -h
    python cli.py chat
    python cli.py summarize
    python cli.py translate
    python cli.py translate "你好"

这个文件只干一件事：读懂命令行，然后叫对应的函数。
它不知道对话怎么实现、翻译怎么调模型，那是 commands.py 的事。
"""

import argparse

from commands import run_chat, run_summarize, run_translate


def build_parser():
    """按「菜单」的方式描述这个工具：有哪些子命令，各自要什么参数。"""
    parser = argparse.ArgumentParser(
        description="命令行 AI 工具：对话 / 摘要 / 翻译"
    )

    # 子命令组。-h 里那个 {chat,summarize,translate} 就是它生成的。
    # dest="command" → 解析结果存进 args.command
    # required=True  → 一个子命令都不给时，自动报错并打帮助，而不是默默什么都不做
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("chat", help="多轮对话，输入「退出」结束")
    sub.add_parser("summarize", help="长文本摘要，多行粘贴后单独一行输入 END")

    # translate 单独拿出来，因为它多一个可选参数
    p_translate = sub.add_parser("translate", help="中英互译，自动判断语向")
    p_translate.add_argument(
        "text",              # 参数名 → 解析后是 args.text
        nargs="?",           # ? = 可给可不给，不给就是 None
        help="要翻译的文本；不填则进入交互模式",
    )

    return parser


def main():
    parser = build_parser()      # 第一步：造好「菜单」
    args = parser.parse_args()   # 第二步：拿用户敲的命令去对菜单，结果装进 args

    # args.command 就是用户敲的那个子命令名字
    if args.command == "chat":
        run_chat()
    elif args.command == "summarize":
        run_summarize()
    elif args.command == "translate":
        # 带了文本就传进去，没带就是 None，函数自己会处理
        run_translate(args.text)


# 只有「直接运行 python cli.py」时才执行 main()；
# 被别的文件 import 时不执行。
if __name__ == "__main__":
    main()
