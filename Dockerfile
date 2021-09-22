FROM continuumio/anaconda3
COPY . /usr/app
EXPOSE 8501
WORKDIR /usr/app
RUN pip install --upgrade pip && \
pip install --upgrade --no-cache-dir --ignore-installed -r requirements.txt
CMD streamlit run user_interface.py