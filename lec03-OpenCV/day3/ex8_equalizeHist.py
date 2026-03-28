import cv2
import matplotlib.pyplot as plt

# Hawkes.jpg 이미지를 그레이스케일로 읽기
image = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 히스토그램 평활화(균등화) 적용
    dst = cv2.equalizeHist(image)

    # 원본과 결과 이미지 출력
    cv2.imshow('Original Image', image)
    cv2.imshow('Equalized Image', dst)

    # 히스토그램 비교 출력
    hist_orig = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_eq = cv2.calcHist([dst], [0], None, [256], [0, 256])

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.title("Original Histogram")
    plt.plot(hist_orig)
    plt.xlim([0, 256])

    plt.subplot(1, 2, 2)
    plt.title("Equalized Histogram")
    plt.plot(hist_eq)
    plt.xlim([0, 256])

    plt.tight_layout()
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
