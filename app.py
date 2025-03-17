from flask import Flask, render_template, request, redirect, url_for
from scanners.port_scanner import scan_ports
from scanners.headers_scanner import check_headers
from scanners.ssl_scanner import check_ssl
from scanners.sql_scanner import test_sql_injection
from utils.report_generator import generate_csv_report
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, render_template, request, send_file, abort
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join("reports", filename)

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        abort(404)  # Return a proper 404 response if file is not found


# Home Page

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target_url = request.form['target_url'].strip()
        clean_target = target_url.replace("http://", "").replace("https://", "").strip("/")

        # Run scans in parallel for speed optimization
        with ThreadPoolExecutor() as executor:
            future_ports = executor.submit(scan_ports, clean_target)
            future_headers = executor.submit(check_headers, target_url)
            future_ssl = executor.submit(check_ssl, clean_target)
            future_sql = executor.submit(test_sql_injection, target_url)

            scan_results = {
                'ports': future_ports.result(),
                'headers': future_headers.result(),
                'ssl': future_ssl.result(),
                'sql': future_sql.result(),
            }

        report_filename = generate_csv_report(clean_target, scan_results)
        return render_template('results.html', target=target_url, results=scan_results, report_filename=report_filename)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
