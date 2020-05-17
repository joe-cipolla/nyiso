import chart_studio as cs
from dashboard import params

cs.tools.set_credentials_file(username=params.cs_user_name, api_key=params.cs_api_key)
cs.tools.set_config_file(world_readable=False, sharing='secret')

