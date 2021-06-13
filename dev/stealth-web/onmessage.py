from py_stealth import *

obj = {"test": "test"}
broadcast = []


async def onMessage(message):
    global obj
    param = ""
    split = message.split()
    if len(split) >= 2:
        param = split[1]

    if "/bark" in split:
        bark()
        log(f"barked")
        return True

    elif "/say" in split:
        edited = message.replace("/say", "")
        log(f"{GetName(Self())}: {edited}")
        say(edited)
        return True

    elif '/useskill' in split:
        UseSkill(param)
        log(f"used skill {param}")
        return True

    elif '/obj' in split:
        log("object changed")
        obj = {'test2': 'test2'}
        return True

    return False


def bark():
    UOSay("Woof")


def say(msg):
    UOSay(msg)


def log(message):
    global broadcast
    broadcast.append(message)
