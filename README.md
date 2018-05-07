# goodtables-gov

A RESTful web service for validating files of tabular data.

Given a data file, applies a
[Goodtables table schema](https://github.com/frictionlessdata/goodtables-py)
and returns the validation results in JSON form.

Using no validator (applies the GoodTables default validator only)

    curl -F 'file=@files/budget.csv' https://goodtables-gov-dev.app.cloud.gov

Using validator defined in a local file

    curl -F 'schema=@files/table_schema.json' -F 'file=@files/budget.csv'   https://goodtables-gov-dev.app.cloud.gov

Using validator defined at a URL

    curl -F 'file=@files/budget.csv' -F 'schema_url=https://raw.githubusercontent.com/18F/goodtables-gov/master/files//table_schema.json' https://goodtables-gov-dev.app.cloud.gov

For readability, you may want to pipe the output through a formatter, like

    curl -F 'file=@files/budget.csv' https://goodtables-gov-dev.app.cloud.gov | python -m json.tool

    curl -F 'file=@files/budget.csv' https://goodtables-gov-dev.app.cloud.gov | jq

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
