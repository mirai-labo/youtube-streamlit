import streamlit as st
# import numpy as np
# import pandas as pd

# from PIL import Image
import time


st.title('Streamlit 超入門')

st.write('Dataframe')
st.write('Display Image')
'Start!!'

latest_iteration = st.empty()

bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラム')

# expander1 = st.expander('問い合わせ')
# expander1.write('問い合わせ内容を書く')
# expander2 = st.expander('問い合わせ')
# expander2.write('問い合わせ内容を書く')
# expander3 = st.expander('問い合わせ')
# expander3.write('問い合わせ内容を書く')


# if st.checkbox(' Show Image'):
#     img = Image.open('top-01.jpg')
#     st.image(img, caption='AAL', use_column_width=True)

# # 選択
# option = st.selectbox(
#     'あなたが好きな数字を押してください。',
#     options = list(range(1,11))
# )

# 'あなたの好きな数字は', option, 'です。'

# # テキスト入力
# option2 = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は',option2, 'です。'

# # スライダー
# condition = st.slider('あなたの今の調子は', 0, 100, 50)

# 'コンディション:', condition


