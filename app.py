from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carregar dados e limpar
df = pd.read_csv('./data/Relatorio_cadop.csv', delimiter=';', encoding='utf-8')
df = df.dropna(subset=['Nome_Fantasia'])  # Removendo registros sem nome
df['Nome_Fantasia'] = df['Nome_Fantasia'].str.strip()  # Evita espaços extras


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()
    print(f"Buscando por: {query}")

    if not query:
        return jsonify({"error": "A consulta não pode estar vazia."}), 400

    results = df[df['Nome_Fantasia'].str.contains(query, case=False, na=False)]

    # Retorna os 10 resultados mais relevantes (se houver)
    return jsonify(results.head(10).to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)

