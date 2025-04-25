import cv2
import os

def extract_frames(video_path, output_folder, target_width=None, target_height=None, target_fps=None):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # 获取视频帧率
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Original Video FPS: {original_fps}")

    frame_count = 0
    saved_frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No more frames to read or error occurred.")
            break

        # 如果指定了目标宽度和高度，则调整帧的大小
        if target_width and target_height:
            frame = cv2.resize(frame, (target_width, target_height))

        # 检查帧是否为空
        if frame is None:
            print(f"Frame {frame_count} is None, skipping.")
            continue

        # 根据目标帧率保存帧
        if target_fps:
            if frame_count % int(original_fps / target_fps) == 0:
                frame_filename = os.path.join(output_folder, f"{saved_frame_count}.png")
                success = cv2.imwrite(frame_filename, frame)
                if success:
                    print(f"Saved frame {saved_frame_count} to {frame_filename}")
                    saved_frame_count += 1
                else:
                    print(f"Failed to save frame {saved_frame_count}")
        else:
            frame_filename = os.path.join(output_folder, f"{frame_count}.png")
            success = cv2.imwrite(frame_filename, frame)
            if success:
                print(f"Saved frame {frame_count} to {frame_filename}")
            else:
                print(f"Failed to save frame {frame_count}")

        frame_count += 1

    cap.release()
    print(f"Extracted {saved_frame_count} frames to {output_folder}")

if __name__ == "__main__":
    video_path = r"H:\CQ_PROJ\Project_Alpha\Client\Dev\pytest\PYTEST(DONTDELETE!!)\baowu22.mp4"  # 替换为你的MP4文件路径
    output_folder = r"H:\CQ_PROJ\Project_Alpha\Client\Dev\pytest\PYTEST(DONTDELETE!!)\test"  # 替换为你想要的输出文件夹路径
    target_width = 982# 替换为你想要的目标宽度
    target_height = 563  # 替换为你想要的目标高度
    target_fps = 12  # 替换为你想要的目标帧率
    extract_frames(video_path, output_folder, target_width, target_height, target_fps)