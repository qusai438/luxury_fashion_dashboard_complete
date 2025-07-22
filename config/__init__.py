import os

if os.environ.get("RENDER") == "true":
    from .render_config import RenderConfig as Config
else:
    from .local_config import LocalConfig as Config
