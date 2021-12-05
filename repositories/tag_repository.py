from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name, active) VALUES (%s, %s) RETURNING id"
    values = [tag.name, tag.active]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row['name'], row['active'], row['id'])
        tags.append(tag)
    return tags


def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['name'], result['active'], result['id'])
    return tag

def select_by_name(name):
    tag = None
    sql = "SELECT * FROM tags WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['name'], result['active'], result['id'])
    return tag

def update(tag, new_name, new_active):
    sql = "UPDATE tags SET (name, active) = (%s, %s) WHERE id = %s"
    values = [new_name, new_active, tag.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

