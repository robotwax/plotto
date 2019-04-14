def load_graph():
    with open('plotto-graph.html', 'rb') as htmlContent.text:
        jsonD = json.dumps(htmlContent.text)
        return jsonD