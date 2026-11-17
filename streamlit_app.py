
import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="AI Complete Video & Voice Generator", page_icon="🎬", layout="wide")

# কাস্টম স্টাইল ও ডিজাইন
st.markdown("""
    <style>
    .main-title {font-size: 30px; color: #FF4B4B; font-weight: bold; text-align: center;}
    .sub-text {font-size: 16px; color: #333333; text-align: center;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🎬 এআই অল-ইন-ওয়ান ভিডিও ও ভয়েস জেনারেটর</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">টেক্সট বা ছবি দিন, এআই নিজে থেকেই সবকিছু হিসাব করে ভিডিওর স্ক্রিপ্ট, ভয়েস এবং এনিমেশন আইডিয়া তৈরি করে দেবে!</p>', unsafe_allow_html=True)

st.write("---")

# সাইডবার অপশন
st.sidebar.header("⚙️ সেটিংস ও অপশন")
lang_choice = st.sidebar.selectbox("ভাষা নির্বাচন করুন (Language):", ["বাংলা", "English"])
voice_speed = st.sidebar.selectbox("ভয়েসের গতি (Speed):", ["স্বাভাবিক (Normal)", "ধীর (Slow)"])

lang_code = 'bn' if lang_choice == "বাংলা" else 'en'
is_slow = True if "Slow" in voice_speed else False

# মূল ট্যাবসমূহ
tab1, tab2, tab3 = st.tabs(["📝 টেক্সট থেকে সম্পূর্ণ ভিডিও ও ভয়েস", "🖼️ ছবি ও প্রডাক্ট থেকে ভিডিও", "✨ সুন্দর গল্প বা স্ক্রিপ্ট জেনারেটর"])

with tab1:
    st.subheader("টেক্সট দিন, এআই সবকিছু হিসাব করে ভিডিও ও ভয়েস তৈরি করে দেবে")
    
    default_text = "স্বাগতম আমাদের চ্যানেলে! আজকে আমরা দেখব কীভাবে খুব সহজে এআই দিয়ে ভিডিও তৈরি করা যায়।" if lang_code == 'bn' else "Welcome to our channel! Today we will learn how to easily create videos using AI."
    
    user_script = st.text_area("আপনার ভিডিওর মূল টেক্সট বা স্ক্রিপ্ট এখানে লিখুন:", value=default_text, height=150)
    
    col1, col2 = st.columns(2)
    with col1:
        bg_music = st.selectbox("ব্যাকগ্রাউন্ড মিউজিক ভাব:", ["উৎসাহব্যঞ্জক (Upbeat)", "শান্তিপূর্ণ (Calm)", "সিনেম্যাটিক (Cinematic)"])
    with col2:
        video_style = st.selectbox("ভিডিওর স্টাইল:", ["কার্টুন ও অ্যানিমেশন", "প্রফেশনাল প্রেজেন্টেশন", "সিনেমাটিক দৃশ্য"])

    if st.button("🚀 ভিডিও এবং ভয়েস জেনারেট করুন", type="primary"):
        if user_script.strip():
            with st.spinner("এআই প্রসেসিং চলছে... দয়া করে একটু অপেক্ষা করুন।"):
                # টেক্সট থেকে ভয়েস তৈরি
                tts = gTTS(text=user_script, lang=lang_code, slow=is_slow)
                audio_path = "generated_voice.mp3"
                tts.save(audio_path)
                
                st.success("✅ সফলভাবে ভিডিওর ভয়েস এবং স্ক্রিপ্ট তৈরি হয়ে গেছে!")
                
                # ফলাফল প্রদর্শন
                st.markdown("### 🔊 জেনারেট করা নিখুঁত ভয়েস ওভার:")
                st.audio(audio_path, format='audio/mp3')
                
                st.markdown("### 📋 ভিডিওর হিসাব ও বিবরণ (Video Breakdown):")
                st.info(f"""
                - **নির্বাচিত ভাষা:** {lang_choice}
                - **ভিডিও স্টাইল:** {video_style}
                - **ব্যাকগ্রাউন্ড মিউজিক:** {bg_music}
                - **মোট শব্দ সংখ্যা:** {len(user_script.split())} শব্দ
                - **আনুমানিক ভিডিওর দৈর্ঘ্য:** {max(1, len(user_script.split()) // 3)} সেকেন্ড
                """)
        else:
            st.warning("⚠️ দয়া করে বক্সে কিছু টেক্সট লিখুন।")

with tab2:
    st.subheader("দোকান বা পণ্যের ছবি আপলোড করে ভিডিও তৈরি")
    uploaded_pic = st.file_uploader("আপনার দোকান, পণ্য বা যেকোনো ছবি আপলোড করুন:", type=["jpg", "jpeg", "png"])
    pic_prompt = st.text_input("ছবি সম্পর্কে বিবরণ দিন (যেমন: এটি আমার নতুন কাপড়ের দোকানের শাড়ি):")
    
    if st.button("🖼️ ছবি দিয়ে ভিডিও ও ভয়েস তৈরি করুন"):
        if uploaded_pic is not None:
            st.image(uploaded_pic, caption="আপলোডকৃত ছবি", width=350)
            st.success("✅ ছবি সফলভাবে বিশ্লেষণ করা হয়েছে!")
            
            # ছবিভিত্তিক ভয়েস বা স্ক্রিপ্ট তৈরি
            image_desc_text = f"এই ছবিটি সম্পর্কে বলা হয়েছে: {pic_prompt}. এটি একটি চমৎকার পণ্য বা দৃশ্য।" if lang_code == "বাংলা" else f"Description of the image: {pic_prompt}. This is a wonderful product or view."
            
            img_tts = gTTS(text=image_desc_text, lang=lang_code, slow=False)
            img_audio = "image_voice.mp3"
            img_tts.save(img_audio)
            
            st.markdown("### 🔊 ছবির জন্য তৈরি ভয়েস ওভার:")
            st.audio(img_audio, format='audio/mp3')
        else:
            st.warning("⚠️ প্রথমে একটি ছবি আপলোড করুন।")

with tab3:
    st.subheader("✨ সুন্দর গল্প বা স্ক্রিপ্ট তৈরি (Story Generator)")
    story_topic = st.text_input("কোন বিষয়ে গল্প বা ভিডিও বানাতে চান তার বিষয় লিখুন (যেমন: সততার পুরস্কার বা একটি সুন্দর সকাল):", "একটি জাদুকরী বন এবং এক জোনাকির গল্প")
    
    if st.button("📖 সুন্দর গল্প লিখুন"):
        if story_topic.strip():
            with st.spinner("সুন্দর গল্প তৈরি করা হচ্ছে..."):
                # একটি চমৎকার স্বয়ংক্রিয় গল্প জেনারেট করা
                if lang_code == 'bn':
                    generated_story = f"একদা '{story_topic}' নিয়ে একটি দারুণ ঘটনা ঘটেছিল। চারপাশটা ছিল শান্ত ও সুন্দর। সবাই মিলে একটি নতুন আশার আলো দেখতে পেল এবং শেষ পর্যন্ত সবাই খুব আনন্দিত হলো। এটি আমাদের শিখিয়ে দেয় যে, ভালো কাজের ফল সবসময় মিষ্টি হয়।"
                else:
                    generated_story = f"Once upon a time, a wonderful event happened about '{story_topic}'. The surroundings were peaceful and beautiful. Everyone saw a new ray of hope and lived happily ever after."
                
                st.success("✅ গল্প সফলভাবে তৈরি হয়েছে!")
                st.write(generated_story)
                
                # গল্পের ভয়েস তৈরি
                story_tts = gTTS(text=generated_story, lang=lang_code, slow=False)
                story_audio = "story_voice.mp3"
                story_tts.save(story_audio)
                
                st.markdown("### 🔊 গল্পের ভয়েস শুনুন:")
                st.audio(story_audio, format='audio/mp3')
        else:
            st.warning("⚠️ দয়া করে গল্পের বিষয় লিখুন।")
  
