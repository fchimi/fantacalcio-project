#--kind python:default
#--web true
#--param POSTGRES_URL $POSTGRES_URL
 
import psycopg

def main(args):

    response = {"body": {}}

    with psycopg.connect(args.get("POSTGRES_URL")) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Execute a command: this creates a new table
            #cur.execute("""
            #    CREATE EXTENSION IF NOT EXISTS "pgcrypto";
            #    CREATE TABLE IF NOT EXISTS tbl_e1 (
            #        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            #        message varchar(100)        
            #    );
            #    """)

            # Pass data to fill a query placeholders and let Psycopg perform
            # the correct conversion (no SQL injections!)
            #cur.execute("INSERT INTO tbl_e2(message) VALUES(%(message)s)",{"message":"Esempio messaggio e4"})
            # Make the changes to the database persistent

            # Query the database and obtain data as Python objects.
            cur.execute("DROP TABLE tbl_e2")
            #record = cur.fetchall()
            #response["body"] = record
            conn.commit()

    return response
