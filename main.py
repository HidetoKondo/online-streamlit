import streamlit as st
import numpy as np
import pandas as pd
import time as te
from PIL import  Image
from streamlit_metrics import metric, metric_row


st.title('Streamlit 超入門')
st.write('Interactive Widgets')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
#    latest_iteration.text(f'Iteration {i+1}')
#    bar.progress(i + 1)
    te.sleep(0.1)
    bar.progress(i + 1)

'Done!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')


#text = st.text_input('あなたの趣味を教えてください。')
#'あなたの趣味は：', text, 'です。'

#condition = st.slider('あなたの今の調子は?',0,100,50)
#'コンディション：', condition

#if st.checkbox('Show Image'):
#  img = Image.open('sample.png')
#  st.image(img, caption='bag', use_column_width=True)

#option = st.selectbox(
#    'あなたの好きな数字を教えてください。',
#    list(range(1,11))
#)

#'あなたの好きな数字は：', option, 'です。'

# df = pd.DataFrame({
#    '1列目': [1, 2, 3, 4],
#    '2列目': [10, 20, 30, 40]
# })

#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat', 'lon']
#)

# st.table(df.style.highlight_max(axis=0))
#st.map(df)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""