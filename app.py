# """
#   Để import 1 file từ trong folder thực thi của chúng ta thì làm theo quy ước sau.
#   from <folder chứa file> import <file>
#   hoặc như phía dưới đây là ta đang muốn lấy hẳn class thì trong file đó ra thì làm như sau
#   from <folder chứa file>.<file> import <class>
# """
#
from modules.physthon_images import PhysthonImage

# url là đường dẫn tới hình ảnh mà ta muốn xử lý
url ='static/img/camgiang.jpg'

#khai báo 1 biến tên là show là đối tượng của class PhysthonImage truyền vào tham số là (url)
show = PhysthonImage(url)
show.open()
show.to_gray()
show.show_of()

show.changeColor(1000,2000,3000)
show.show_of()

show.rotate(45)

show.save_img('static/img/image_save.jpg')