import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

st.write('Dataframe')

df = pd.DataFrame({
    '１列目': [1, 2, 3, 4],
    '２列目': [10, 20, 30, 40]
})

st.write(df)

#st.dataframe(df.style.highlight_max(axis=0), width=100) # 表の縦横を指定できる
#st.dataframe(df.style.highlight_max(axis=0)) # 表の縦横を指定できる

st.table(df) #静的な表を作る 

# マジックコマンド
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

### チャートを書く
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)

### 地図を書く
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon',]
)

st.dataframe(df)
st.map(df)

from PIL import Image
### 画像を開く 

st.write('Display Image')

img = Image.open('top-01.jpg')
st.image(img, caption='AAL', use_column_width=True)
