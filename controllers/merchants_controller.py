from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    active_merchants = []
    deactivated_merchants = []
    for merchant in merchants:
        if merchant.active == True:
            active_merchants.append(merchant)
        else:
            deactivated_merchants.append(merchant)
    return render_template("merchants/index.html", active_merchants = active_merchants, deactivated_merchants = deactivated_merchants)

@merchants_blueprint.route("/merchants/<id>/delete", methods=['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/add")
def add_merchant():
    return render_template("merchants/add.html")

@merchants_blueprint.route("/merchants/add", methods=['POST'])
def new_merchant():
    merchant = Merchant(request.form['name'], request.form['description'])
    merchant_repository.save(merchant)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/edit.html", merchant = merchant)

@merchants_blueprint.route("/merchants/<id>/edit", methods=['POST'])
def update_merchant(id):
    merchant = merchant_repository.select(id)
    merchant_repository.update(merchant, request.form['name'], request.form['description'], merchant.active)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/deactivate")
def deactivate_merchant(id):
    merchant = merchant_repository.select(id)
    merchant_repository.update(merchant, merchant.name, merchant.description, False)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/reactivate")
def reactivate_merchant(id):
    merchant = merchant_repository.select(id)
    merchant_repository.update(merchant, merchant.name, merchant.description, True)
    return redirect("/merchants")
