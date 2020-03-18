import os
userName = input('请输入电脑用户名：')
# 文件夹目录
path = r"C:\Users\{}\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\\"\
        .format(userName)
# 图片保存路径
savePath = r'D:\win 壁纸\\'
# 创建文件夹
os.mkdir(savePath)
# 得到文件夹下的所有文件名称
files= os.listdir(path)
for file in files:
    # 打开原图片
    with open(path + file,'rb') as f:
        content = f.read()
    # 保存图片到目标地址
    with open(savePath + file + '.jpg','wb') as p:
        p.write(content)
print('保存成功，在 D 盘名为 “win 壁纸” 的文件夹中~~~')
input('\n回车退出......')
