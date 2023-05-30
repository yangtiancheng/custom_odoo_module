import base64
import requests

url = 'http://iface.dingyi-china.cn:18922/api/hly/token'
url = 'https://iface.dingyi-china.cn/api/hly/token'

headers = {'Authorization': 'Basic NjA2OTkzYjctZmU4ZC00ZjA5LTkwN2YtYTg3YmYyOTk5YTI5Ok5URmlaV0k1WlRRdE56RXdOaTAwT0RrNExUbG1OR0l0TXpJNE4yUXpZalpoTVdJNDE=', 'service-token': 'xlig5JUaRY1nfaKygJhz3pbxFiD7Nqx8fXxZPQ1vThLb4eUwjWfwhzwh6WlhUbSXJLANhudRCnv4KlW3GZaxIKC0fYqBd9UbxaSact1+CbI1i681T+L/Y+sAk3+0f4sm'}
response = requests.post(url, headers=headers)
print(response.text.encode().decode("unicode_escape"))
