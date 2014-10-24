from app import db
from app.users.decorators import login_required
from .models import Tickets
from flask import Blueprint, flash, redirect, render_template, request, session, url_for

mod = Blueprint('tickets', __name__, url_prefix="/tickets")


@mod.route('/')
@login_required
def ticketindex():
    pass
