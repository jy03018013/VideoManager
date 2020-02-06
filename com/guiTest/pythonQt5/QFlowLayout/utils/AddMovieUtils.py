# import os
# from PyQt5.QtWidgets import QFileDialog, QMessageBox
# import re
#
# from SqlUtils import SqlUtils
# from utils import CommonUtils
#
#
# def _openfolder():
#     try:
#         directory = QFileDialog.getExistingDirectory(None,"选取文件夹", CommonUtils.get_setting_ini_('DEFAULT', 'last_open_folder', "./"))  # 起始路径
#         if directory.strip() == "":
#             return
#         CommonUtils.update_setting_ini_('DEFAULT', 'last_open_folder', directory)
#         process_folder(directory)
#     except Exception as e:
#         print(e)
#         pass
# def process_folder(directory):
#     video_list = []
#     _listdir(directory, video_list)
#     _process_video_list(video_list)
#
# def _openfiles():
#     try:
#         files, file_type = QFileDialog.getOpenFileNames(None, "多文件选择", CommonUtils.get_setting_ini_
#         ('DEFAULT', 'last_open_folder', "./"), "All Files (*)")
#         # files, file_type = QFileDialog.getOpenFileName(self, 'Open File', '',  "All Files (*)",options = QFileDialog.DontUseNativeDialog)
#         if len(files) == 0:
#             return
#         CommonUtils.update_setting_ini_('DEFAULT', 'last_open_folder', files[0])
#         # self._save_last_open_folder(files[0])
#         process_files(files)
#     except Exception as e:
#         print(e)
#         pass
# def process_files(files):
#     video_list = []
#     for file in files:
#         if judge_file_is_movie(file):
#             video_list.append(file)
#     _process_video_list(video_list)
#
# def _process_video_list(video_list):
#     config = CommonUtils.read_config()
#     image_type = config.get('DEFAULT', 'default_img_type')
#     qb_identifier_str = config.get('DEFAULT', 'qb_identifier')
#     qb_identifier_arr = qb_identifier_str.split(",")
#     for _video_path in video_list:
#         _video_path = _video_path.replace("\\", "/")
#         _video_name = _video_path[_video_path.rfind('/') + 1:_video_path.rfind('.')]
#         _hash = _video_name
#         # _hash = file_md5(_video_path)
#         if SqlUtils.hash_exists(_hash):
#             reply = QMessageBox.question(None,"提示框", "数据库中已存在名称相同的视频，是否更新视频路径？",
#                                          QMessageBox.Yes | QMessageBox.No)
#             if reply == QMessageBox.Yes:
#                 sql = "UPDATE video SET video_path = ?,video_name_local=? WHERE hash = ?"
#                 SqlUtils.update_video(sql, (_video_path, _video_name, _hash))
#
#         else:
#             _identifier = ""
#             _serious = ""
#             _video_type = 0
#             try:
#                 _video_type = get_video_type(_video_name, qb_identifier_arr)
#                 if _video_type == 1:
#                     _identifier, _serious = _get_qb_identifier(qb_identifier_arr, _video_name)
#                     print(_video_name + " : " + _identifier)
#                 else:
#                     pass
#             except Exception as e:
#                 print(e)
#                 pass
#             sql = "INSERT INTO video (series,identifier,type,video_name_local,video_path,img_type,hash) VALUES (?,?,?,?,?,?,?)"
#             SqlUtils.update_video(sql,
#                                   (_serious, _identifier, _video_type, _video_name, _video_path, image_type, _hash))
#
#             print(_hash)
#
#
# def _get_qb_identifier(qb_identifier_arr, _video_name):
#     _video_name_upper = _video_name.upper()
#     for series in qb_identifier_arr:
#         try:
#             series_upper = series.upper()
#             if series_upper in _video_name_upper:
#                 pattern = re.compile(str(series_upper) + '(.*?)\d+')  # 用于匹配指定符号及其后的数字及中间的字符串
#                 m = pattern.search(_video_name_upper)
#                 pattern = re.compile('\d+')  # 匹配数字
#                 n = pattern.search(m.group().replace(series_upper, ""))  # 防止300MIUM-010 : 300MIUM-300
#                 num = n.group()
#                 if len(num) > 3:
#                     num = num.lstrip("0")
#                 return (series_upper + "-" + num, series_upper)
#         except Exception as e:
#             print(e)
#             pass
#     print("无法识别：" + _video_name)
#     return ("", "")
#
#
# def get_video_type(_video_name, qb_identifier_arr):
#     _video_name_upper = _video_name.upper()
#     for series in qb_identifier_arr:
#         try:
#             series_upper = series.upper()
#             if series_upper in _video_name_upper:
#                 return 1
#         except Exception as e:
#             print("无法识别：" + _video_name + "  " + e)
#             pass
#     return 0
#
# def _listdir(path, list_name):  # 传入存储的list
#     for file in os.listdir(path):
#         file_path = os.path.join(path, file)
#         if os.path.isdir(file_path):
#             _listdir(file_path, list_name)
#         else:
#             if judge_file_is_movie(file_path):
#                 list_name.append(file_path)
#
# # 判断是不是视频
# def judge_file_is_movie(file_name):
#     return file_name.lower().endswith(('.mp4', '.mkv', '.avi', '.wmv', '.iso', '.rmvb', 'mov', 'rm', '3gp', 'flv'))
