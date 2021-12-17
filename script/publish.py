import hmac
import json
import os
import sys

import requests
import validators
import yaml

file_path = os.getenv('JIANMU_DSL_FILE_PATH')
url = os.getenv('JIANMU_HUB_URL')
version = os.getenv('JIANMU_VERSION')
image = os.getenv('JIANMU_IMAGE')
ak = os.getenv('JIANMU_HUB_API_AK')
sk = os.getenv('JIANMU_HUB_API_SK')

#  校验hub_url
if not validators.url(url):
    print('error: hub_url格式校验错误，不是一个正确的URL地址')
    sys.exit(1)
if url.endswith("/"):
    url = url[0:len(url) - 1]

try:
    with open(file_path, 'r', encoding="utf-8") as fr:
        dsl_dict = yaml.full_load(fr)
except Exception as e:
    print("error: 解析 yml 文件失败，", e)
    sys.exit(1)

# 修改版本和镜像
if version and not version.isspace():
    if not dsl_dict.get('version'):
        print('error: dsl中不存在version')
        sys.exit(1)
    dsl_dict['version'] = version
if image and not image.isspace():
    if not dsl_dict.get('spec'):
        print('error: dsl中不存在spec')
        sys.exit(1)
    dsl_dict['spec']['image'] = image
dsl = yaml.dump(data=dsl_dict, allow_unicode=True, sort_keys=False)

data = {
    'dsl': dsl
}
json_data = json.dumps(data)
signature = hmac.new(sk.encode('utf8'), json_data.encode('utf8'), 'sha1').hexdigest()

headers = {
    'Content-Type': 'application/json',
    'X-Access-Key': ak,
    'X-Signature': signature
}
response = requests.post(
    url=url + '/hub/upload/node_definitions/versions',
    headers=headers,
    data=json_data
)

if response.history:
    location = response.history[0].headers.get('location')
    print("redirect:", location)
    response = requests.post(url=location, headers=headers, data=json_data)
if response.status_code == 403:
    print('error: 请检查 api key')
    sys.exit(1)
elif response.status_code != 200:
    print(response.text)
    sys.exit(1)

print('发布成功')
