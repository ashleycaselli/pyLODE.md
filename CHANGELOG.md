## [1.0.3](https://github.com/ashleycaselli/pyLODE.md/compare/1.0.2...1.0.3) (2022-06-11)


### Build and continuous integration

* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.6 ([1d65b3d](https://github.com/ashleycaselli/pyLODE.md/commit/1d65b3d9c8dbafa3076cb43e82a066551af234d3))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.7 ([8ec0e75](https://github.com/ashleycaselli/pyLODE.md/commit/8ec0e7595191b1e6312ebd6f5c3abba1ca331e80))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.8 ([70a78a3](https://github.com/ashleycaselli/pyLODE.md/commit/70a78a3fb3f9a1a28138e3fa5e6ca8368f8545b8))
* **deps:** update docker/login-action action to v2 ([a18ce1e](https://github.com/ashleycaselli/pyLODE.md/commit/a18ce1ebe04995725fe082019be40f2d6923e6f1))
* **deps:** update node.js to 16.15 ([fd78e71](https://github.com/ashleycaselli/pyLODE.md/commit/fd78e71d38b603423eef562bc9553ad4dd217d23))


### Dependency updates

* **core-deps:** update dependency python to v3.10 ([42e44c3](https://github.com/ashleycaselli/pyLODE.md/commit/42e44c31aeaaceb0a53b7958950077ff5202e96d))

### [1.0.2](https://github.com/ashleycaselli/pyLODE.md/compare/1.0.1...1.0.2) (2022-05-03)


### General maintenance

* update renovate.json ([db9ead1](https://github.com/ashleycaselli/pyLODE.md/commit/db9ead100bf061b5921fb86c8b6e86ca3c3b62eb))


### Build and continuous integration

* update config for running in PR branches ([1a4deff](https://github.com/ashleycaselli/pyLODE.md/commit/1a4deff903a5982a2036ca3e0b3e76208ebe1701))


### Dependency updates

* **core-deps:** pin dependency rdflib to ==6.1.1 ([bdad6bf](https://github.com/ashleycaselli/pyLODE.md/commit/bdad6bfb14adbe2e0089d37b181bf3a9bc7cfccb))
* **deps:** add renovate.json ([8b0dc68](https://github.com/ashleycaselli/pyLODE.md/commit/8b0dc68137625d70627369429cc34f7e7a43bc70))

### [1.0.1](https://github.com/ashleycaselli/pyLODE.md/compare/1.0.0...1.0.1) (2022-04-03)


### General maintenance

* **examples:** update the example generator with the right package name ([01855dd](https://github.com/ashleycaselli/pyLODE.md/commit/01855ddcd6bdefeafcf00cda210f607a8a4c7caa))


### Dependency updates

* **core-deps:** update rdflib version ([39e817c](https://github.com/ashleycaselli/pyLODE.md/commit/39e817c2912f52b3f410c4038f6bed93b7e871d9))

## 1.0.0 (2022-04-03)


### Features

* **anchors:** add element type to the uri, used as anchor ([3e9c991](https://github.com/ashleycaselli/pyLODE.md/commit/3e9c991e197f1562f4000dd7808c2eb8f414e792))


### Bug Fixes

* **anchors:** lowerizing the URIs for MD template ([3f4f502](https://github.com/ashleycaselli/pyLODE.md/commit/3f4f502c5acc10febd8b3b83cabcf37e4a034bf8))
* **classes:** add MD and adoc formatted output for classes ([e2de9b8](https://github.com/ashleycaselli/pyLODE.md/commit/e2de9b820b15393c03a15858c7ee969d9d40cb7c))
* **log:** remove .name error in logging ([ccd9d4d](https://github.com/ashleycaselli/pyLODE.md/commit/ccd9d4dfff524aa2a21048a1c9a5dd06d2338def))
* **metadata-template:** add hypen in subsections names ([d48df36](https://github.com/ashleycaselli/pyLODE.md/commit/d48df367663b8b8e928cd66c4af2e3e711241d3e))
* **setup:** add missing comma after description ([c5caaf2](https://github.com/ashleycaselli/pyLODE.md/commit/c5caaf29b8e86ade756e39035c06a7202c11eb1d))
* switch arg order in call to `cast ([0a3be76](https://github.com/ashleycaselli/pyLODE.md/commit/0a3be76fd1f6c5e0b66b21f410ba0a3acdf12ab8))
* update representation of ontology source file (link) in MD output ([13778c4](https://github.com/ashleycaselli/pyLODE.md/commit/13778c46242980c9411b69a12aa02b669f9b6693))


### Revert previous changes

* back to commit #e97240b ([7634745](https://github.com/ashleycaselli/pyLODE.md/commit/76347450df52b30373be3cdea84d0e927046a8ef)), closes [#e97240](https://github.com/ashleycaselli/pyLODE.md/issues/e97240)


### Refactoring

* update package name and info ([a341816](https://github.com/ashleycaselli/pyLODE.md/commit/a341816eddc14f8bcc0c7e9bcaeb31692e978207))


### Style improvements

* update formatting ([2ff7256](https://github.com/ashleycaselli/pyLODE.md/commit/2ff725636ba4425a3dee7b6bc413c8e2b8f8f9f3))


### General maintenance

* **dockerfile:** update Dockerfile ([ee2f092](https://github.com/ashleycaselli/pyLODE.md/commit/ee2f09266ccbbd1af78b2d76867f6c7473b72b80))
* **document-template:** update markdown template ([7a2de5e](https://github.com/ashleycaselli/pyLODE.md/commit/7a2de5e08e78a265af3e9c3ea46f06bf482ca7bc))
* **example:** update example ([e42fc1b](https://github.com/ashleycaselli/pyLODE.md/commit/e42fc1b9f921e57816c756e72cbea0f518e17745))


### Build and continuous integration

* add build config ([4f30d03](https://github.com/ashleycaselli/pyLODE.md/commit/4f30d038d73f90d52e014bc1ed624c9ca55f3dec))
* add package.json for semantic-release ([464451d](https://github.com/ashleycaselli/pyLODE.md/commit/464451dcfa6cfb6921a28ec77f61e904f4b08071))
* add semantic-release config ([474d3ea](https://github.com/ashleycaselli/pyLODE.md/commit/474d3eab3381932210d66c9ea4e8505083a8d855))
