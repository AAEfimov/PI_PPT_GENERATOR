FROM python:3.8.10

# Expose port you want your app on
EXPOSE 8501

# install requirements
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /server
COPY . .
COPY gpt_ollama.py gpt.py 

# Run
CMD streamlit run streamlit_api.py
