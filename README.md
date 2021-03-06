# jianmu-runner-hub

#### 介绍
发布节点定义版本

#### 发布到建木Hub
通过建木CI执行[hub_publish.yml](https://gitee.com/jianmu-runners/jianmu-runner-list/blob/master/release_dsl/hub_publish.yml) ，可发布到建木Hub

#### 输入参数
```
hub_url: 发布节点定义版本的地址
dsl_file_path: 节点定义版本dsl文件路径
hub_api_ak: 用户ApiKey的Access_Key_Id
hub_api_sk: 用户ApiKey的Secret_Access_Key
version: 版本号，不填写时默认为dsl中定义的版本
image: 镜像，不填写时默认为dsl中定义的镜像
```

#### 构建docker镜像
```
# 创建docker镜像
docker build -t jianmurunner/hub_publish:${version} -f dockerfile/Dockerfile .

# 上传docker镜像
docker push jianmurunner/hub_publish:${version}
```

#### 用法
```
docker run --rm \
  -e JIANMU_HUB_URL=xxx \
  -e JIANMU_DSL_FILE_PATH=xxx \
  -e JIANMU_HUB_API_AK=xxx \
  -e JIANMU_HUB_API_SK=xxx \
  -e JIANMU_VERSION=xxx \
  -e JIANMU_IMAGE=xxx \
  jianmurunner/hub_publish:${version} 
```
