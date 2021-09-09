# https://docs.streamlit.io/en/stable/index.html

# from pandas._config.config import options
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
  '１列目': [1, 2, 3, 4],
  '２列目': [10, 20, 30, 40]
})

# st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
# st.table(df)

# """

# # 章
# ## 節
# ### 項

# ```
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

df2 = pd.DataFrame(
  np.random.rand(20,3),
  columns = ['a', 'b', 'c']
)

# df2

# st.line_chart(df2)
# st.area_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
  np.random.rand(100,2)/[50,50] + [35.69, 139.70],
  columns = ['lat', 'lon']
)

st.map(df3)

st.write('Display Image')

if st.checkbox('show Image'):
  img = Image.open('sample.jpg')
  st.image(img, caption='sample', use_column_width=True)

###

option = st.selectbox(
  'あなたが好きな数字を教えて下さい。',
  list(range(1,11))
)
'あなたの好きな数字は、', option, 'です'


st.write('[Interactive Widgets]')
text = st.text_input('あなたの趣味を教えて下さい')
# text = st.sidebar.text_input('あなたの趣味を教えて下さい')
'あなたの好きな数字は：', text

condision = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condision

###

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラム')


'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)

expander1 = st.expander('お問い合わせ')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('お問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('お問い合わせ3')
expander3.write('問い合わせ3の回答')

