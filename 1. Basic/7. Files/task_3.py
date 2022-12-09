import os


def sorted_files():
    files = {}
    for file in os.listdir("files"):
        with open(os.path.join("files", file), encoding="utf-8") as f:
            item = f.readlines()
            files[file] = len(item)

    sorted_files = sorted(files.items(), key=lambda x: x[1])
    write_text = ""

    with open("result.txt", "w", encoding="utf-8") as w:
        for index, file in enumerate(sorted_files):
            write_text += f"{file[0]}\n{index+1}\n"

            with open(os.path.join("files", file[0]), encoding="utf-8") as f:
                for index, line in enumerate(f):
                    write_text += f"Строка {index+1} - {line.strip()}\n"
                
        w.write(write_text)


if __name__ == "__main__":
    sorted_files()