## Requirements

- `python` = `3.11.6`
- `docker` >= `25.0.3`
- `docker-compose` >= `1.29.2`

## Project setup

1. Create a virtual environment `python3 -m venv .venv` and activate it
2. Install requirements `pip install -r requirements.txt`
3. Start postgres and redis `docker-compose up`
4. Start the web worker `make start_local_web_worker`
5. Start the web server `make start_local_web_server`
