import hashlib


def file_md5(filename):
    hmd5 = hashlib.md5()
    fp = open(filename, 'rb')
    hmd5.update(fp.read())
    return hmd5.hexdigest()


if __name__ == "__main__":
    filepath = "D:/BaiduNetdiskDownload/任务050：03利用语言模型生成句子11.mp4"
    hvalue = file_md5(filepath)
    print(hvalue)
