import os, sys, hashlib

_FILE_SLIM = (100 * 1024 * 1024)


def file_md5(filename):
    calltimes = 0
    hmd5 = hashlib.md5()
    fp = open(filename, 'rb')
    f_size = os.stat(filename).st_size
    if f_size > _FILE_SLIM:
        while (f_size > _FILE_SLIM):
            hmd5.update(fp.read(_FILE_SLIM))
            f_size /= _FILE_SLIM
            calltimes += 1
        if (f_size > 0) and (f_size < _FILE_SLIM):
            hmd5.update(fp.read())
    hmd5.update(fp.read())
    return hmd5.hexdigest()


if __name__ == "__main__":
    filepath = "D:/BaiduNetdiskDownload/1-50\任务050：03利用语言模型生成句子.mp4"
    hvalue = file_md5(filepath)
    print(hvalue)
