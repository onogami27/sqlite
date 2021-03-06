import cv2
import numpy as np
import os

count = 0

#カレントディレクトリのパスを取得する
def get_path(path):
    file_list = []
    #カレントディレクトリを移動する
    os.chdir(path)
    #ディレクトリ内のファイルを取得
    file_path = os.listdir(path)
    for i in file_path:
        #絶対パスで表示させる
        x = os.path.abspath(i)
        file_list.append(x)
    
    return file_list


num = 1
def main(img_path):
    #写真データ読み込み
    img = cv2.imread(img_path)
    
    pt_1 = []
    pt_2 = [] 
    total = [] 
    num = [0]

    #マウスイベント関数        
    def event_mouse(event, x, y,a,b):
        global  count , aa , bb
        
        count = count

        if event == cv2.EVENT_LBUTTONDOWN:
            count += 1 #左クリックするとcountが1プラスされる
            
            #1クリック目のイベント処理
            if count == 1:
                pt_1.append((x,y))
                total.append(x)
                total.append(y)
                cv2.circle(img, (x,y), 1,(255,0,0),thickness=2)
                
                cv2.imshow("",img)
                
            #2クリック目のイベント処理
            if count == 2:
                pt_2.append((x,y))
                total.append(x - pt_1[0][0])
                total.append(y - pt_1[0][1])
                cv2.circle(img, (x,y), 1,(255,0,0),thickness=2)
                cv2.rectangle(img, pt_1[0],pt_2[0],(0,0,255),thickness=3)
                cv2.imshow("",img)
                #print(pt_1,pt_2)
                #print(total)
            
                #リセットする
                count = 0
                pt_1.clear()
                pt_2.clear()
                num[0] += 1
                
    
                
        if event == cv2.EVENT_MOUSEMOVE:  # マウスが移動したときにx線とy線を更新する
            if count == 0:
                
                img2 = np.copy(img)
                h, w = img2.shape[0], img2.shape[1]
                cv2.line(img2, (x, 0), (x, h - 1), (255, 0, 0))
                cv2.line(img2, (0, y), (w - 1, y), (255, 0, 0))
                cv2.imshow("", img2) 
                
            if count == 1:
                
                img2 = np.copy(img)
                h, w = img2.shape[0], img2.shape[1]
                cv2.rectangle(img2, pt_1[0], (x,y), (255,0,0),thickness=1)
                #cv2.line(img2, pt_1[0], (x, pt_1[0][1]), (255, 0, 0))
                #cv2.line(img2, pt_1[0], (pt_1[0][0], y), (255, 0, 0))
                cv2.imshow("", img2) 
        
               
                
    cv2.imshow("", img)

    #マウスイベント（コールバック関数）を定義
    cv2.setMouseCallback("", event_mouse,)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return {"total" :total , "num" :num[0]}

file_path = get_path(r"C:\Users\onoga\desktop\test_pic")
lec = ""
#メイン
for i in file_path:
    mes = main(i)
    total = mes["total"]
    num = mes["num"]
    for ff in total:
        lec = lec + f" {ff}"
    final = f"{num}",lec
    #f = open("poslist.txt", "w")
    
    #f.write(f"{i},{final[0]},{final[1]}\n")
    #f.close()
    file_name = os.path.join(os.getcwd(),"poslist.txt")
    f = open(file_name, "a")
    f.write(f"{i} {final[0]}{final[1]}\n")
 
    lec = ""
    
