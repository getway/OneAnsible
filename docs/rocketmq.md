# rocketmq笔记
## 下载地址
http://mirror.bit.edu.cn/apache/rocketmq/4.2.0/rocketmq-all-4.2.0-source-release.zip
## 解压&编译
```bash
  > unzip rocketmq-all-4.2.0-source-release.zip
  > cd rocketmq-all-4.2.0/
  > mvn -Prelease-all -DskipTests clean install -U
  > cd distribution/target/apache-rocketmq
```
## start Name Server
```bash
nohup sh bin/mqnamesrv &
tail -f ~/logs/rocketmqlogs/namesrv.log
```

## Start Broker
```
nohup sh bin/mqbroker -n localhost:9876 &
tail -f ~/logs/rocketmqlogs/broker.log 
```

## 测试
注意：这里export比较关键，要不然可能在consumer的时候不消费
```
export NAMESRV_ADDR=localhost:9876
sh bin/tools.sh org.apache.rocketmq.example.quickstart.Producer
 SendResult [sendStatus=SEND_OK, msgId= ...

sh bin/tools.sh org.apache.rocketmq.example.quickstart.Consumer
 ConsumeMessageThread_%d Receive New Messages: [MessageExt...
```

