from app import create_app

app = create_app()

if __name__ == "__main__":
    # 로컬 디버그용 (컨테이너에서는 gunicorn 사용)
    app.run(host="0.0.0.0", port=8000, debug=True)
