from pylab import *
from PIL import Image
import numpy as np


class PhysthonImage:
    # Khi được truyền tham số là url thì hàm khởi tạo __init__ sẽ tạo ra 1 biến nằm trong phạm vi xử lý
    # của class PhysthonImage là self.url
    # Từ khóa self này mục đích là để khai báo các biến thuộc phạm vi class tạo ra nó.
    # Tất cả các phương thức trong class đều phải khai báo tham số self
    def __init__(self, url):
        self.url = url
        self.image_convert = ""
        self.image_original = ""
    # Phương thức open là bắt buộc phải gọi ra trước khi thực hiện các phương thức phía dưới

    def open(self):
        self.image_original = Image.open(self.url)
        return "Mở ảnh thành công"

    # Phương thức này giúp show ra hình ảnh truyền vào dưới dạng màu trắng đen
    def to_gray(self):
        self.image_convert = self.image_original
        self.image_convert = array(self.image_convert.convert('L'))
        gray()
        imshow(self.image_convert)

    def show_of(self):
        if(type(self.image_convert) != 'list'):
            show()
            return True
        else:
            return False

    # Ở đây ta xây dựng một phương thức để có thể chính sửa ảnh tùy ý màu sắc với 3 giá trị tham số truyền vào
    # là R ứng với màu Đỏ, G ứng với màu xanh lá, B ứng với màu xanh dương.

    # Giá trị mặc định truyền vào cho RGB là R,G,B<10000
    def changeColor(self, R=0.1, G=0.1, B=0.1):
	    R = R/1000
	    G = G/1000
	    B = B/1000
        # Khai báo 1 ma trận màu sắc mặc định truyền vào cho hình ảnh chỉnh sửa
	    rgb_matrix = (R, 1.5*R, 0.5*R, 0,
   		       G, 1.5*G, 0.5*G, 0,
		       B, 1.5*B, 0.5*B, 0,)
	    self.image_convert = self.image_original
	    self.image_convert = array(self.image_convert.convert('RGB', rgb_matrix));imshow(self.image_convert)

    # Phương thức xoay tìm điểm xoay ảnh
    def findOriginalPixel(self, angle, rowIndex, colIndex, centerX, centerY):
        x0 = np.cos(angle)*(colIndex - centerX) - np.sin(angle)*(rowIndex - centerY) + centerX
        y0 = np.sin(angle)*(colIndex - centerX) + np.cos(angle)*(rowIndex - centerY) + centerY
        return x0, y0
    # Tiền xử lý trước khi xoay ảnh
    def pre_rotate(self,angle):
        # Do chưa tìm ra cách xoay ảnh màu nên mình convert sang ảnh trắng đen để xử lý
        img = array(self.image_original.convert('L'))
        gray()
        row, col = img.shape
        angle = -angle
        rowOut = row + 500 # + Thêm phần mở rộng cho ảnh khi xoay bị mất góc
        colOut = col + 500 # + Tương tự
        centerX = np.round(col/2)
        centerY = np.round(row/2)
        # index = np.around(img)
        # index = imgOut.astype(int)
        # imgOut
        imgOut = np.empty((rowOut,colOut))
        for i in range(0,row):
            for j in range(0,col):
                x0 ,y0 = self.findOriginalPixel(angle,i,j,centerX,centerY)
                x0 = np.round(x0).astype(int); y0 = np.round(y0).astype(int)
                # if(x0 < 0): imgOut[k,m] =0
                # elif(x0 > col-1): imgOut[k,m] = 0
                # elif(y0 < 0): imgOut[k,m] = 0
                # elif(y0 > row -1): imgOut[k,m] = 0
                # else:
                imgOut[y0+250,x0+250] = img[i,j]
        return imgOut
    
    # Phương thức xoay ảnh và xuất ảnh ra ngoài
    def rotate(self,angle):
        self.image_convert = self.pre_rotate(angle)
        imshow(self.image_convert)
        show()

    # Lưu ảnh. Sẽ lưu lại ảnh được convert sau cùng
    def save_img(self,url):
        im = Image.fromarray(self.image_convert)
        im.save(url)
