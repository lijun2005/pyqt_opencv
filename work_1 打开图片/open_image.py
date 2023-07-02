import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog 
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
# QFileDialog() 是 PyQt5 中的一个类，用于创建文件对话框以便用户选择文件或文件夹。它提供了一个友好的用户界面，可以浏览文件系统并选择所需的文件或文件夹。
# 使用 QFileDialog() 可以按以下步骤执行文件选择操作：
#     创建 QFileDialog 对象：使用 QFileDialog() 创建一个文件对话框对象，例如 file_dialog = QFileDialog()。
#     打开文件对话框：使用 getOpenFileName() 方法来打开文件对话框。该方法有一些参数，包括：
#         parent：指定父级窗口（对话框所属的窗口）。
#         caption：指定对话框的标题。
#         directory：指定对话框打开时显示的默认目录。
#         filter：指定文件过滤器，用于限制用户可选择的文件类型。
#     例如，使用 image_path, _ = file_dialog.getOpenFileName(parent, caption, directory, filter) 来打开文件对话框，并将用户选择的文件路径保存在 image_path 变量中。
#     处理用户选择的文件路径：根据需要，可以对用户选择的文件路径进行进一步处理。例如，可以使用该路径加载图像文件或执行其他操作。
# QFileDialog 类还提供了其他方法，例如 getExistingDirectory() 用于选择文件夹路径，getSaveFileName() 用于选择保存文件的路径等。这些方法和参数可以根据具体需求进行使用。
# 请注意，QFileDialog 是 PyQt5 中的一个类，但也与 Qt 库紧密相关。您可以参考 PyQt5 和 Qt 官方文档以获取更多详细的用法和示例。

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 400, 400)

        self.button = QPushButton("Open Image", self)
        self.button.setGeometry(10, 420, 100, 30)
        self.button.clicked.connect(self.open_image)

    def open_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)")

        if image_path:
            image = cv2.imread(image_path)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.label.setPixmap(pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio))
            
            #pixmap = QPixmap.fromImage(q_image) 这行代码将 QImage 对象 q_image 转换为 QPixmap 对象 pixmap。
            # 在 PyQt5 中，QPixmap 是用于在界面上显示图像的类，而 QImage 则是用于处理和表示图像数据的类。通过将 QImage 转换为 QPixmap，可以方便地在界面上显示图像。
            # QPixmap.fromImage(q_image) 方法将 QImage 对象作为参数，返回一个相应的 QPixmap 对象。这个 QPixmap 对象包含了与 QImage 相同的图像数据，并可以用于在 PyQt5 应用程序的界面上显示图像。
            # 一旦将 QImage 转换为 QPixmap，就可以通过调用 QLabel 的 setPixmap() 方法，将 QPixmap 设置为 QLabel 的显示内容，从而在界面上显示图像。

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
