import pandas as pd
  # 替换为你的应用名称和模型名称
import os
import django
from user.models import User
# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 's_a.settings')  # 替换为你的项目名称
django.setup()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 拼接文件路径
csv_file_path = os.path.join(BASE_DIR, '/Users/garry/Desktop/S_A/s_a/data/USER.csv')
df = pd.read_csv(csv_file_path)

# 将数据保存到模型中
for _, row in df.iterrows():
    User.objects.create(
        index=row["index"],
        PID=row["PID"],
        Fname=row["Fname"],
        Lname=row["Lname"],
        Age=row["Age"],
        Phone=row["Phone"],
        Email=row["Email"],
        # Cd_account=row["Cd_account"]
    )

print("数据导入成功!")
