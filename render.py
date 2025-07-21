import json
from pathlib import Path

def load_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_rows(schedule):
    rows = []
    for entry in schedule:
        row_cells = [entry['time'], entry['lunes'], entry['martes'], entry['miercoles'], entry['jueves'], entry['viernes']]
        cells_html = []
        for cell in row_cells:
            cls = ' class="no-servicio"' if cell in ("No hay servicio", "—") else ''
            cells_html.append(f'<td{cls}>{cell}</td>')
        rows.append(f"        <tr>{''.join(cells_html)}</tr>")
    return "\n".join(rows)


def render_template(template_path, output_path, data):
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    rows_html = generate_rows(data['schedule'])
    html = template.replace('{{title}}', data['title']).replace('{{rows}}', rows_html)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    data = load_data('data.json')
    render_template('index.template.html', 'index.html', data)
    print('index.html generado a partir de data.json')
