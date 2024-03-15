from flask import Flask, request, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        csv_file = request.files['file']
        if not csv_file:
            return 'No file'

        data_frame = pd.read_csv(csv_file)
        top_cities = data_frame.nlargest(3, 'Population')
        avg_population = data_frame['Population'].mean()
        median_population = data_frame['Population'].median()

        return render_template('display.html', tables=[top_cities.to_html(classes='data')], titles=top_cities.columns.values,
                               avg_population=avg_population, median_population=median_population)

    return '''
        <html>
            <body>
                <h1>The task will be performed in docker</h1>
                <h1>Upload CSV File</h1>
                <form method="post" action="/" enctype="multipart/form-data">
                    <input type="file" name="file">
                    <input type="submit">
                </form>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
