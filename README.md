# Cloudlab Integration for Wickie 

`wke-cloudlab` is an extension to `wke` that provides [Cloudlab](cloudlab.us) integration.

You need to first install [genilib](https://github.com/nbastin/genilib.git) to make this work correctly.
Beause genilib is not on pypi, this tool is also not on pypi (yet).

## Usage
### Create Topology XML File
`wke-cloudlab create-xml --num-nodes=5 --hardware-type=c220g2 --username=bob`

### Extract wke Configuration

`wke-cloudlab extract-config manifest.xml`

### Full Workflow
You need the most recent version of [cryptography](https://github.com/pyca/cryptography) (installed from git), because cloudlab uses certificates with unusually large [Object Identifiers](https://en.wikipedia.org/wiki/Object_identifier).

## Defaults
`wke-cloudlab` looks for a `~/.wke-cloudlab.toml` file on startup that can contain default setting.
For example the following config sets the tool to use "c220g5" machines, the "UBUNTU22-64-STD" image, and the username "alice" by default.

```toml
[defaults]
hardware-type="c220g5"
os-image="UBUNTU22-64-STD"
username="alice"
```
