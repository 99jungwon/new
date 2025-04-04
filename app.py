import streamlit as st
from PIL import Image

# 페이지 설정
st.set_page_config(page_title="에로상 이거 눌러봐", layout="centered")

# 대시보드 제목
st.title("🎯 에로필그, 골뽑 망해라")

# 상단 조롱 멘트
st.markdown("""
## 🤡 사람이 진짜 운이 없어...
- 픽하면 망하고...  
- 돌려도 망하고 ...
- **해도 안 해도 손해**

---

""")

# 이미지 불러오기 & 가운데 출력
img = Image.open("image.png")
st.image(img, use_column_width=False)

# 하단 박제 멘트
st.markdown("""
---

## 💬 다음 주도? 기대하지 마셈
> 그냥 결과 나오기 전에 미리 말해드리는 거예요  
> 이번에도 망합니다. 네, 또요.

---

#### 🧨 골뽑 결과 = 18 허경민, 18 이정후
""")
