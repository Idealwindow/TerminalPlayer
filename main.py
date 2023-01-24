from PIL import Image
import numpy as np
import cv2,os,time
def footage_to_frame(video:str,speed:int) -> list:
    video = os.path.abspath(video)
    vidcap = cv2.VideoCapture(video)
    frames = []
    success, frame = vidcap.read()
    i = 0
    while success:
        if i%speed == 0:
            frames.append(frame)
        success, frame = vidcap.read()
        i += 1
    return frames
def video2text(frame: np.ndarray,dpi: int) -> list:
    gray = []
    text = ["#","8","O","o","=",":","."," "]
    img = Image.fromarray(frame)
    b,g,r = img.split()
    img = Image.merge("RGB", (r,g,b))
    img_array = np.array(img)
    shape = img_array.shape
    for h in range(0,shape[0]//(dpi*2)):
        gray.append([])
        for w in range(0,shape[1]//dpi):
            (r_color,g_color,b_color) = img_array[h*(dpi*2),w*dpi]
            gray[h].append(text[int((r_color*30+g_color*59+b_color*11)/25500*7)])
    return gray
if __name__ == "__main__":
    frames = footage_to_frame(input("输入视频路径"),2)#第二个参数为视频抽帧系数,越大视频越短
    video_text = []
    for frame in frames:
        video_text.append(video2text(frame,9))#video2text函数,调整第2个参数至终端播放的正常水平,越大视频越小
    for i in range(0,len(video_text)): 
        if os.name == 'nt':
            temp = os.system("cls")
        else:
            temp = os.system("clear")
        for j in range(0,len(video_text[0])):
            for k in range(0,len(video_text[0][0])):
                print(video_text[i][j][k],end="")
            print("")
        time.sleep(0.05)
    os.system("pause")
    