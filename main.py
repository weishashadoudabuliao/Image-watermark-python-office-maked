import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui import Ui_Dialog
import office

class Dialog(Ui_Dialog, QMainWindow):
    def __init__(self):
        super(Dialog, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.on_pushbutton)


    def on_pushbutton(self):
        info1 = self.lineEdit.text()
        info2 = self.lineEdit_2.text()
        info3 = self.lineEdit_3.text()

        office.image.add_watermark(file=info1, mark=info2, color=info3)

        msgbox = QMessageBox.information(self, "msg", "已完成!!!请在本目录的output查看")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = Dialog()
    m.show()
    sys.exit(app.exec_())
