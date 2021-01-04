# 사용법 - ()안의 내용은 새로운 모델을 생성할때 사용
* (output 폴더에 학습 시킬 데이터를 넣고 python CsvWord2Vec.py - 형태소 분리)
* cd Bi_LSTM
* (python Bi_LSTM_csv_train.py - 모델 생성)
* python prediction.py --input_text=test.txt --output_text=result.txt

## CsvWord2Vec.py
 텐서플로우는 Embedding을 이용해 임베딩을 한 후 신경망 모델에 넣는 전처리용으로는 적합합니다. 그런데 단어 자체를 분석하고 토픽 모델링을 하기엔 제공되는 모듈이 많이 없어 어느정도 제한이기에 Gensim을 사용해 자연어 처리를 하였습니다.
 Gensim의 Word2Vec를 사용해 문장을 형태소 단위로 분리하고 형태소가 min_count(5) 미만 출현한 경우 제거 하여 오류를 제거하였습니다. 이를 통해 post.embedding을 생성합니다.

## Bi_LSTM_csv_train.py
 형태소로 분리한 문장들과 Tag를 매핑 시키고 keep_prob 를 0.75로 하였습니다. 이는 training epoch를 크게 하여 여러 번 학습을 시킴에 있어 overfitting이 발생하는 것을 막기위해 학습데이터의 75%만을 학습 시키는 것입니다. 이 과정을 반복하여 Model을 생성합니다.

## CsvWord2Vec.py
 학습 시킨 모델을 바탕으로 input으로 받은 값의 Tag를 분류합니다.

