from typing import Union, Tuple

from pyrogram.types import User, Chat

from pagermaid.enums import Client, Message
from pagermaid.listener import listener


def get_text(opt: str, opt1: str, user1: Union[User, Chat], user2: Union[User, Chat]) -> str:
    first = user1.mention
    second = user2.mention
    return f"{first} {opt} {second} {opt1}!"


def get_second_chat(message: Message, me: User) -> Union[User, Chat]:
    if not message.reply_to_message:
        return me
    reply = message.reply_to_message
    if reply.from_user:
        return reply.from_user
    if reply.sender_chat:
        return reply.sender_chat
    return me


def get_opt(message: Message) -> Tuple[str, str]:
    text = message.arguments
    # 分割命令和参数
    opt, _, opt1 = text.partition(' ')
    # opt1 为空的话给 opt 加个"了"
    if opt and not opt1:
        opt += "了"
    return opt, opt1


@listener(command="qu", description=r"使用“qu”代替“/”,以拙劣地模仿 @fish_quote_reply_bot")
async def qu(bot: Client, message: Message):
    me = await bot.get_me()
    # 分割命令和参数
    opt, opt1 = get_opt(message)
    # opt 为空报错
    if not opt:
        return await message.edit("E:未指定内容")
    user1 = me
    user2 = get_second_chat(message, me)
    text = get_text(opt, opt1, user1, user2)
    await message.edit(text, disable_web_page_preview=True)


@listener(command="uq", description=r"使用“uq”代替“\”,以拙劣地模仿 @fish_quote_reply_bot")
async def uq(bot: Client, message: Message):
    me = await bot.get_me()
    # 分割命令和参数
    opt, opt1 = get_opt(message)
    # opt 为空报错
    if not opt:
        return await message.edit("E:未指定内容")
    user1 = me
    user2 = get_second_chat(message, me)
    text = get_text(opt, opt1, user2, user1)
    await message.edit(text, disable_web_page_preview=True)
