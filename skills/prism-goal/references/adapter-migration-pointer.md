# Adapter migration pointer

Canonical matrix (MAP-001…009):

```text
registry/adapter-migration-matrix.md
```

Also indexed in:

```text
registry/adapter-index.yaml
```

`prism-goal` uses the matrix to choose `bridge` | `distill` | `vendor_pin` | `defer` when recommending the next public surface. It does not perform vendor installs or Lake D producer extraction in Lake B′.
