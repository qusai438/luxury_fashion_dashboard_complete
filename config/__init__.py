import os

USE_MOCK = os.getenv("MOCK_MODE", "false").lower() == "true"
IS_RENDER = os.getenv("RENDER", "false").lower() == "true"

if USE_MOCK:
    from .mock_config import MockConfig as Config
elif IS_RENDER:
    from .render_config import RenderConfig as Config
else:
    from .local_config import LocalConfig as Config
