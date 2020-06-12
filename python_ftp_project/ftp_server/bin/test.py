import os
from configparser import ConfigParser
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file = os.path.join(base_dir,'config','user_config')
conf = ConfigParser()
conf.read(file)
print(conf.has_section('Yasin'))
password = '1554698cdf30a005f0b69228c54f3155'
if conf.get('Yasin','password') == password:
    print("成功")
