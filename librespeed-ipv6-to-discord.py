import requests
import datetime

import subprocess
from subprocess import PIPE
import json

webhook_url = 'DISCORD_ENDPOINT'

speedtest = subprocess.run("/usr/local/bin//librespeed_speedtest-cli/librespeed-cli --json --share --chunks 1000 --timeout 60 --secure --local-json /usr/local/bin//librespeed_speedtest-cli/custom-sv-ipv6.json --telemetry-json /usr/local/bin//librespeed_speedtest-cli/telemetry.json", shell=True, stdout=PIPE, stderr=PIPE, text=True)
speedtest_result = speedtest.stdout

speedtest_json = json.loads(speedtest_result)

#data get and input
ping = speedtest_json['ping']
download = speedtest_json['download']
upload = speedtest_json['upload']
url = speedtest_json['share']

#Debug print
#print(ping)
#print(download)
#print(upload)
#print(url)

#result text
ping_text = str(ping) + "ms"
download_text = str(download) + "Mbps"
upload_text = str(upload) + "Mbps"

#Debug print
#print(ping_text)
#print(download_text)
#print(upload_text)

#date get
dt_now = datetime.datetime.now()

year = dt_now.year
month = dt_now.month
day = dt_now.day
hour = dt_now.hour

date_get = str(year) + "年" + str(month) + "月" + str(day) + "日" + str(hour) + "時"

#Debug print
#print(year)
#print(month)
#print(day)
#print(hour)
#print(date_get)

#footer
footer_text = "© " + str(year) + "YourName"

#Debug print
#print(footer_text)

#content
content="Home Network\n【定期スピードテスト】\n" + str(date_get) + "の結果は以下の通りです"

#Debug print
#print(content)

main_content = {
    "content": content,
    "embeds": [
        {
            "title": "inonius Speedtest(IPv6)",
            "url": url,
            "color": 5620992,
            "footer": {
                "text": footer_text
            },
            "image": {
                "url": url
            },
            "fields": [
                {
                    "name": "Ping",
                    "value": ping_text,
                    "inline": True
                },
                {
                    "name": "Download",
                    "value": download_text,
                    "inline": True
                },
                {
                    "name": "Upload",
                    "value": upload_text,
                    "inline": True
                }
            ]
        }
    ]
}

requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})
