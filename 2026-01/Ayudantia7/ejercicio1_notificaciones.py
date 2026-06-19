class Notificacion:
    """Clase base para notificaciones."""
    def __init__(self, destinatario: str):
        self.destinatario = destinatario

    def enviar(self) -> str:
        return "Enviando notificación general..."

class NotificacionEmail(Notificacion):
    """Subclase para notificaciones por correo."""
    def __init__(self, destinatario: str, asunto: str):
        super().__init__(destinatario)
        self.asunto = asunto

    def enviar(self) -> str:
        return f"Enviando correo a {self.destinatario} con el asunto '{self.asunto}'."

class NotificacionSMS(Notificacion):
    """Subclase para notificaciones por SMS."""
    def __init__(self, destinatario: str, numero_telefono: str):
        super().__init__(destinatario)
        self.numero_telefono = numero_telefono

    def enviar(self) -> str:
        return f"Enviando SMS al número {self.numero_telefono} para {self.destinatario} con un código de verificación."

# Script de prueba
if __name__ == "__main__":
    notificaciones = [
        NotificacionEmail("estudiante@uoh.cl", "Bienvenido a POO"),
        NotificacionSMS("Profe", "+56912345678")
    ]

    for notif in notificaciones:
        print(notif.enviar())
