import base64

# النص المشفر من شاشتك مع تصحيح الأقواس
data = "cHJpbnQoJ4pyFIHRlbSBhbC10YXNoZmVlciB3YWwgLXRhc2hnaGVlbCBiZS1uYWphaCB5YSBiYXRhbCEnKQ=="

try:
    # فك التشفير مع تجاهل أي أخطاء في الرموز الغريبة
    decoded = base64.b64decode(data).decode('utf-8', 'ignore')
    exec(decoded)
except Exception as e:
    print(f"حدث خطأ بسيط في القراءة: {e}")
