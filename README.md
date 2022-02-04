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
- 전처리 : 데이터 cleaning, mecab을 통해 명사, 서술어 추출 후 불용어 제거 등
- 임베딩 : Doc2Vec 선정
- Clustering: k-means clustering 
- 군집 별 키워드를 키워드 추출 모델 4가지를 사용하여 추출 후 비교함 
1. Yake : 단일 문서에서 추출한 텍스트를 통계적 기반으로 비지도 학습하는 방법으로, 별도의 형태소 분석 등의 전처리가 불필요하여 매우 간단함
2. Rake : 구분기호나 불용어를 입력으로 하여 개별 문서에서 키워드를 추출하는 방법
3. TextRank : 단어의 동시 발생을 정의하여 단어간의 관계를 파악하여 키워드 추출하는 방법으로, 문장간 유사도를 기반으로 추출함
4. KeyBert : Sentence Bert로 문장을 임베딩 후 n-gram으로 단어 임베딩 추출. 코사인 유사도를 이용하여 가장 유사성이 높은 단어를 키워드로 추출함
- Keyword 추출 모델로는 군집별로 적절한 키워드가 잡히지 않아 K-means 군집의 중심 근처에 위치한 단어들을 키워드로 잡는 방법을 선택함.

### 파이프라인
PPT 사진4
- 전처리 : 데이터 cleaning, mecab을 통해 명사만 추출
- 임베딩 : TF-IDF 선정
- Clustering : k-means clustering
- 군집별 가장 중앙에 가까운 상위 10개 단어를 대표 단어로 추출
- 군집별 Top k개 리뷰 추출

### 실험결과
PPT 사진5

#### 군집 개수

#### 군집별 키워드 추출

#### 군집별 Top k 리뷰 추출

## 유용성 결정요인 파악 및 분석

## 웹 구현
[웹 시연 영상(youtube)](https://youtu.be/VAzpjofp-Zw)
- Streamlit을 활용하여 프로토타입 완성
- Screenshots
 <img width="450" alt="스크린샷 2022-02-04 오후 5 49 04" src="https://user-images.githubusercontent.com/58161277/152499301-011333b8-2b94-4fc6-bdac-253093d831be.png" align="left">
 <img width="450" alt="스크린샷 2022-02-04 오후 5 54 26" src="https://user-images.githubusercontent.com/58161277/152500043-3d7579de-8b1d-4dc3-b00f-baa43f3e0aed.png">

 <img alt="스크린샷 2022-02-04 오후 5 50 02" src="https://user-images.githubusercontent.com/58161277/152499445-01b6025d-5ee8-4ef0-97f1-e49cff346543.png" align="center">
 <img alt="스크린샷 2022-02-04 오후 5 56 01" src="https://user-images.githubusercontent.com/58161277/152500286-1694dec5-9110-42ed-a616-c9aa2eece372.png" align="center">
 <img alt="스크린샷 2022-02-04 오후 5 56 15" src="https://user-images.githubusercontent.com/58161277/152500319-f410e049-0f20-4e5a-aa92-7352bb36b557.png" align="center">


## 결론 및 제언



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
