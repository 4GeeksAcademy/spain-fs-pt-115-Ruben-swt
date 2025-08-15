from flask import Blueprint,jsonify,request
from flask_cors import CORS
from api.models import Author,db

author_bp= Blueprint("author", __name__, url_prefix="/author")

CORS(author_bp)

@author_bp.route("/", methods=["GET"])
def get_author():
    authors= Author.query.all()
    return jsonify([a.serialize() for a in authors])

@author_bp.route("/<int:author_id>", methods=["GET"])
def get_user(author_id):
    author = Author.query.get(author_id)
    if author:
        return jsonify(author.serialize()),200
    return jsonify({"msg":"Author no encontrado"}),404
    
@author_bp.route("/", methods=["POST"])
def post_author():
    authors= Author.query.all()
    data =request.get_json()
    complete_name= data.get("complete_name") 

    if not complete_name:
        return jsonify({"msg":"Faltan datos por rellenar"})
    
    for author  in authors:
        if author.complete_name == complete_name:
            return jsonify({"msg": "Autor ya existe."})
        
    new_author= Author(complete_name= complete_name )
    db.session.add(new_author)
    db.session.commit()
    return jsonify({"msg":"Autor registrado."}),200

@author_bp.route("/<int:author_id>", methods=["DELETE"] )
def delete_id(author_id):
    author= db.session.get(Author,author_id)

    if not author:
        return jsonify("Datos no encontrados"),400
    
    db.session.delete(author)
    db.session.commit()
    return jsonify({"msg":"Author eliminado correctament"})







