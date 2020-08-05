## redis内存分析工具

[redis-rdb-tools](https://github.com/sripathikrishnan/redis-rdb-tools)

#### 导出rdb每个key的内存占用

```bash
rdb -c memory /var/redis/6379/dump.rdb --bytes 128 -f memory.csv
head memory.csv

# outout
database,type,key,size_in_bytes,encoding,num_elements,len_largest_element
0,list,lizards,241,quicklist,5,19
0,list,user_list,190,quicklist,3,7
2,hash,baloon,138,ziplist,3,11
2,list,armadillo,231,quicklist,5,20
2,hash,aroma,129,ziplist,3,11
```

#### [stat_memory_usage.py](stat_memory_usage.py)
```bash
python stat_memory_usage.py memory.csv

# output
user:extend:* => 635.881 MB
suspension:*:app:* => 134.631 MB
user:bomb:reward:rate:* => 70.771 MB
user:follow:* => 70.220 MB
room:*:share:* => 66.688 MB
app:daily_tasks:* => 54.152 MB
room:ranking:total:* => 34.799 MB
...
```
