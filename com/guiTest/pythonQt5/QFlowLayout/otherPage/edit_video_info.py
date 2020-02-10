import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

import video_info
from SqlUtils import SqlUtils


class edit_video_info(QWidget, video_info.Ui_Form):

    def __init__(self, video_hash):
        super(edit_video_info, self).__init__()
        self.setupUi(self)
        self.video_hash = video_hash
        self.initText(video_hash)
        self.save_pushButton.clicked.connect(self._save_button_on_click)
        self.cancel_pushButton.clicked.connect(self.close)

    def _save_button_on_click(self):
        paramters = (self.identifier_lineEdit.text(), self.series_lineEdit.text(), self.type_lineEdit.text(),
                     self.country_lineEdit.text(), self.img_type_lineEdit.text(), self.video_director_lineEdit.text(),
                     self.publish_time_lineEdit.text(), self.video_length_lineEdit.text(),
                     self.video_zhizuoshang_lineEdit.text(), self.video_faxingshang_lineEdit.text(),
                     self.video_score_lineEdit.text(), self.like_stars_lineEdit.text(), self.video_path_lineEdit.text(),
                     self.title_lineEdit.text(), self.video_name_local_lineEdit.text(), self.custom_tag_textEdit.toPlainText(),
                     self.actor_name_textEdit.toPlainText(), self.video_tag_textEdit.toPlainText(), self.intro_textEdit.toPlainText(),
                     self.video_hash)
        sql = "UPDATE video SET identifier = ?,series = ?,type = ?,country = ?,img_type = ?" \
              ",video_director = ?,publish_time = ?,video_length = ? ,video_zhizuoshang = ?,video_faxingshang = ?,video_score = ?" \
              ",like_stars = ? ,video_path = ?,title = ?,video_name_local = ?,custom_tag = ?,actor_name = ?,video_tag = ?" \
              ",intro = ?  WHERE hash = ?"
        SqlUtils.update_video(sql, paramters)
        self.close()

    def initText(self, video_hash):
        video_list = SqlUtils.select_videos("SELECT * from video where hash = " + '\''+ video_hash +'\'')
        video = video_list[0]
        self.identifier_lineEdit.setText(self.formate_str(video.identifier))
        self.series_lineEdit.setText(self.formate_str(video.series))
        self.type_lineEdit.setText(self.formate_str(video.type))
        self.country_lineEdit.setText(self.formate_str(video.country))
        self.img_type_lineEdit.setText(self.formate_str(video.img_type))
        self.video_director_lineEdit.setText(self.formate_str(video.video_director))
        self.publish_time_lineEdit.setText(self.formate_str(video.publish_time))
        self.video_length_lineEdit.setText(self.formate_str(video.video_length))
        self.video_zhizuoshang_lineEdit.setText(self.formate_str(video.video_zhizuoshang))
        self.video_faxingshang_lineEdit.setText(self.formate_str(video.video_faxingshang))
        self.video_score_lineEdit.setText(self.formate_str(video.video_score))
        self.like_stars_lineEdit.setText(self.formate_str(video.like_stars))
        self.video_path_lineEdit.setText(self.formate_str(video.video_path))
        self.title_lineEdit.setText(self.formate_str(video.title))
        self.video_name_local_lineEdit.setText(self.formate_str(video.video_name_local))
        self.custom_tag_textEdit.setText(self.formate_str(video.custom_tag))
        self.actor_name_textEdit.setText(self.formate_str(video.actor_name))
        self.video_tag_textEdit.setText(self.formate_str(video.video_tag))
        self.intro_textEdit.setText(self.formate_str(video.intro))
        print(video_hash)

    def formate_str(self, colume):
        if colume is None:
            return ''
        return str(colume)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = edit_video_info()
    form.show()
    sys.exit(app.exec_())
