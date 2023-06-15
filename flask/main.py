from website import create_app

app = create_app()

# Apenas se rodarmos o arquivo, não roda se der um import 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=True)