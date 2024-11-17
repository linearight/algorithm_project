from flask import Flask, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__)

def parse_rs3(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    relations = []
    segments = []
    groups = []

    for rel in root.findall('.//rel'):
        relations.append({'name': rel.get('name'), 'type': rel.get('type')})
        
    for seg in root.findall('.//segment'):
        segments.append({
            'id': seg.get('id'),
            'parent': seg.get('parent'),
            'relname': seg.get('relname'),
            'text': seg.text,
        })
    for group in root.findall(".//group"):
        groups.append({
            'id': group.get('id'),
            'type': group.get('type'),
            'parent': group.get('parent'),
            'relname': group.get('relname'),
            
        })
    
    
    return {'relations': relations, 'segments': segments, 'groups': groups}

@app.route('/')
def index():
    rs3_data = parse_rs3('static/file.rs3')
    return render_template('fuck.html', rs3_data=rs3_data)

if __name__ == "__main__":
    app.run(debug=True)