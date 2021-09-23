# Cyclone Idai

Shared data and layers for Cyclone Idai

# Layer Validator

Updating layer specifications only to find you missed a comma or some curly brackets after hours of starring on your screen can be a pain. Such errors can be hard to detect when reviewing data, and may lead to unwanted bugs on stage and production instances. The layer validator seeks to check the formats of all JSON files on commit, ensuring all layers have the correct format before pushing the files. It also allows for implementation of complex data validation logic via declarative schemas for your JSON data using [ajv schema validator](https://ajv.js.org/). Schemas can be generated from existing layers using schema generators such as [jsonschema.net](https://jsonschema.net/). The current schema can be found inside validation-schema directory located in the root directory.

## Usage

To validate all layers in the repository

```js
// Pre-requisite for all npm related commands    (installs npm packages)
npm install

// Validates all layers against provided schema
npm run validate

```

On `git commit` a format and schema validation will run against committed files.
