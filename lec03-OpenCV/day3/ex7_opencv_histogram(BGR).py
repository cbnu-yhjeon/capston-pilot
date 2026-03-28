import cv2
import matplotlib.pyplot as plt

# Lenna 이미지를 BGR로 읽기
image = cv2.imread('Lenna.png')

# 이미지 읽기가 성공적이지 못한 경우 처리
if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 각 채널별 히스토그램 계산
    colors = ('b', 'g', 'r')
    channel_names = ('Blue', 'Green', 'Red')

    # 원본 이미지 출력
    cv2.imshow('Original Image (BGR)', image)

    # 히스토그램 출력 (matplotlib 사용)
    plt.figure()
    plt.title("BGR Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    for i, (color, name) in enumerate(zip(colors, channel_names)):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=name)

    plt.xlim([0, 256])
    plt.legend()
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
