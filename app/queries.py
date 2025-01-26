class Queries:
    CREATE_USERS_TABLE = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100),
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL
    );
    """

    CREATE_TODOS_TABLE = """
    CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        taskname VARCHAR(100) NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status BOOLEAN DEFAULT FALSE,
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
    );
    """

    INSERT_USER = """
    INSERT INTO users (fullname, email, password)
    VALUES (%s, %s, %s)
    RETURNING id;
    """

    INSERT_TODO = """
    INSERT INTO todos (taskname, description, user_id)
    VALUES (%s, %s, %s)
    RETURNING id;
    """

    GET_USER_BY_EMAIL = """
    SELECT * FROM users WHERE email = %s;
    """

    GET_TODOS_BY_USER = """
    SELECT * FROM todos WHERE user_id = %s;
    """

    UPDATE_TODO_STATUS = """
    UPDATE todos SET status = %s WHERE id = %s RETURNING id;
    """

    DELETE_TODO = """
    DELETE FROM todos WHERE id = %s RETURNING id;
    """

    DROP_ALL_TABLES = """
    DROP TABLE IF EXISTS todos, users CASCADE;
    """
