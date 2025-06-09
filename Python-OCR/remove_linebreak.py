def remove_linebreaks(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        text = infile.read()

    # Replace "-\n" with "" (removes dash and linebreak)
    text = text.replace("-\n", "")
    # Replace remaining single linebreaks with space
    text = text.replace("\n", " ")

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python remove_linebreaks.py input.txt output.txt")
    else:
        remove_linebreaks(sys.argv[1], sys.argv[2])