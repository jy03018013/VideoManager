import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QCheckBox

import video_info
from SqlUtils import SqlUtils


class edit_video_info(QWidget, video_info.Ui_Form):

    def __init__(self, video_hash):
        super(edit_video_info, self).__init__()
        self.setupUi(self)
        self.initText(video_hash)

    def initText(self, video_hash):
        video_list = SqlUtils.select_videos("SELECT * from video where hash = " + video_hash)
        video = video_list[0]
        self.shibiema_lineEdit.setText(str(video.identifier))
        self.xilie_lineEdit_2.setText(str(video.series))
        self.leixing_lineEdit_3.setText(str(video.type))
        self.guojia_lineEdit_8.setText(str(video.country))
        self.fengianleixing_lineEdit_10.setText(str(video.img_type))
        self.daoyan_lineEdit_12.setText(str(video.video_director))
        self.faxingshijian_lineEdit_13.setText(str(video.publish_time))
        self.yingpianshichang_lineEdit_14.setText(str(video.video_length))
        self.zhizuoshang_lineEdit_15.setText(str(video.video_zhizuoshang))
        self.faxingshang_lineEdit_16.setText(str(video.video_faxingshang))
        self.pingfen_lineEdit_17.setText(str(video.video_score))
        self.xiaichengdu_lineEdit_7.setText(str(video.like_stars))
        self.yingpianlujing_lineEdit_9.setText(str(video.video_path))
        self.faxingbiaoti_lineEdit_11.setText(str(video.title))
        self.bendimingcheng_lineEdit_4.setText(str(video.video_name_local))
        self.zidingyibiaoqian_textEdit_3.setText(str(video.custom_tag))
        self.yanyuan_textEdit_2.setText(str(video.actor_name))
        self.guanfangbiaoqian_textEdit_4.setText(str(video.video_tag))
        self.jianjie_textEdit.setText(str(video.intro))
        print(video_hash)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = edit_video_info()
    form.show()
    sys.exit(app.exec_())
