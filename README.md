# Cyclone Idai

Shared data and layers for Cyclone Idai

# Layer Validator

![alt text](layer-valid-dfd.jpeg)

Updating layer specifications only to find you missed a comma or some curly brackets after hours of starring on your screen can be a pain. Such errors can be hard to detect when reviewing data, and may lead to unwanted bugs on stage and production instances. The layer validator also seeks to check the formats of all JSON files on commit, ensuring all layers have the correct format before pushing the files. On commit, json files will be validated against declarative schemas using [ajv schema validator](https://ajv.js.org/). Schemas can be generated from all existing layers by running ` npm run generate `, this is based on a schema generator [jsonschema.net](https://jsonschema.net/). Schemas for various layers can be found inside validation-schema directory located in the root directory.

## Usage

To validate all layers in the repository

```js
// Pre-requisite for all npm related commands    (installs npm packages)
npm install

// Validates all layers against provided schema
npm run validate

// Generates schemas for all layers (Not necessarry if you have no new layers)
npm run generate

```

On `git commit` a format and schema validation will run against all committed  JSON files inside moz folder.
