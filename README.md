# AI_Vaccine

### Decision Tree & CNN & WGAN-GP

#### Decision Tree
DF를 악성 코드를 분류 할 수 있는 요인들을 찾기 위한 방법론으로 사용함 
특성 중요도를 찾기 위해 게임이론(Game Thoery)의 Shapley Value 측정 - XAI(eXplainable AI)
추후 성능을 높이기 위한 방법으로 RandomForest로 대치 가능

#### CNN
![CNN 탐지](https://github.com/integralstar/AI_Vaccine/blob/main/cnn_training.png)
Deep Learning을 이용한 일반적인 탐지 방법

#### WGAN-GP
![WGAN-GP 훈련](https://github.com/integralstar/AI_Vaccine/blob/main/wgan-gp.png)
1. Gradient Penalty loss는 입력 이미지에 대한 예측의 gradient L2 norm(유클리드 거리)과 1사이의 차이를 제곱한 값
2. critic의 가중치를 클리핑하지 않음 (1-립시츠 조건 부과)
3. critic에 배치 정규화 미사용 : 같은 배치 안의 이미지 사이에 상관관계를 만들기 때문에 GP loss 효과가 떨어짐
4. keras에서는 _Merge층을 상속한 RandomWeightedAverage층을 만들어 보간 연산 수행 가능

테스트 결과 CNN으로 탐지하지 못하는 변형된 형태의 악성코드를 탐지 할 수 있었음 (성능이 더 우수함)

#### 정리
장점
1. 여러 인공지능 방법론을 결합하여 성능을 개선하거나 높일 수 있음
2. 새로운 바이러스 파일이 존재할 경우 pattern이나 signiture 방법은 바이러스 탐지에 실패하지만 AI의 경우 탐지 가능성이 높음

단점
1. 어떤 malware인지 확인 해야 하는 경우 곤란함
2. 감염 치료를 위해서도 signiture가 필요

결론
기존 백신의 탐지 방법과 AI를 결합하여 사용할 경우 우수한 성능을 기대할 수 있음
