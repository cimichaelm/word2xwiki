#
# file: word2xwiki.py
#
import os
import glob
import subprocess
import requests
import yaml
import argparse

class WordToXWikiConverter:
    def __init__(self, config_path, dryrun=False, debug=False, verbose=False):
        """Initialize the converter with the configuration file."""
        self.load_config(config_path)
        self.dryrun = dryrun
        self.debug = debug
        self.verbose = verbose
        
    def load_config(self, config_path):
        """Load configuration parameters from a YAML file."""
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.directory = self.config['directory']
        self.xwiki_url = self.config['xwiki_url']
        self.space = self.config['space']
        self.username = self.config['username']
        self.password = self.config['password']

    def traverse_directory(self):
        """Traverse the directory and subdirectories to find all .docx files."""
        docx_files = glob.glob(os.path.join(self.directory, '**', '*.docx'), recursive=True)
        return docx_files

    def convert_to_xwiki(self, doc_path):
        """Convert a Word document to XWiki format using pandoc."""
        result = subprocess.run(['pandoc', doc_path, '-t', 'xwiki'], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Error converting document: {result.stderr}")

        if self.debug:
            print(result.stdout)

        return result.stdout

    def import_to_xwiki(self, page, content):
        """Upload the converted content to XWiki."""
        url = f"{self.xwiki_url}/rest/wikis/xwiki/spaces/{self.space}/pages/{page}"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }
        data = {
            "content": content
        }
        response = requests.put(url, headers=headers, data=data, auth=(self.username, self.password))
        return response.status_code, response.text

    def process_files(self):
        """Process all .docx files in the directory and subdirectories."""
        docx_files = self.traverse_directory()
        for doc_path in docx_files:
            page = os.path.splitext(os.path.basename(doc_path))[0]
            if self.verbose:
                msg = "Processing: {0}".format(page)
                print(msg)

            try:
                xwiki_content = self.convert_to_xwiki(doc_path)
                if not self.dryrun:
                    status_code, response_text = self.import_to_xwiki(page, xwiki_content)
                    if status_code == 200:
                        print(f"Content from {doc_path} imported successfully!")
                    else:
                        print(f"ERROR: Failed to import content from {doc_path}. Status code: {status_code}")
                    if self.debug:
                        print(response_text)
            except Exception as e:
                print(f"An error occurred while processing {doc_path}: {e}")

def main():
    """Main function to parse arguments and start the conversion process."""
    parser = argparse.ArgumentParser(description='Convert Word documents to XWiki format and import them into XWiki.')
    parser.add_argument('-c', '--config', required=True, help='Path to the configuration file')
    parser.add_argument('-n', '--dryrun', required=False, action='store_true', help='Dry run. Do not upload')
    parser.add_argument('-d', '--debug', required=False, action='store_true', help='Debug mode')
    parser.add_argument('-v', '--verbose', required=False, action='store_true', help='Verbose mode')
    args = parser.parse_args()

    converter = WordToXWikiConverter(args.config,dryrun=args.dryrun,debug=args.debug,verbose=args.verbose)
    converter.process_files()

if __name__ == "__main__":
    main()
