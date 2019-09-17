#### 安装
pip3 install -r ./requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple/

#### 调用
调用 compare_mini.pyc 来生成对比结果。

```
python3 compare_mini.pyc 标注文本.txt  比对文本.txt
```

#### 结果数据说明

| 字段        | 说明                                  |
| ----------- | ------------------------------------- |
| ref         | 标注文本（处理后）                    |
| hpy         | 机转文本（处理后）                    |
| op          | 不用修改的                            |
| op2         | 修改的操作 s 指替换，i指插入，d指删除 |
| s1          | 标注文本（对齐处理前）                |
| s2          | 机转文本（对齐处理后）                |
| D_COUNT_PCT | 删除率                                |
| I_COUNT_PCT | 插入率                                |
| S_COUNT_PCT | 替换率                                |
| accuracy    | 字准                                  |
