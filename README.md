# OOI Data Stream Repo Sync

Github actions for syncing data stream repositories in ooi-data

## Inputs

### `GH_ORG`

**Required** Github Organization String.

### `GH_MAIN_BRANCH`

Main Branch to run the workflow in.

### `DEBUG`

Debug flag. If activated, won't actually run workflow

## Outputs

### `sync_status`

Syncing Status

## Example usage

```yaml
uses: ooi-data/sync-data-stream-action@main
with:
  GH_ORG: ooi-data
  DEBUG: "false"
```
