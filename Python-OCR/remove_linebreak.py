def remove_linebreaks(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        text = infile.read()

    # Temporarily replace triple linebreaks with a placeholder
        placeholder = "<<<TRIPLE_LINEBREAK>>>"
        text = text.replace("\n\n\n", placeholder)

        # Remove "-\n" (dash and linebreak)
        text = text.replace("-\n", "")

        # Remove all remaining single linebreaks
        text = text.replace("\n", " ")

        # Restore triple linebreaks
        text = text.replace(placeholder, "\n\n\n")
        

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(text)


file_path = "OCR-Text/RKG.txt"
output_path = "OCR-Text/RKG_cleaned.txt"
remove_linebreaks(file_path, output_path)