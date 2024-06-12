# Utiliser l'image de base Alpine
FROM alpine

# Installer curl
RUN apk add --no-cache curl

# Copier le fichier de configuration dans l'image
COPY config.txt /app/config.txt

# Commande par défaut
CMD ["echo", "Hello, World!"]
