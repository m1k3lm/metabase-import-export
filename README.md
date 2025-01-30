# Metabase Import/Export Tool

This repository contains tools to export and import Metabase questions, dashboards, and queries using the Metabase API. The purpose of this repository is to provide an easy way to manage Metabase content through version control and automation.

## How to Use

### Exporting Metabase Content

1. Clone the repository:
   ```sh
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the export script:
   ```sh
   python scripts/export_metabase.py
   ```

   This will export the existing queries, questions, and dashboards from Metabase and save them to a file.

### Importing Metabase Content

1. Clone the repository:
   ```sh
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the import script:
   ```sh
   python scripts/import_metabase.py
   ```

   This will read the data from a file and import the queries, questions, and dashboards into Metabase.

## Setting Up GitHub Actions

To automate the import and export process using GitHub Actions, follow these steps:

1. Create a new file in the `.github/workflows` directory called `metabase-import-export.yml`.

2. Define the necessary steps to authenticate with the Metabase API, export existing queries, questions, and dashboards, and import them into Metabase.

3. Commit and push the changes to your repository. GitHub Actions will automatically run the workflow based on the defined triggers.
