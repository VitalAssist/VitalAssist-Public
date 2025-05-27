
from langdetect import detect

# Map of symptoms and keywords per language
symptom_replies = {
    "en": {
        "headache": "You may be experiencing a headache. Try resting and staying hydrated.",
        "fever": "You may have a fever. Monitor your temperature and rest.",
        "stomach": "For stomach pain or cramps, avoid solid foods for a while and stay hydrated.",
        "throat": "If your throat is sore or painful, consider warm fluids and rest. See a doctor if it worsens.",
        "cough": "Try staying hydrated and resting. If persistent, consult a doctor.",
        "pain": "Could you please specify where the pain is located?",
    },
    "ar": {
        "headache": "قد يكون لديك صداع. حاول الراحة وشرب الكثير من الماء.",
        "fever": "قد تكون مصابًا بالحمى. راقب درجة حرارتك واسترح.",
        "stomach": "لآلام المعدة، تجنب الطعام الصلب واشرب السوائل.",
        "throat": "إذا كنت تعاني من ألم في الحلق، اشرب سوائل دافئة واسترح.",
        "cough": "إذا كنت تسعل، اشرب الماء الدافئ واسترح.",
        "pain": "يرجى تحديد مكان الألم.",
    },
    "fa": {
        "headache": "ممکن است سردرد داشته باشید. استراحت کنید و آب کافی بنوشید.",
        "fever": "شاید تب دارید. دمای بدن را بررسی کنید و استراحت کنید.",
        "stomach": "در صورت دل‌درد، غذاهای جامد نخورید و مایعات بنوشید.",
        "throat": "اگر گلودرد دارید، مایعات گرم بنوشید و استراحت کنید.",
        "cough": "اگر سرفه می‌کنید، آب گرم بنوشید و استراحت کنید.",
        "pain": "لطفاً مشخص کنید درد در کجاست.",
    },
    "hi": {
        "headache": "आपको सिरदर्द हो सकता है। आराम करें और पानी पिएं।",
        "fever": "आपको बुखार हो सकता है। तापमान की निगरानी करें और आराम करें।",
        "stomach": "पेट दर्द के लिए थोड़ी देर ठोस भोजन से बचें और तरल पदार्थ पिएं।",
        "throat": "अगर गले में दर्द है तो गर्म तरल पिएं और आराम करें।",
        "cough": "अगर खांसी है तो गर्म पानी पिएं और आराम करें।",
        "pain": "कृपया बताएं कि दर्द कहाँ है।",
    },
    "ku": {
        "headache": "سەردەردت هەیە، تکایە ئارام بە و ئاڤ بخۆ.",
        "fever": "گەرمی تەنەوە هەیە؟ بزانە چەندەیە و ئاڤ بخۆ.",
        "stomach": "ئەگەر سەرووشە دەردت هەیە، خواردنی قەڵەوە مەخۆ و ئاڤ بخۆ.",
        "throat": "ئەگەر گەڵوە دەردت هەیە، ئاوی گەرم بخۆ و ئارام بە.",
        "pain": "تکایە بیڵێ دەردەکە لە کوێیە.",
    }
}

def detect_language(text):
    try:
        lang = detect(text)
        if lang.startswith("ar"): return "ar"
        if lang.startswith("fa"): return "fa"
        if lang.startswith("hi"): return "hi"
        if lang.startswith("ku") or "سەردەرد" in text or "گەڵو" in text: return "ku"
        return "en"
    except:
        return "en"

def openai_offline_reply(message):
    lang = detect_language(message)
    message_lower = message.lower()

    for keyword in symptom_replies.get(lang, {}):
        if keyword in message_lower:
            return symptom_replies[lang][keyword]

    fallback = {
        "en": "I'm here to assist. Please describe your symptoms or ask a health question.",
        "ar": "أنا هنا للمساعدة. من فضلك صف أعراضك أو اسأل سؤالًا صحيًا.",
        "fa": "من اینجا هستم تا کمک کنم. لطفاً علائم خود را توضیح دهید یا یک سؤال پزشکی بپرسید.",
        "hi": "मैं आपकी सहायता के लिए यहाँ हूँ। कृपया अपने लक्षण बताएं या कोई स्वास्थ्य संबंधी प्रश्न पूछें।",
        "ku": "من بۆ یارمەتی ئەمە، تکایە نیشانەکانت بەسەر بکە یان پرسیارێکی تەندروستی بکە.",
    }

    return fallback.get(lang, fallback["en"])
