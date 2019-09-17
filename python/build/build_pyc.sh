# 编译
python -m compileall .

# 删除文件
find -name "__pycache__" -exec rm -f {} \;
find -name "*.py" -exec rm -rf {} \;
