# ThingsBoard

## installatie

1.  docker installeren

2.  `docker-compose.yml`

    ``` .yml
    services:
    postgres:
        # restart: always
        image: "postgres:16"
        ports:
        - "5432"
        environment:
        POSTGRES_DB: thingsboard
        POSTGRES_PASSWORD: postgres
        volumes:
        - postgres-data:/var/lib/postgresql/data
    thingsboard-ce:
        restart: always
        image: "thingsboard/tb-node:4.3.1.1"
        ports:
        - "8080:8080"
        - "7070:7070"
        - "1883:1883"
        - "8883:8883"
        - "5683-5688:5683-5688/udp"
        logging:
        driver: "json-file"
        options:
            max-size: "100m"
            max-file: "10"
        environment:
        TB_SERVICE_ID: tb-ce-node
        SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/thingsboard
        depends_on:
        - postgres

    volumes:
    postgres-data:
        name: tb-postgres-data
        driver: local
    ```

    -   `8080:8080` - connect local port 8080 to exposed internal HTTP
        port 8080
    -   `1883:1883` - connect local port 1883 to exposed internal MQTT
        port 1883
    -   `8883:8883` - connect local port 8883 to exposed internal MQTT
        over SSL port 8883
    -   `7070:7070` - connect local port 7070 to exposed internal Edge
        RPC port 7070
    -   `5683-5688:5683-5688/udp` - connect local UDP ports 5683-5688 to
        exposed internal COAP - and LwM2M ports
    -   `tb-postgres-data` - name of the docker volume that stores the
        PostgreSQL's data
    -   `thingsboard-ce` - friendly local name of the ThingsBoard
        container
    -   `restart: always` - automatically start ThingsBoard in case of
        system reboot and - restart in case of failure.
    -   image: "`thingsboard/tb-node:4.3.1.1`" - ThingsBoard docker
        image and version.

3.  `docker compose run --rm -e INSTALL_TB=true -e LOAD_DEMO=true thingsboard-ce`

    -   `INSTALL_TB=true` - Installs the core database schema and system
        resources (widgets, images, rule chains, etc.).
    -   `LOAD_DEMO=true` - Loads sample tenant account, dashboards and
        devices for evaluation and testing.

4.  `docker compose up -d && docker compose logs -f thingsboard-ce`

    of

    `docker compose up`

    inloggegevens

    -   System Administrator: `sysadmin@thingsboard.org` / `sysadmin`
    -   Tenant Administrator: `tenant@thingsboard.org` / `tenant`
    -   Customer User: `customer@thingsboard.org` / `customer`
