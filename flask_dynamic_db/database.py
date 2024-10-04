from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  #without this connect_args, OperationalError (1105, 'unknown error: Code: UNAVAILABLE\nserver does not allow insecure connections, client must use SSL/TLS\n')
  connect_args={
    "ssl": {
      "ssl_ca":
      "/etc/ssl/cert.pem"  #this value is available on planetscale / connect with Python / main.py WITH ssl_ca INSTEAD OF ca
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
      jobs.append(dict(zip(result.keys(), row)))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])