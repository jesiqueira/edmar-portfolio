from flask import Flask


def create_app():
    app = Flask(__name__)

    # Importa rotas
    from app.routes.home import home_bp
    from app.routes.projects import projects_bp
    from app.routes.contact import contact_bp
    from app.routes.services import services_bp
    from app.routes.project_detail import project_detail_bp
    from app.routes.seo import seo

    # Registra rotas
    app.register_blueprint(home_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(services_bp)
    app.register_blueprint(project_detail_bp)
    app.register_blueprint(seo)

    # Context processor para o ano atual
    @app.context_processor
    def inject_year():
        from datetime import datetime

        return {"current_year": datetime.now().year}

    return app
