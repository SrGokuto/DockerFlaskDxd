# Mi App Flask con Docker

Aplicacion Flask desplegada con Docker, Nginx y MySQL.

## Estructura

```
├── .github/workflows/deploy.yml  ← CI/CD: publica imagen en Docker Hub
├── nginx/default.conf            ← Proxy inverso hacia Flask
├── Dockerfile                    ← Imagen Python + Flask
├── docker-compose.yml            ← nginx + MySQL + Flask
├── requirements.txt              ← dependencias Python
├── sample_app.py                 ← App Flask
└── .env.example                  ← Plantilla de variables de entorno
```

## Despliegue local

1. Copia el archivo de ejemplo de variables:
   ```bash
   cp .env.example .env
   ```

2. Edita `.env` con tu password y nombre de base de datos.

3. Levanta los servicios:
   ```bash
   docker compose up -d
   ```

4. Accede a http://localhost

## GitHub Actions

Para que el CI/CD funcione, configura estos secrets en tu repositorio (Settings > Secrets):

- `DOCKER_USERNAME`: tu usuario de Docker Hub
- `DOCKER_PASSWORD`: tu token de Docker Hub

Cada push a `main` construira y subira la imagen automaticamente.
