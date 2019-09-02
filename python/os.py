import os

work_dir = os.getcwd()
print("work_dir",work_dir)
print(os.path.join(os.path.dirname(work_dir), "z_markgo_items"))