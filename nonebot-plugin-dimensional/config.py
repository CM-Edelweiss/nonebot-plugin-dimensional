from nonebot import get_driver
from pydantic import BaseModel, Extra

class Config(BaseModel, extra=Extra.ignore):
     ai_draw_cooldown: int = 30

plugin_config = Config.parse_obj(get_driver().config)

cooldown_time = plugin_config.ai_draw_cooldown