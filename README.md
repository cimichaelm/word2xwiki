# Word2XWiki

This Python program converts Word documents (.docx) to XWiki format and uploads them to an XWiki instance. It traverses all .docx files in a specified directory and subdirectories, processes each file with `pandoc`, and uploads the converted content to XWiki.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/cimichaelm/word2xwiki.git
    cd word2xwiki
    ```

2. Install the package:
    ```bash
    pip install .
    ```
3. Install pandoc

    ```bash
   sudo apt-get install pandoc
    ```

## Configuration

Copy the config-dist.yaml to config.yaml and edit to
create a YAML configuration file with the following structure:
```yaml
directory: "path/to/your/directory"
xwiki_url: "http://your-xwiki-instance"
space: "YourSpace"
username: "your-username"
password: "your-password"
```

## Usage

Run the program with the configuration file:
```bash
word2xwiki -c path/to/config.yaml
```

## Testing

Run the unit tests:
```bash
python -m unittest discover tests
```

## License

This project is licensed under the MIT License.


### Directory Structure
Ensure your directory structure looks like this:
```
word2xwiki/
├── word2xwiki
├   └── word2xwiki.py
├── conf
├   └── config.yaml
├── setup.py
├── README.md
└── tests/
    └── test_word2xwiki.py
```

### How to Install and Run
1. **Clone the repository**:
    ```bash
    git clone https://github.com/cimichaelm/word2xwiki.git
    cd word2xwiki
    ```

2. **Install the package**:
    ```bash
    pip install .
    ```

3. **Run the program**:
    ```bash
    word2xwiki -c path/to/config.yaml
    ```

4. **Run the unit tests**:
    ```bash
    python -m unittest discover tests
    ```

## Issues

- unit tests are setup correctly so they dont work
- some of the formatting information is not preserved such as color.


## Summary

This setup allows you to traverse all Word files in a directory and subdirectories, convert each file to XWiki format using `pandoc`, and upload the converted content to XWiki. All parameters are read from a YAML configuration file, and the code is organized into a class with methods for each function. The program can be installed and run using `setuptools`, and unit tests are provided to ensure the functionality works as expected. Comments are added to each method for clarity, and a README file provides documentation.

