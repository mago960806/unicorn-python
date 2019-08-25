# 开发需求列表
- [x] 爬虫
    - [x] 模拟请求接口数据并入库 -> requests
    - [ ] 定时后台运行 -> python-daemon
    - [ ] 数据预处理和去重并归档
- [x] API
    - [x] 读取MongoDB数据库中的数据并返回给客户端
    - [ ] unicorns的restful接口
- [x] 日志 -> logging
    - [x] 日志格式
        - [x] 爬虫日志格式配置
        - [ ] tornado日志格式配置
    - [ ] 日志切片 -> TimedRotatingFileHandler
- [ ] 分页
    - [ ] 基类BasePagination
    - [ ] 实现PageNumberPagination
- [ ] 搜索和过滤中间件 -> 自己实现
    - [ ] 基类BaseFilter
    - [ ] 实现OrderingFilter
    - [ ] 实现SearchFilter
- [ ] 错误上报 -> Sentry
- [ ] 配置 -> Settings

# 安装
## 依赖安装
```bash
# 安装虚拟环境管理工具
pip install pipenv
# 安装依赖
pipenv install
```
# 直接运行
```bash
# 运行tornado后端
python app.py
```
# 简易后台运行
```bash
nohup python app.py &
```

# Docker
```bash
docker build .
```