import streamlit as st
import json
import openai
import os


def app():

    # Set API key OpenAI
    openai.api_key = st.secrets['OPENAI_API_KEY']

    if 'openai_model' not in st.session_state:
        st.session_state['openai_model'] = 'gpt-4-turbo'

    # Fungsi untuk memuat data kuis dari file JSON
    def load_quiz_data(json_file):
        with open(json_file, encoding="utf-8") as f:
            return json.load(f)

    # Fungsi untuk mendapatkan petunjuk dari chatbot
    def get_hint(question):
        prompt = f"Saya kesulitan menjawab pertanyaan berikut: '{question}'. Bisakah Anda memberi saya beberapa petunjuk?"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150
        )
        hint = response.choices[0].text.strip()
        return hint

    # Fungsi untuk menampilkan soal dan menerima jawaban
    def display_question(question, options, correct_answer, key_prefix):
        st.write(question)
        answer = st.radio("Pilih jawaban Anda:", options, key=f"{key_prefix}_radio")
        hint_button = st.button("Minta Petunjuk", key=f"{key_prefix}_hint")
        
        if hint_button:
            hint = get_hint(question)
            st.info(hint)
        
        submit = st.button("Kirim Jawaban", key=f"{key_prefix}_submit")
        
        if submit:
            if answer == correct_answer:
                st.success("Jawaban Anda benar!")
            else:
                st.error(f"Jawaban Anda salah. Jawaban yang benar adalah: {correct_answer}")

    # Judul aplikasi
    st.title("Latihan Soal dengan Bantuan Chatbot")

    # Memuat data kuis dari file JSON
    quiz_data = load_quiz_data('quiz_data.json')

    if quiz_data:
        # Loop untuk menampilkan setiap soal
        for idx, question_data in enumerate(quiz_data):
            question = question_data['question']
            options = question_data['options']
            correct_answer = question_data['correct_answer']
            display_question(question, options, correct_answer, f"q{idx}")
            st.write("---")  # Garis pemisah antar soal
    else:
        st.error("Tidak ada data kuis yang ditemukan.")
