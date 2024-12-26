# Steps to Run the Project
## Create a virtual environment
```bash 
py -m venv venv
```
## Activate the virtual environment:

```bash 
venv\Scripts\activate
```
## Install Python Requirements

```bash 
pip install -r requirements.txt
```
## Initialize the Database

```bash 
python migrations/setup_db.py
```
## Seed Initial Data
```bash 
python data/seed_data.py

```
## Start the Application

```bash 
python app/main.py
```
### The server will start running, typically on http://127.0.0.1:5000