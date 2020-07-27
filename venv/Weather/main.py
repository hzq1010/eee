import requests
from lxml import etree
import pandas as pd
import re
url = 'http://www.weather.com.cn/weather1d/101010100.shtml#input'
with requests.get(url) as res:
    content = res.content
    html = etree.HTML(content)
    location = html.xpath('//*[@id="around"]//a[@target="_blank"]/span/text()')
    temperature = html.xpath('//*[@id="around"]/div/ul/li/a/i/text()')

    df = pd.DataFrame({'location': location, 'temperature': temperature})
    print('温度列')
    print(df['temperature'])

    df['high'] = df['temperature'].apply(lambda x: int(re.match('(-?[0-9] * ?) / -?[0 - 9] *?°C', x).group(1) ) )
    df['low'] = df['temperature'].apply(lambda x: int(re.match('-?[0-9] * ? / (-?[0-9] * ?)°C', x).group(1) ) )

    print(df)

    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

    print(m.group(0))
    print(m.group(1))
    print(m.group(2))