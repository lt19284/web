from website import create_app


app = create_app()


if __name__ == '__main__':
    port = int(os.getenv("PORT", 10080))
    app.run(host="0.0.0.0",port=port)
    app.run(debug=True)
