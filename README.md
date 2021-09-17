# jianmu-runner-hub

#### 介绍
发布节点定义版本

#### 输入参数
```
hub_url: 发布节点定义版本的地址
dsl_file_path: 节点定义版本dsl文件路径
hub_api_key: 用户ApiKey
```

#### 构建docker镜像
```
# 创建docker镜像
docker build -t jianmudev/jianmu-runner-hub:${version} .

# 上传docker镜像
docker push jianmudev/jianmu-runner-hub:${version}
```

#### 用法
```
docker run --rm \
  -e JIANMU_HUB_URL=xxx \
  -e JIANMU_DSL_FILE_PATH=xxx \
  -e JIANMU_HUB_API_KEY=xxx \
  jianmudev/jianmu-runner-hub:${version} 
```
