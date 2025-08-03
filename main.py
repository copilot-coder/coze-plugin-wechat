from fastapi import FastAPI
from pydantic import BaseModel
from wxauto import WeChat
import uvicorn

app = FastAPI()
wx = WeChat()


class SendWechatMsgRequest(BaseModel):
    who: str
    msg: str


@app.post("/send_wechat_msg")
async def send_wechat_msg(req: SendWechatMsgRequest):
    wx.ChatWith(req.who)
    resp = wx.SendMsg(req.msg, req.who)
    return resp


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
