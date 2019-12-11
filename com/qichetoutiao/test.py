import numpy as np
import cv2 as cv
import nltk

def matchTemplate_demo():
    np.random.rand()

    tpl = cv.imread('1_tpl.jpg')
    target = cv.imread('1.jpg')
    # cv.namedWindow('matchTemplate_demo', cv.WINDOW_AUTOSIZE)
    # cv.imshow('matchTemplate_demo',tpl)
    # cv.namedWindow('matchTemplate_demo', cv.WINDOW_AUTOSIZE)
    # cv.imshow('matchTemplate_demo', target)
    #定义3中标准匹配方法
    methods = [cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]
    tpl_h , tpl_w = tpl.shape[:2]    #取模板图片的高 宽
    for method in methods:
        result = cv.matchTemplate(target,tpl,method)
        #返回的 minVal, maxVal （模板与目标图片像素匹配的最小值 最大值）, minLoc, maxLoc（最小和最大位置）
        #打印出minVal, maxVal, minLoc, maxLoc： 0.0004309755750000477 1.0 (466, 185) (395, 327)
        minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)
        print(minVal, maxVal, minLoc, maxLoc)
        if method == cv.TM_SQDIFF_NORMED:
            tl = minLoc
        else:
            tl = maxLoc
        # 当时用第一种cv.TM_SQDIFF_NORMED匹配方法时：br是矩形左上角的坐标
        # 当时用第二种cv.TM_CCORR_NORMED第三种cv.TM_CCOEFF_NORMED匹配方法时：br是矩形左上角的坐标
        print(tl)
        br = (tl[0]+tpl_w,tl[1]+tpl_h)
        #在target图片上绘制tl+br矩形，红色，线宽2
        cv.rectangle(target,tl,br,(0,0,255),2)
        cv.namedWindow('match-'+np.str(method),cv.WINDOW_NORMAL)
        cv.imshow('match-'+np.str(method),target)


matchTemplate_demo()

cv.waitKey(0)
cv.destroyAllWindows()