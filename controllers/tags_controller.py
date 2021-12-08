from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repository
import models.random_stat_generator as generator

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    active_tags = []
    deactivated_tags = []
    for tag in tags:
        if tag.active == True:
            active_tags.append(tag)
        else:
            deactivated_tags.append(tag)
    return render_template("tags/index.html", active_tags = active_tags, deactivated_tags = deactivated_tags)

@tags_blueprint.route("/tags/<id>/delete")
def delete_tag(id):
    tag_repository.delete(id)
    return redirect("/tags")

@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    stat = generator.get_random_stat()
    return render_template("tags/edit.html", tag = tag, stat = stat)

@tags_blueprint.route("/tags/add")
def add_tag():
    stat = generator.get_random_stat()
    return render_template("tags/add.html", stat = stat)

@tags_blueprint.route("/tags/add", methods=['POST'])
def new_tag():
    tag = Tag(request.form['name'])
    tag_repository.save(tag)
    return redirect("/tags")

@tags_blueprint.route("/tags/<id>/edit", methods=['POST'])
def update_tag(id):
    tag = tag_repository.select(id)
    tag_repository.update(tag, request.form['name'], tag.active)
    return redirect("/tags")

@tags_blueprint.route("/tags/<id>/deactivate")
def deactivate_tag(id):
    tag = tag_repository.select(id)
    tag_repository.update(tag, tag.name, False)
    return redirect("/tags")

@tags_blueprint.route("/tags/<id>/reactivate")
def reactivate_tag(id):
    tag = tag_repository.select(id)
    tag_repository.update(tag, tag.name, True)
    return redirect("/tags")

