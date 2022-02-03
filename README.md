# Re-View the Review
### Review? Re-View!
물건 살 때 여러분이 보는 그 리뷰의 **⭐️유용성⭐️**, 저희가 알려드립니다! 

📌 리뷰 유용성 판단부터   
📌 군집화를 통한 대표 리뷰 추출까지

*우리 같이 Review를 Re-View해봐요♥️*

## 프로젝트 소개

## 유용성 분류 모델

## 리뷰 군집화 모델

### 실험 배경
PPT 사진1
- 소비자가 무수한 리뷰를 직접 보고 판단하기 어려워, 비슷한 리뷰끼리 군집화하여 군집 별 핵심 리뷰만 제공하고자 함

### 임베딩 모델 실험

##### TF-idf
PPT 사진2
- 어떤 단어가 특정 문저 내에서 얼마나 중요한 것인지를 나타내는 벡터
- 개별 문서에서 자주 등장하는 단어에 높은 가중치를 주되, 모든 문서에서 전반적으로 자주 등장하는 단어에 대해서는 패널티를 주는 방식
- TF(문서 내에 얼마나 자주 등장하는지), IDF(다른 문서에서 자주 등장하는지의 역수)를 곱해 구하는 방법

##### Doc2vec
PPT 사진3
- 고전 모델인 Word2vec과 유사한 distributed word representation 방법
- 의미공간에 document의 위치좌표를 학습하는 방법으로, 단어를 예측하며 로그 확률 평균을 최대화하는 과정으로 학습
- 단어 사이의 연관성 뿐만이 아닌 paragraph vector가 지속적으로 학습됨
- 일반적으로 성능이 더 좋다고 알려진 PV-DM 방식 사용

##### 키워드 추출 모델

### 파이프라인
PPT 사진4
- 전처리 : 데이터 cleaning, mecab을 통해 명사만 추출
- 임베딩 : TF-IDF 선정
- Clustering : k-means clustering
- 군집별 가장 중앙에 가까운 상위 10개 단어를 대표 단어로 추출
- 군집별 Top k개 리뷰 추출

### 실험결과
PPT 사진5

###### 군집 개수

###### 군집별 키워드 추출

###### 군집별 Top k 리뷰 추출

## 유용성 결정요인 파악 및 분석

## 웹 구현

## 결론 및 제언

----
## Contributors

<table>
  <tr>
      <td align="center"><a href="https://github.com/jayleenym"><img src="https://github.com/jayleenym.png" width="100"  height="100"><br /><sub><b>문예진</b>(조장)</sub></td>
      <td align="center"><a href="https://github.com/SeoroMin"><img src="https://github.com/SeoroMin.png" width="100"  height="100"><br /><sub><b>이상민</b></sub></td>
      <td align="center"><a href="https://github.com/fromslow"><img src="https://github.com/fromslow.png" width="100" height="100"><br /><sub><b>정수연</b></sub></td>
      <td align="center"><a href="https://github.com/SeungYeon-Chung"><img src="https://github.com/SeungYeon-Chung.png" width="100" height="100"><br /><sub><b>정승연</b></sub></td> 
      <td align="center"><a href="https://github.com/hul980"><img src="https://github.com/hul980.png" width="100" height="100"><br /><sub><b>황의린</b></sub></td> 
    </tr>
</table>

----
