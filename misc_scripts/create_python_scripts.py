import pandas as pd
import os
from datetime import datetime
from pathlib import Path

developer = "Azizan Wazir"
def log_msg(status, msg):
    date_str = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    status = status.upper().ljust(8)
    print("{} :: {} - {}".format(date_str, status, msg))

def create_python_files(drafts_folder, euler_file):
    # read Excel file containing Project Euler problems 
    # columns: id, title
    df_euler = pd.read_excel(euler_file)

    # get dictionary of records
    euler_dict = df_euler.to_dict('records')

    successful_files = []
    skipped_files = []
    failed_files = []

    for record in euler_dict:
        id = record.get('id')
        title = record.get('title')
        filename = "problem_{}.py".format(id)
        file_path = os.path.join(drafts_folder, filename)

        try:

            if os.path.isfile(file_path):
                log_msg("info", "{} already exists. Skipping this file.".format(filename))
                skipped_files.append(str(id))
            else:
                with open(file_path, 'w') as f:
                    f.write('''# Project Euler Problem {}
# Developer: {}
# Title: {}

# Project Euler Website: https://projecteuler.net/archives
                            
import time
from datetime import datetime

# for custom command line logging                            
def log_msg(status, msg):
    date_str = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    status = status.upper().ljust(8)
    print("{{}} :: {{}} - {{}}".format(date_str, status, msg))
                            
def main():
    pass
                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem {}")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {{}} seconds".format(end_time))
                            '''.format(id, developer, title, id))
                    
                log_msg("success", "{} successfully created.".format(filename))
                successful_files.append(str(id))

        except:
            log_msg("error", "{} could not be created or opened.".format(filename))
            failed_files.append(str(id))

    if len(successful_files) > 0:
        log_msg("success", "{} files created into the 'drafts' folder. Good luck!".format(len(successful_files)))

    if len(skipped_files) > 0:
        log_msg("warning", "{} files were skipped because files with the same name already exist. Problem IDs: {}".format(len(skipped_files), ", ".join(skipped_files)))
    
    if len(failed_files) > 0:
        log_msg("warning", "{} files could not be created. Problem IDs: {}".format(len(failed_files), ", ".join(skipped_files)))
    
def main():
    current_folder = Path( __file__ ).parent.parent.absolute()
    drafts_folder = os.path.join(current_folder, "drafts")
    
    if not os.path.isdir(drafts_folder):
        log_msg("info", "Drafts folder not found. Creating drafts folder now.")
        os.mkdir(drafts_folder)
    
    log_msg("info", "Searching for project_euler.xlsx")
    euler_file = os.path.join(current_folder, "project_euler.xlsx")
    
    if not os.path.isfile(euler_file):
        log_msg("error", "project_euler.xlsx not found! Please ensure the Excel file is available. Expected columns: id, title")
        return -1
    else:
        log_msg("info", "project_euler.xlsx found. Creating Python files now.")
    
    create_python_files(drafts_folder, euler_file)

    return 0

if __name__ == "__main__":
    main()

