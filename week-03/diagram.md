
# Week 03 — Architecture Diagram

## Container View

```mermaid
flowchart TB
    subgraph A["Machine 1 — Registrar Office"]
        CLI["cli.py"]
        Service["MaterialService"]
        Store["MaterialStore Interface"]
        Local["LocalMaterialStore"]
        Remote["RemoteMaterialStore — HTTP Adapter"]
        Files["local_materials/"]

        CLI --> Service
        Service --> Store
        Store --> Local
        Store --> Remote
        Local --> Files
    end

    subgraph B["Machine 2 — Faculty IT"]
        Server["File Server :8102"]
        Storage["server_files/"]

        Server --> Storage
    end

    Remote -->|"HTTP GET / PUT — 2 s timeout"| Server
```

## Network Boundary

The network boundary separates the Registrar application from the Faculty IT file server.

The RemoteMaterialStore adapter handles HTTP communication, timeouts and errors.

The MaterialService depends only on the MaterialStore interface and does not know which implementation is used.

## Failure Handling

- MaterialsUnavailable: server unreachable or timeout.
- MaterialNotFound: requested file does not exist.
- Timeout: 2 seconds for remote requests.
- The student management functionality remains available when the file server is down.
