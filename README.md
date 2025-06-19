# What is Tooyou?
Tooyou is a simple python API REST application to manage orders:

- Search for items available
- Recieve order requests
- Verifiy its disponibility
- Save it in the database
- Recieve Payments (and verify for duplication)
- Deliver the order at the end


## Initial purpose
It was created to serve like a study project for me, to learn some concepts like:

- Docker
- The Python ORM sqlalchemy
- Unit tests
- The Decorator design pattern
- FastAPI


# First steps
1. After cloning it, create a virtual environment with `python3 -m venv .venv`
2. Activate it with `source .venv/bin/activate` for linux or `.venv\Scripts\activate` for winodws
3. Run `pip install -r requirements.txt` to install all the dependecies

## To bootstrap the database:

1. First, create the migration: `alembic revision -m 'migration'`
> From there, you need to do these steps every time you want run the application.
2. Second, you need to build the mysql container: `docker build --tag <container_tag> ./.docker`
3. And then run `docker run -p <port>:3306 -e MYSQL_ROOT_PASSWORD=<password> <container_tag>`

> REMEMBER:
> - Replace`<password>` and `<port>` with the values you created in your own `.env` file.
> - If you haven´t created one, use the `.env.template`and replace the default values with the desired ones.

4. Finally, run `alembic upgrade head`

## To run the API:

- Simply run `python3 src/main.py` and it will be available at the `htttp://localhost:8000/` address.
