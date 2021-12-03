from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name) VALUES (%s) RETURNING id"
    values = [tag.name]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def update(tag, new_name):
    sql = "UPDATE tags SET name = %s WHERE id = %s"
    values = [new_name, tag.id]
    run_sql(sql, values)