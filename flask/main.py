from website import create_app

app = create_app()

# Apenas se rodarmos o arquivo, não roda se der um import 
if __name__ == '__main__':
    app.run(debug=True)