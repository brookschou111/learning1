import os
from PIL import Image, ImageFilter

def resize_images_in_folder(folder_path, target_resolution):
    # 获取文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, filename)
        
        # 检查文件是否为图片
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                # 打开图片
                with Image.open(file_path) as img:
                    # 转换为支持透明通道的模式（如果不是RGBA模式）
                    if img.mode != "RGBA":
                        img = img.convert("RGBA")
                    
                    # 获取目标分辨率
                    target_width, target_height = target_resolution
                    
                    # 调整图像大小（无论是放大还是缩小）
                    resized_img = img.resize(target_resolution, Image.LANCZOS)
                    
                    # 应用平滑滤镜以减少马赛克感
                    smoothed_img = resized_img.filter(ImageFilter.SMOOTH)
                    
                    # 创建目标尺寸的空白画布（透明背景）
                    new_img = Image.new("RGBA", target_resolution, (0, 0, 0, 0))
                    
                    # 计算居中位置
                    offset_x = (target_width - smoothed_img.size[0]) // 2
                    offset_y = (target_height - smoothed_img.size[1]) // 2
                    
                    # 将调整后的图片粘贴到空白画布上
                    new_img.paste(smoothed_img, (offset_x, offset_y), smoothed_img)
                    
                    # 保存图片
                    new_img.save(file_path)
                    print(f"Processed image: {file_path}")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

# 示例用法
folder_path = 'C:/Users/Administrator/Desktop/集字道具'  # 替换为你的文件夹路径
target_resolution = (100, 100)  # 替换为你想要的分辨率
resize_images_in_folder(folder_path, target_resolution)