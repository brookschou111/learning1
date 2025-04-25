import os
from PIL import Image
from realesrgan import RealESRGAN

def resize_images_with_ai(folder_path, target_resolution):
    # 初始化 Real-ESRGAN 模型
    model = RealESRGAN('cuda', scale=4)  # 使用 GPU（如果没有 GPU，可以改为 'cpu'）
    model.load_weights('RealESRGAN_x4plus.pth')  # 确保下载了预训练模型

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                # 打开图片
                with Image.open(file_path) as img:
                    # 转换为 RGB 模式（Real-ESRGAN 不支持 RGBA）
                    if img.mode != "RGB":
                        img = img.convert("RGB")
                    
                    # 使用 Real-ESRGAN 放大图像
                    sr_image = model.predict(img)
                    
                    # 调整到目标分辨率
                    sr_image = sr_image.resize(target_resolution, Image.LANCZOS)
                    
                    # 保存图像
                    sr_image.save(file_path)
                    print(f"Processed image with AI: {file_path}")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

# 示例用法
folder_path = 'C:/Users/Administrator/Desktop/集字道具'  # 替换为你的文件夹路径
target_resolution = (100, 100)  # 替换为你想要的分辨率
resize_images_with_ai(folder_path, target_resolution)