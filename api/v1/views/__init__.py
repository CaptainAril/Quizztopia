#!/usr/bin/python3

from flask import Blueprint

app_views = Blueprint('app_views', __name__)
auth = Blueprint('auth', __name__)

from api.v1.views.questions import *
from api.v1.views.categories import *
from api.v1.auth import *
