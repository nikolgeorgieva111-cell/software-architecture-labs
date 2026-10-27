# ADR-003: Remote Materials Storage Contract

**Status:** Accepted

## Decision
We chose Option B: keep the existing MaterialStore interface with list, read and write operations, while explicitly defining failure behavior.

A RemoteMaterialStore adapter communicates with the external file server over HTTP, using a 2-second timeout.

## Why
The file server is maintained by another team and may be unavailable, slow or updated independently. The adapter isolates HTTP details from the application logic. Explicit errors allow the CLI to respond without crashing.

## Cost
The solution introduces an additional adapter and requires consistent error handling in both local and remote implementations. Network requests also introduce latency.

## Reconsider When
We will reconsider this decision if the student portal requires richer file metadata or if network traffic makes coarse-grained operations necessary.