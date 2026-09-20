import streamlit as st
import os

# إعدادات الصفحة
st.set_page_config(
    page_title="اكتشف السعودية - اليوم الوطني",
    page_icon="🟢",
    layout="wide"
)

# ---------------------------------------------------------
# نظام عداد الزوار الحقيقي (يخزن في ملف نصي ولا يعود للصفر)
# ---------------------------------------------------------
COUNTER_FILE = "visitor_count.txt"


def get_and_increment_visitor_count():
    # التحقق مما إذا كانت هذه الجلسة قد حُسبت مسبقاً لمنع زيادة العداد عند تحديث الصفحة (Refresh)
    if "visited" not in st.session_state:
        st.session_state.visited = True

        # قراءة العدد الحالي أو إنشاء الملف إذا لم يكن موجوداً
        count = 0
        if os.path.exists(COUNTER_FILE):
            try:
                with open(COUNTER_FILE, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content.isdigit():
                        count = int(content)
            except:
                count = 0

        # زيادة العدد وحفظه في الملف
        count += 1
        try:
            with open(COUNTER_FILE, "w", encoding="utf-8") as f:
                f.write(str(count))
        except:
            pass
        return count
    else:
        # إذا تم تحديث الصفحة لنفس الجلسة، نعرض العدد الحالي دون زيادته
        if os.path.exists(COUNTER_FILE):
            try:
                with open(COUNTER_FILE, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content.isdigit():
                        return int(content)
            except:
                pass
        return 1


current_visitors = get_and_increment_visitor_count()

# تخصيص التصميم والأنماط
st.markdown("""
    <style>
    /* خلفية الموقع العامة واتجاه النصوص لليمين */
    .stApp {
        background-color: #0b2e1e;
        color: #f8f9fa;
        font-family: 'Cairo', sans-serif, Arial;
        direction: rtl;
        text-align: right;
    }

    /* تنسيق لوني واضح لنصوص إدخال الأسماء والقوائم */
    .stTextInput label, .stSelectbox label {
        color: #ffffff !important;
        font-weight: bold;
        font-size: 16px;
        text-align: right;
        direction: rtl;
    }

    /* العناوين العامة */
    h1, h2, h3 {
        color: #ffffff;
        text-align: center;
        direction: rtl;
    }

    /* تصميم بطاقة الجواز السياحي الرقمي الفاخرة */
    .passport-card {
        background: linear-gradient(135deg, #006C35 0%, #034d26 100%);
        border: 2px solid #d4af37;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
        margin: 20px auto;
        color: white;
        direction: rtl;
    }

    /* بطاقات المدن والوجهات */
    .city-card {
        background-color: #113f2b;
        border: 1px solid #1e6b47;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        direction: rtl;
        text-align: right;
    }

    /* الأزرار */
    .stButton>button {
        background: linear-gradient(135deg, #d4af37 0%, #aa8c2c 100%);
        color: #0b2e1e;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        border: none;
        width: 100%;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #ffd700 0%, #d4af37 100%);
        color: #000000;
        transform: scale(1.02);
    }

    /* شريط الترحيب */
    .hero-section {
        text-align: center;
        padding: 40px 20px;
        background: radial-gradient(circle, #113f2b 0%, #0b2e1e 100%);
        border-radius: 20px;
        border: 1px solid #1e6b47;
        margin-bottom: 30px;
        direction: rtl;
    }

    /* قسم أسماء الطالبات في الأسفل - سطر واحد مستقيم */
    .students-footer {
        background-color: #061c12;
        border: 1px solid #1e6b47;
        padding: 25px 30px;
        border-radius: 15px;
        text-align: right;
        margin-top: 40px;
        color: #f8f9fa;
        direction: rtl;
        width: 100%;
    }
    .student-single-line {
        font-size: 15px;
        color: #f8f9fa;
        line-height: 1.8;
        word-spacing: 2px;
        text-align: right;
    }

    /* تنسيق عداد الزوار في الأسفل بشكل أنيق ومتناسق مع الثيم */
    .visitor-counter {
        text-align: center;
        background-color: #061c12;
        border: 1px solid #d4af37;
        padding: 12px;
        border-radius: 10px;
        margin: 20px auto;
        max-width: 300px;
        color: #f8f9fa;
        font-size: 16px;
        font-weight: bold;
        direction: rtl;
    }
    </style>
""", unsafe_allow_html=True)

# 1. شاشة البداية: طلب اسم المستخدم
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if not st.session_state.user_name:
    st.markdown("""
        <div class='hero-section'>
            <h1>أهلًا بك في برنامج اكتشف السعودية ✨</h1>
            <p style='font-size: 20px; color: #d4af37;'>عالم من التراث، الحداثة، والطبيعة الخلابة</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        name_input = st.text_input("الرجاء إدخال اسمك الكريم:")
        if st.button("✈️ ابدأ الرحلة الوطنية"):
            if name_input.strip() != "":
                st.session_state.user_name = name_input
                st.rerun()
            else:
                st.warning("الرجاء إدخال اسم صحيح.")
else:
    user_name = st.session_state.user_name

    # 2. تهيئة الذاكرة المؤقتة للأختام
    if "stamps" not in st.session_state:
        st.session_state.stamps = []
    if "reviews" not in st.session_state:
        st.session_state.reviews = {}

    # 3. قاعدة بيانات الوجهات
    destinations = {
        "الرياض": {
            "المنطقة": "منطقة الرياض",
            "الوصف": "عاصمة المملكة، تجمع بين الأصالة التاريخية والحداثة المتطورة.",
            "المعالم": ["قصر المصمك", "بوليفارد سيتي", "الدرعية التاريخية"],
            "ikon": "🏰"
        },
        "جدة": {
            "المنطقة": "منطقة مكة المكرمة",
            "الوصف": "عروس البحر الأحمر وواجهة تجارية وثقافية نابضة بالحياة.",
            "المعالم": ["البلد التاريخي", "كورنيش جدة", "نافورة الملك فهد"],
            "ikon": "🌊"
        },
        "العلا": {
            "المنطقة": "منطقة المدينة المنورة",
            "الوصف": "متحف عالمي مفتوح يضم إرثاً حضارياً وتشكيلات صخرية ساحرة.",
            "المعالم": ["مدائن صالح (الحجر)", "جبل الفيل", "البلدة القديمة"],
            "ikon": "🏜️"
        },
        "أبها": {
            "المنطقة": "منطقة عسير",
            "الوصف": "عروس الجبل، تتميز بأجوائها الساحرة وطبيعتها الخضراء الخلابة.",
            "المعالم": ["جبل السودة", "شارع الفن", "قصر شدا"],
            "ikon": "⛰️"
        },
        "الأحساء": {
            "المنطقة": "الشرقية",
            "الوصف": "أكبر واحة نخيل طبيعية في العالم وموطن للتاريخ والعراقة.",
            "المعالم": ["جبل القارة", "سوق القيصرية", "عين الحانة"],
            "ikon": "🌴"
        }
    }

    # القائمة الجانبية للتنقل
    st.sidebar.markdown(f"### 🟢 أهلاً بك، {user_name}")
    menu = st.sidebar.selectbox("🧭 القائمة الرئيسية", ["🗺️ استكشاف الوجهات", "🛂 جواز السفر الرقمي"])

    # ---------------------------------------------------------
    # قسم 1: استكشاف الوجهات
    # ---------------------------------------------------------
    if menu == "🗺️ استكشاف الوجهات":
        st.markdown("""
            <div class='hero-section'>
                <h1>استكشف وجهات المملكة</h1>
                <p style='font-size: 18px; color: #d4af37;'>اختر المدينة بنفسك واستكشف تفاصيلها ومعالمها المميزة ✨</p>
            </div>
        """, unsafe_allow_html=True)

        # عدّاد التقدم الإنجازي
        total_cities = len(destinations)
        visited_count = len(st.session_state.stamps)
        st.progress(visited_count / total_cities)
        st.markdown(
            f"<p style='text-align: center; color: #d4af37;'>نسبة إنجاز الاستكشاف: {visited_count} من {total_cities} مدن مكتشفة</p>",
            unsafe_allow_html=True)

        st.markdown("---")

        city_options = ["الرجاء اختيار مدينة للاستكشاف..."] + list(destinations.keys())
        selected_option = st.selectbox("📍 اختر المدينة التي ترغب في استكشافها:", city_options)

        if selected_option and selected_option != "الرجاء اختيار مدينة للاستكشاف...":
            city_info = destinations[selected_option]

            st.markdown(f"""
                <div class="city-card">
                    <h2>{city_info['ikon']} {selected_option}</h2>
                    <p><b>📍 المنطقة:</b> {city_info['المنطقة']}</p>
                    <p><b>📖 الوصف:</b> {city_info['الوصف']}</p>
                    <hr style='border-color: #1e6b47;'>
                    <p><b>🏛️ المعالم السياحية:</b> {', '.join(city_info['المعالم'])}</p>
                </div>
            """, unsafe_allow_html=True)

            note = st.text_input(f"اكتب انطباعك أو ملاحظتك عن {selected_option}:", key=f"note_{selected_option}")

            if st.button(f"✨ أضف ختم {selected_option} إلى جوازك", key=f"btn_{selected_option}"):
                if selected_option not in st.session_state.stamps:
                    st.session_state.stamps.append(selected_option)
                    st.session_state.reviews[selected_option] = note
                    st.balloons()
                    st.success(f"🎉 مبروك! أضفت ختمًا جديدًا إلى جوازك ({selected_option})")
                else:
                    st.session_state.reviews[selected_option] = note
                    st.warning(f"⚠️ لديك ختم {selected_option} بالفعل! تم تحديث ملاحظاتك.")

    # ---------------------------------------------------------
    # قسم 2: جواز السفر السياحي الرقمي الفاخر
    # ---------------------------------------------------------
    elif menu == "🛂 جواز السفر الرقمي":
        st.markdown("""
            <div class='hero-section'>
                <h1>جواز السفر السياحي الرقمي</h1>
                <p style='font-size: 18px; color: #d4af37;'>إنجازك الشخصي في استكشاف أرجاء الوطن الغالي</p>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(f"""
                <div class="passport-card">
                    <h2 style='color: #d4af37;'>المملكة العربية السعودية</h2>
                    <p style='letter-spacing: 2px;'>وزارة السياحة - جواز السفر الرقمي</p>
                    <hr style='border-color: #d4af37;'>
                    <h3 style='margin: 10px 0;'>👤 المسافر: {user_name}</h3>
                    <p style='font-size: 18px;'>🏆 عدد الأختام المحصل عليها: <b>{len(st.session_state.stamps)}</b> من {len(destinations)}</p>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("🎫 سجل الأختام والمدن المكتشفة:")

        if len(st.session_state.stamps) > 0:
            stamp_cols = st.columns(3)
            for idx, stamp in enumerate(st.session_state.stamps):
                user_comment = st.session_state.reviews.get(stamp, "بدون ملاحظات")
                with stamp_cols[idx % 3]:
                    st.markdown(f"""
                        <div style="background-color: #113f2b; border: 2px dashed #d4af37; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 15px; direction: rtl;">
                            <h2 style='margin: 0;'>🟢</h2>
                            <h3 style='color: #d4af37; margin: 5px 0;'>ختم {stamp}</h3>
                            <p style='font-size: 13px; color: #ccc;'><b>ملاحظتك:</b> {user_comment if user_comment else 'رحلة رائعة'}</p>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("🎫 جواز السفر فارغ حالياً. انتقل إلى قسم (استكشاف الوجهات) لتبدأ جمع الأختام الوطنية!")

        # ---------------------------------------------------------
        # قسم أسماء الطالبات في سطر واحد مستقيم
        # ---------------------------------------------------------
        st.markdown("""
            <div class="students-footer">
                <h4 style="color: #d4af37; margin-bottom: 10px; text-align: right;">مشروع الطالبات:-</h4>
                <p class="student-single-line">
                    هند غزواني - نجاح العامري - وسن الحارثي - ميس العنزي - نجية الدوسري
                </p>
                <hr style="border-color: #1e6b47; width: 100%; margin: 15px 0;">
                <p style="margin: 5px 0; font-size: 16px; color: #d4af37; text-align: right;"><b>بإشراف :</b> روان الراشد</p>
            </div>
        """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # عداد زوار الموقع الحقيقي (تحت القائمة الرئيسية وفي الأسفل)
    # ---------------------------------------------------------
    st.markdown(f"""
        <div class="visitor-counter">
            👥 عدد زوار الموقع: {current_visitors}
        </div>
    """, unsafe_allow_html=True)

    # التذييل العام للموقع
    st.markdown("---")
    st.markdown("""
        <p style='text-align: center; color: #d4af37; font-size: 15px;'>
            نعتز بهمتنا حتى القمة | مشروع «اكتشف السعودية» للتعليم البرمجي التفاعلي
        </p>
    """, unsafe_allow_html=True)