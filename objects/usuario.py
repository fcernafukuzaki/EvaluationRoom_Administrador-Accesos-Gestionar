from configs.flask_config import db, ma

class Usuario(db.Model):
    __table_args__ = {"schema": "evaluationroom", 'extend_existing': True}
    __tablename__ = 'usuario'
    
    idusuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())
    correoelectronico = db.Column(db.String())
    activo = db.Column(db.Boolean())
    
    def __init__(self, id_usuario=None, nombre=None, email=None, activo=False):
        self.idusuario = id_usuario
        self.nombre = nombre
        self.correoelectronico = email
        self.activo = activo

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('idusuario','nombre','correoelectronico','activo')
