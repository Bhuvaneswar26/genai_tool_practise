import csv

TABLE_NAME = "nasdaq_prices"
DATABASE_ENGINE = "InnoDB"
DEFAULT_CHARSET = "latin1"
INPUT_FILENAME = "prices.csv"
SCHEMA_OUTPUT = "mysqlCreateSchema.sql"
VALUES_OUTPUT = "mysqlInsertValues.sql"


def process_csv(input_file, schema_file, values_file):
    with open(input_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        headers = [header.strip().replace(" ", "_") for header in headers]

        column_types = {}
        column_lengths = {}
        decimal_lengths = {}

        rows = []
        for row in reader:
            processed_row = []
            for i, value in enumerate(row):
                value = value.strip().replace("'", "\\'")
                if not value:
                    value = "0"
                processed_row.append(value)

                # Determine column type and length
                if i not in column_types:
                    column_types[i] = "int"
                    column_lengths[i] = 0
                    decimal_lengths[i] = (0, 0)

                if value.isdigit():
                    column_lengths[i] = max(column_lengths[i], len(value))
                elif value.replace(".", "", 1).isdigit():
                    column_types[i] = "decimal"
                    integer_part, _, decimal_part = value.partition(".")
                    decimal_lengths[i] = (
                        max(decimal_lengths[i][0], len(integer_part)),
                        max(decimal_lengths[i][1], len(decimal_part)),
                    )
                else:
                    column_types[i] = "varchar"
                    column_lengths[i] = max(column_lengths[i], len(value))

            rows.append(processed_row)

        # Write schema file
        with open(schema_file, "w") as schema_out:
            schema_out.write(f"CREATE TABLE `{TABLE_NAME}` (\n")
            for i, header in enumerate(headers):
                if column_types[i] == "decimal":
                    length = decimal_lengths[i][0] + decimal_lengths[i][1]
                    schema_out.write(
                        f"  `{header}` {column_types[i]}({length},{decimal_lengths[i][1]})"
                    )
                else:
                    schema_out.write(
                        f"  `{header}` {column_types[i]}({column_lengths[i]})"
                    )
                if i < len(headers) - 1:
                    schema_out.write(",\n")
            schema_out.write(
                f"\n) ENGINE={DATABASE_ENGINE} DEFAULT CHARSET={DEFAULT_CHARSET};\n"
            )

        # Write values file
        with open(values_file, "w") as values_out:
            for row in rows:
                values_out.write(
                    f"INSERT INTO {TABLE_NAME} ({', '.join(headers)}) VALUES "
                    f"({', '.join(f'\"{value}\"' for value in row)});\n"
                )


if __name__ == "__main__":
    process_csv(INPUT_FILENAME, SCHEMA_OUTPUT, VALUES_OUTPUT)
    print("Process completed.")