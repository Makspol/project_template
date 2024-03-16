import app.io.input as reader
import app.io.output as writer

RESOURCES = './data/'


def main():
    data = reader.read_line_from_console('Write anything: ')
    writer.write_to_console(data)
    writer.write_file(data, RESOURCES + 'line_from_console.txt')

    data = reader.read_file(RESOURCES + 'text.txt')
    writer.write_to_console(data)
    writer.write_file(data, RESOURCES + 'data_from_file.txt')

    data = reader.read_file_with_pandas(RESOURCES + 'csv.csv')
    writer.write_to_console(data.to_string())
    writer.write_file(data.to_string(), RESOURCES + 'data_from_file_csv.txt')
    writer.write_file_with_pandas(data, RESOURCES + 'data_from_file_csv.csv')


if __name__ == "__main__":
    main()
