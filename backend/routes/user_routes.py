from flask import Blueprint, jsonify
from ..services.user_service import get_users

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/')
def list_users():
    return jsonify(get_users())
