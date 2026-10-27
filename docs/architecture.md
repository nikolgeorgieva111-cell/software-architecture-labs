
# Software Architecture — Materials Management

## 4. System Context

The Registrar application manages course materials through the MaterialService and MaterialStore interface.

An external Faculty IT file server provides remote storage for course materials. The application communicates with this server through the RemoteMaterialStore adapter using HTTP requests with a 2-second timeout.

The Faculty IT file server is outside the application's ownership and deployment boundary.

## 5. Contract at the Boundary

| Operation | Contract | Failure |
|---|---|---|
| list(course_id) | Returns a list of material names | MaterialsUnavailable |
| read(course_id, filename) | Returns file contents as bytes | MaterialNotFound, MaterialsUnavailable |
| write(course_id, filename, content) | Stores file contents | MaterialsUnavailable |

The MaterialStore interface is implemented by LocalMaterialStore and RemoteMaterialStore.

The remote adapter translates HTTP and network errors into domain-level exceptions. It also supports both API v1 and API v2 list response formats.

## 8. Deployment

The system consists of two separately deployed processes on different machines.

**Machine 1 — Registrar Office:** Runs the CLI, MaterialService and RemoteMaterialStore adapter.

**Machine 2 — Faculty IT:** Runs the external HTTP file server and stores the course material files.

The two processes communicate over HTTP. The Registrar application uses a 2-second request timeout and handles remote server failures without crashing.

Faculty IT owns and maintains the file server independently of the Registrar application.
