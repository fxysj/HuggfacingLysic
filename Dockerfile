FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# 修改 pip 配置，使用清华源加速安装
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /app

RUN pip install --upgrade pip && pip install --no-cache-dir  -r requirements.txt

RUN python -c "\
from transformers import BertTokenizer, GPT2LMHeadModel; \
model_id = 'uer/gpt2-chinese-lyric'; \
BertTokenizer.from_pretrained(model_id); \
GPT2LMHeadModel.from_pretrained(model_id);"

EXPOSE 9001

CMD ["gunicorn", "app:create_app()", "-c", "gunicorn.conf.py"]
