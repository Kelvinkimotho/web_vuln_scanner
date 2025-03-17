import os
import pandas as pd
import re

def sanitize_filename(url):
    """Sanitize URL to a valid filename (remove special characters)."""
    return re.sub(r'[<>:"/\\|?*]', '_', url)  # Replace invalid characters with "_"

def generate_csv_report(target_url, scan_results):
    sanitized_filename = sanitize_filename(target_url) + "_scan_report.csv"
    report_dir = "reports"

    # Ensure the reports directory exists
    os.makedirs(report_dir, exist_ok=True)

    file_path = os.path.join(report_dir, sanitized_filename)

    # Save the results to CSV
    df = pd.DataFrame(scan_results)
    df.to_csv(file_path, index=False)

    return sanitized_filename  # Return just the filename, not full path
