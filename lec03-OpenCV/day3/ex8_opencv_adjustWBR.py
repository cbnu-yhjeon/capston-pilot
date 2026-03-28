import cv2
import numpy as np

# 이미지를 그레이스케일로 읽기
image = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 명암비 조작 수식: dst(x,y) = saturate(src(x,y) + (src(x,y) - 128) * alpha)
    # alpha > 0: 명암비 증가, alpha < 0: 명암비 감소
    alpha = 1.0
    func = (1 + alpha) * image - (alpha * 128)
    dst = np.clip(func, 0, 255).astype(np.uint8)

    cv2.imshow('Original Image', image)
    cv2.imshow(f'Contrast Adjusted (alpha={alpha})', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
