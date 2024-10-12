# labossi.fr

Code source pour le site labossi.fr

## Running dev profile

```bash
## Not daemonized, see logs
docker compose -f docker-compose-dev.yml up --build 
```

## Running prod profile

```bash
## Stop the current server
docker compose down
## Daemonized
docker compose -f docker-compose-prod.yml up --build -d
# attach to output
docker attach app-app
# see last 200 lines of logs and follow the current ones
docker logs --tail 200 --follow app-app
```
