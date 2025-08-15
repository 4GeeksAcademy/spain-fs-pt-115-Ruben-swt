
from flask import Blueprint,jsonify,request
from flask_cors import CORS
from api.models import User,db

user_bp= Blueprint("users", __name__, url_prefix="/users")

CORS(user_bp)

@user_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.serialize()for u in users])

@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user= User.query.get(user_id)
    if user:
        return jsonify(user.serialize()),200
    return jsonify({"msg":"Usuario no encontrado"}),404

@user_bp.route("/", methods=["POST"])
def post_user():
    users=User.query.all()
    data =request.get_json()
    username= data.get("username")
    email= data.get("email")
    password= data.get("password")
    
    if not username or not email or not password:
        return jsonify({"msg":"Faltan datos por rellenar"})
    
    for user in users :
        if user.username== username or user.email== email:
            return jsonify({"msg":"Username o email ya existente."})

    new_user = User(username= username, email= email, password= password, is_active=True)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg":"Usuario creado" })

@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user= db.session.get(User,user_id)
    if not user :
        return jsonify("Datos no encontrados"),404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({"msg": "Usuario eliminado correctamente"})






    