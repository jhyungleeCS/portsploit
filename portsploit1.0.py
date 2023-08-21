from flask import Flask, request, render_template
import shodan
import csv
import pandas as pd
import os
import json

app = Flask(__name__, template_folder=os.path.abspath('templates')) #this calls index.html

print(os.path.abspath('results.csv'))

# use print(os.path.abspath('templates' or 'static') to figure out where flask is looking for index.html and styles.css
# it is important that flask knows where index.html is and styles.css is

API_KEY = 'AJLsIFeKhIwUR4lV3p5nAtOOOcUq2slu' #parkers api key #'6KvXzZK8Zt9K6hksjl75uB8QOcLUI1L2' #kevins api key

# custom function to generate HTML table with hyperlinks
def generate_html_table(dataframe, url_column, org):
    dataframe = dataframe.drop(columns=['Port(s)'])

    html = '<table id="resultsTable">'
    html += '<thead><tr>' # Add the <thead> and <tr> elements here
    html += ''.join([f'<th>{col}</th>' for col in dataframe.columns])
    html += '</tr></thead>' # Close the <tr> and <thead> elements here
    # html += '<form method="POST" action="/">'
    for _, row in dataframe.iterrows():
        html += '<tr>'
        for col in dataframe.columns:
            cell_value = row[col]
            if col == url_column:
                cell_value = f'<a href="{cell_value}">Speedguide</a>'
            elif col == 'IP Address':
                # Escape the org argument using the json.dumps function
                # print(org)
                # print(org.replace("\"",""))
                org = org.replace("\"", "")
                #escaped_org = json.dumps(org)
                #print(escaped_org)
                # onclick_value = 'shodanSearch(\'' + cell_value + '\', \'' + org + '\')'
                cell_value = f'<form method="POST" action="/" class="no-margin-form"><button type="submit" class="link" name="ip" value="{cell_value}" >{cell_value}</button></form>'
            else:
                cell_value = f'<span class="cell-content" title="{cell_value}">{cell_value}</span>'
            html += f'<td>{cell_value}</td>'
        html += '</tr>'
    # html += '</form>'
    html += '</table>'
    return html
@app.route('/', methods=['GET', 'POST'])
def index():
    # shodan search function
    def shodan_search(query):
        api = shodan.Shodan(API_KEY)

        try:
            results = api.search(query)
            for result in results['matches']:
                result['hostnames'] = result.get('hostnames', [])
            return results
        except shodan.APIError as e:
            print('Error: %s' % e)

    table_html = ''
    merged_df = pd.DataFrame() # Assign a default value to merged_df before the if statement
    if request.method == 'POST':
        print(request.form)
        query = ""
        org = request.form.get('org', '')
        if org:
            query += f'org:"{org}"'

        port = request.form.get('port', '')
        if port:
            query += f' port:{port}'

        ip = request.form.get('ip', '')
        if ip:
            query += f' ip:{ip}'

        print(query)
        results = shodan_search(query)

        with open('results.csv', 'w', newline='') as csvfile:
            fieldnames = ['IP Address', 'Port', 'Organization', 'Hostnames']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for result in results['matches']:
                writer.writerow({'IP Address': result['ip_str'], 'Port': result['port'], 'Organization': result['org'],
                                 'Hostnames': ', '.join(result['hostnames'])})

        df1 = pd.read_csv('results.csv')

        df2 = pd.read_csv('vulnerable-ports.csv')

        merged_df = pd.merge(df1, df2, on='Port')

        merged_df.to_csv('merged.csv', index=False)
        dataframe = merged_df
        table_html = generate_html_table(dataframe, 'IP Address', org)
        table_html = generate_html_table(merged_df,
                                         'Reference', org)  # Use the custom function to generate the HTML table with hyperlinks in the 'Reference' column

    return render_template('index.html', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)