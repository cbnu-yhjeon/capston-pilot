# 3주차 - OpenCV 기반 영상 처리 심화 및 실습

> 지능화 캡스톤 프로젝트 | 충북대학교 산업인공지능학과

---

## 목차

1. [컴퓨터 비전 개요](#1-컴퓨터-비전-개요)
2. [OpenCV란?](#2-opencv란)
3. [OpenCV 설치](#3-opencv-설치)
4. [영상 입출력](#4-영상-입출력)
5. [영상 처리](#5-영상-처리)
6. [예제 파일 목록](#6-예제-파일-목록)
7. [필요 이미지 파일](#7-필요-이미지-파일)

---

## 1. 컴퓨터 비전 개요

컴퓨터를 이용하여 정지 영상(Image) 혹은 동영상(Video)으로부터 정보를 추출하는 학문.
사람이 눈으로 보고 인지하는 작업을 컴퓨터가 수행하게 만드는 기술.

| 인간 | 컴퓨터 |
|------|--------|
| 눈 (영상 획득) | 카메라 (RGB, 열, 라이다 등) |
| 뇌 (인식) | 알고리즘 |

**응용 분야**: 농업, 의료, 교통, 스마트팩토리, 스포츠, 유통, 보안, 로봇 등

---

## 2. OpenCV란?

- **Open Source Computer Vision** — 실시간 컴퓨터 비전 및 머신 비전을 위한 오픈소스 라이브러리
- 2,500개 이상의 최적화된 비전 알고리즘 포함
- Windows, Linux, macOS, iOS, Android 등 다양한 플랫폼 지원

| 링크 | URL |
|------|-----|
| 공식 홈페이지 | https://opencv.org/ |
| Documentation | https://docs.opencv.org/ |
| Github | https://github.com/opencv |
| OpenCV Korea | https://cafe.naver.com/opencv |

---

## 3. OpenCV 설치

```bash
# 기본 모듈 설치
pip install opencv-python

# 추가 모듈 설치 (최신 알고리즘, CUDA 등)
pip install opencv-contrib-python

# 히스토그램 시각화용
pip install matplotlib
```

> 프로젝트별로 가상 환경을 구축하고 그 안에서 라이브러리를 설치하는 것을 권장합니다.

---

## 4. 영상 입출력

### 이미지 읽기/쓰기

| 함수 | 설명 |
|------|------|
| `cv2.imread(fileName, flag)` | 이미지 파일 읽기 |
| `cv2.imshow(title, image)` | 윈도우에 이미지 출력 |
| `cv2.waitKey(sec)` | 키 입력 대기 (0: 무한 대기, ms 단위) |
| `cv2.destroyAllWindows()` | 모든 윈도우 닫기 |

**imread flag 옵션**

| 플래그 | 설명 |
|--------|------|
| `cv2.IMREAD_COLOR` | 컬러로 읽기 (기본값) |
| `cv2.IMREAD_GRAYSCALE` | 그레이스케일로 읽기 |
| `cv2.IMREAD_UNCHANGED` | 이미지 속성 그대로 읽기 |

### 동영상/카메라 읽기

| 함수 | 설명 |
|------|------|
| `cv2.VideoCapture(filepath)` | 동영상 파일 열기 |
| `cv2.VideoCapture(devID)` | 카메라 열기 (0: 기본 카메라) |
| `cap.isOpened()` | 카메라/파일 작동 여부 확인 |
| `cap.read()` | 프레임 읽기 → `(ret, frame)` 반환 |
| `cap.release()` | 카메라/파일 객체 해제 |

---

## 5. 영상 처리

### 색 공간 (Color Space)

| 색 공간 | 구성 요소 | 주요 용도 |
|---------|-----------|-----------|
| RGB | Red, Green, Blue | 모니터, TV |
| CMYK | Cyan, Magenta, Yellow, Black | 프린터 인쇄 |
| HSV | Hue(색상), Saturation(채도), Value(명도) | 직관적 색 추출, 시각예술 |
| YUV | Y(밝기), U(파랑-밝기), V(빨강-밝기) | 디지털 압축 |

**색 공간 변환**: `cv2.cvtColor(src, code)`

| 코드 | 변환 |
|------|------|
| `cv2.COLOR_BGR2GRAY` | BGR → 그레이스케일 |
| `cv2.COLOR_BGR2RGB` | BGR → RGB |
| `cv2.COLOR_BGR2HSV` | BGR → HSV |
| `cv2.COLOR_BGR2YUV` | BGR → YUV |

> OpenCV는 이미지를 **BGR** 순서로 읽습니다 (RGB가 아님에 주의).

### 색상 영역 검출

HSV 색 공간에서 빨간색 Hue 범위: **(0~10)** 과 **(170~180)**

```python
# 마스크 생성
mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

# 마스크 적용
result = cv2.bitwise_and(image, image, mask=mask)
```

### 히스토그램

| 함수 | 설명 |
|------|------|
| `cv2.calcHist(src, channels, mask, histSize, ranges)` | 히스토그램 계산 |
| `cv2.equalizeHist(image)` | 히스토그램 평활화 (균등화) |
| `cv2.normalize(src, dst, 0, 255, cv2.NORM_MINMAX)` | 히스토그램 스트래칭 (정규화) |
| `cv2.calcBackProject(...)` | 히스토그램 역투영 |

### 명암비 조작

```
dst(x,y) = saturate( src(x,y) + (src(x,y) - 128) * alpha )
```

- `alpha > 0`: 명암비 증가
- `alpha < 0`: 명암비 감소

### 이미지 필터링

컨볼루션 연산: `cv2.filter2D(src, ddepth, kernel)`

| 필터 | 커널 예시 | 효과 |
|------|-----------|------|
| 평균값 필터 | 모든 값이 1/9인 3×3 행렬 | 블러링, 노이즈 제거 |
| 샤프닝 필터 | `[[0,-1,0],[-1,5,-1],[0,-1,0]]` | 경계 강조, 선명화 |
| 라플라시안 필터 | `[[0,1,0],[1,-4,1],[0,1,0]]` | 경계선 검출 |

---

## 6. 예제 파일 목록

모든 예제 파일은 `day3/` 디렉토리에 있습니다.

| 파일 | 내용 |
|------|------|
| `ex1_opencv_readImg.py` | 이미지 읽기 및 출력, 그레이스케일 실습 |
| `ex2_opencv_readVideo.py` | 동영상 파일 읽기 및 재생 |
| `ex3_opencv_readCam.py` | 카메라 영상 읽기 및 실시간 출력 |
| `ex4_opencv_split.py` | BGR 채널 분리 (`cv2.split`) |
| `ex5_opencv_cvtColor(HSV).py` | HSV / YUV 색 공간 변환 및 채널 분리 |
| `ex6_opencv_extractColor(RGB).py` | RGB 색 공간에서 빨간색 영역 추출 |
| `ex6_opencv_extractColor(HSV).py` | HSV 색 공간에서 빨간색/파란색 캔디 추출 |
| `ex7_opencv_histogram(grayscale).py` | 그레이스케일 히스토그램 계산 및 시각화 |
| `ex7_opencv_histogram(BGR).py` | BGR 채널별 히스토그램 시각화 |
| `ex8_opencv_adjustWBR.py` | 명암비 조작 |
| `ex8_equalizeHist.py` | 히스토그램 평활화 (균등화) |
| `ex8_opencv_normalizeHist.py` | 히스토그램 스트래칭 (정규화) |
| `ex8_opencv_backproj.py` | 히스토그램 역투영 |
| `ex9_opencv_filtering.py` | 평균값 / 샤프닝 / 라플라시안 필터 적용 |

---

## 7. 필요 이미지 파일

예제 실행 전 아래 이미지 파일을 `day3/` 폴더에 저장하세요.

| 파일명 | 사용 예제 | 다운로드 |
|--------|-----------|----------|
| `Lenna.png` | ex1, ex4, ex5, ex7, ex8, ex9 | https://upload.wikimedia.org/wikipedia/ko/thumb/2/24/Lenna.png/440px-Lenna.png |
| `Candies.png` | ex6 | https://www.charlezz.com/wordpress/wp-content/uploads/2021/04/www.charlezz.com-opencv-candies.png |
| `Hawkes.jpg` | ex8 (equalizeHist, normalizeHist) | https://blog.kakaocdn.net/dn/ZVlAe/btrr1mWG2SK/VsCRrXfpvOZsuD1EKYyHu1/Hawkes.jpg |
| `desert.jpg` | ex8 (backproj) | https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Rub_al_Khali_002.JPG/640px-Rub_al_Khali_002.JPG |
| `test_video.mp4` | ex2 | https://www.kaggle.com/datasets/dpamgautam/video-file-for-lane-detection-project |
