def statusname(sid):
    from app import app
    return app.config["STATUSES"][sid]
