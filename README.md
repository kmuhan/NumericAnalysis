# 수치해석 자율 프로젝트 - 포유류의 체중과 기대수명의 상용로그값에 대한 선형 회귀분석에 대한 결과물

## 프로젝트 내용
- Crawling한 Data를 기반으로 학습 Data와 테스트 Data를 약 8 : 2로 구성하여 간단한 선형 회귀 모델 도출
- 사용 Data Reference : https://a-z-animals.com/animals/mammals/
- Crawler : python, BeutifulSoup
- train Data : 400개
- test Data : 49개
> 실제 학습 라이브러리 : Tensorflow, Keras, Numpy, Scikit-learn, Scipy

![image](https://user-images.githubusercontent.com/66053034/119271937-c855ea00-bc3e-11eb-9449-9cbbddade0cb.png)
- Optimal Data set : weight : max, longevity : avg
![image](https://user-images.githubusercontent.com/66053034/119271932-bffdaf00-bc3e-11eb-9ddc-57c3088930ee.png)
- Tensorflow Mse :  0.1013238242237613
![image](https://user-images.githubusercontent.com/66053034/119271890-84fb7b80-bc3e-11eb-801e-6f73ba5402bc.png)
- Keras Mse : 0.11791003961746452
