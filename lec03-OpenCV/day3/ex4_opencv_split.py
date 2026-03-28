import cv2

# 이미지를 읽기
image = cv2.imread("Lenna.png")

# 이미지 읽기가 성공적이지 못한 경우 처리
if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # Blue, Green, Red 성분 분리
    # cv2.split() 반환 순서: BGR (OpenCV는 BGR 순서로 읽음)
    blue, green, red = cv2.split(image)

    # 각각의 성분 출력
    print("Blue Component:")
    print(blue)
    print("\nGreen Component:")
    print(green)
    print("\nRed Component:")
    print(red)

    # 이미지 윈도우로 확인
    cv2.imshow("Original Image", image)
    cv2.imshow("Blue Component", blue)
    cv2.imshow("Green Component", green)
    cv2.imshow("Red Component", red)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
