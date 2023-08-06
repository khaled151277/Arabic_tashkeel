import streamlit as st
import mishkal.tashkeel

def tashkeel_app(text):
    vocalizer = mishkal.tashkeel.TashkeelClass()
    tashkeeled_text = vocalizer.tashkeel(text)
    return tashkeeled_text

def main():
    st.title("تشكيل الكلمات العربي ")
    st.write("هذا التطبيق يقوم بتشكيل الكلمات العربية")

    tashkeel_input = st.text_area("Enter your text for Tashkeel:")

    if st.button("شَكَّلَهَا"):
        if tashkeel_input:
            tashkeeled_text = tashkeel_app(tashkeel_input)
            st.write("Tashkeeled Text:")
            st.write(tashkeeled_text)
        else:
            st.warning("Please enter some text for Tashkeel.")

if __name__ == "__main__":
    main()
