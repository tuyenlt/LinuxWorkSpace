import cv2
import numpy

img = cv2.imread("image.jpg")

def getAvrgBrightnessVal(image = cv2.Mat,size = 5):
    HEIGHT, WIDTH = image.shape
    print(WIDTH)
    avrg = 0
    mat01 = []
    for i in range(0,HEIGHT):
        row = []
        for j in range(0,WIDTH):
            avrg += image[i][j] / size
            if (j + 1) % size == 0:
                # avrg /= size
                row.append(avrg)
                avrg = 0
        mat01.append(row)
    res_mat = []
    print(mat01.__len__())
    print(mat01[1].__len__())
    # print(mat01)
    avrg = 0
    for i in range(0,int(WIDTH / size)):
        col = []
        for j in range(0,HEIGHT):
            avrg += mat01[j][i] / size
            if (j + 1) % size == 0:
                # avrg /= size
                col.append(int(avrg))
                avrg = 0
        res_mat.append(col)
    return res_mat  

def getLetterByBrightness(brightness):
    letters = " .:-=+*#%@"         
    index = int((brightness/255)*(letters.__len__())) - 1
    return letters[index]

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cvrt_img = getAvrgBrightnessVal(img,10)
for i in cvrt_img:
    for j in i:
        if j > 255: print(j)        
        # print(getLetterByBrightness(j),end="")
    # print()

# cv2.imshow("dsad",img)
cv2.waitKey()



cv2.destroyAllWindows()