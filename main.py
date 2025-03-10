'''

╱╱╱╭━━━┳━━┳━━━╮
╱╱╱┃╭━╮┣┫┣┫╭━━╯
╭━╮┃┃╱╰╯┃┃┃╰━━╮
┃╭╮┫┃╭━╮┃┃┃╭━━╯
┃┃┃┃╰┻━┣┫┣┫┃
╰╯╰┻━━━┻━━┻╯

'''

import sys
import imageio.v2 as imageio
import webbrowser

from numpy import imag # type: ignore
from GUI import *

class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.image_array = []
        self.gifname = "unknow"

        self.pushButton.clicked.connect(self.set_image)
        self.pushButton_3.clicked.connect(self.del_image)
        self.comboBox.currentTextChanged.connect(self.show_image)
        self.actionGitHub.triggered.connect(
            lambda: webbrowser.open_new_tab(
            "https://github.com/KriperPlay/nGIF/")
        )
        self.actionSave.triggered.connect(self.create_gif)
        self.actionNew_File.triggered.connect(self.new_file)

    def set_image(self) -> None:
        wb_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
        if (".png" in wb_patch or ".jpg" in wb_patch or ".jpeg" in wb_patch) and wb_patch not in self.image_array:
            self.label_3.setPixmap(QPixmap(wb_patch))
            self.image_array.append(wb_patch)
            self.comboBox.addItem(wb_patch)
            print(self.image_array)
        else:
            self.label_3.setPixmap(QPixmap(u"imgs/grey.png"))

    def show_image(self) -> None:
        self.label_3.setPixmap(QPixmap(self.comboBox.currentText()))

    def del_image(self) -> None:
        index = self.comboBox.findText(self.comboBox.currentText())

        self.image_array.remove(self.comboBox.currentText())
        self.comboBox.removeItem(index)
        self.label_3.setPixmap(QPixmap(u"imgs/grey.png"))

    def create_gif(self) -> None:
        imgs = [imageio.imread(image) for image in self.image_array]
        imageio.mimsave(
            f'{self.gifname}.gif',
            list(imgs),
            duration=self.spinBox.value()
        )

    def new_file(self) -> None:
        self.gifname = str(QFileDialog.getSaveFileName()[0])
        self.image_array = []
        self.spinBox.setValue(0)
        self.comboBox.clear()
        self.label_3.setPixmap(QPixmap(u"imgs/grey.png"))

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = App()

    window.show()
    app.exec_()

if __name__ == '__main__': main()
