import cv2
import numpy as np

# desert.jpg 이미지를 컬러로 읽기
src = cv2.imread('desert.jpg', cv2.IMREAD_COLOR)

if src is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # ROI(관심 영역) 선택
    x, y, w, h = cv2.selectROI(src)

    # BGR 이미지를 YCrCb 색 공간으로 변환
    src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

    # 선택한 ROI 영역
    roi = src_ycrcb[y:y+h, x:x+w]

    # ROI의 히스토그램 계산 (Cr, Cb 채널 사용)
    hist = cv2.calcHist([roi], [1, 2], None, [128, 128], [0, 256, 0, 256])

    # 히스토그램 역투영 계산
    backproj = cv2.calcBackProject([src_ycrcb], [1, 2], hist, [0, 256, 0, 256], 1)

    # 역투영 결과를 마스크로 원본 이미지에 적용
    dst = cv2.copyTo(src, backproj)

    # 결과 출력
    cv2.imshow('Original Image', src)
    cv2.imshow('Back Projection Mask', backproj)
    cv2.imshow('Back Projection Result', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
