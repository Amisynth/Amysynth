import xfox

@xfox.addfunc(xfox.funcs)
async def repeatMessage(count: str, message: str, *args, **kwargs):
    try:
        count = int(count)
        if count <= 0:
            return ""
        return " ".join([message] * count)
    except ValueError:
        return "Invalid count value"
