FROM python:3.11-slim

# 시스템 기본 준비
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 의존성
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 복사
COPY app ./app

# 비루트 사용자(보안)
RUN useradd -m runner
USER runner

# Gunicorn으로 서빙 (포트 8000)
EXPOSE 8000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "app.server:app"]
